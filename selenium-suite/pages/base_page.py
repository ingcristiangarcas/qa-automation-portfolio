"""Base Page Object with common Selenium interactions shared by all pages."""
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str):
        self.driver.get(url)
        return self

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self._js_click(element)

    def _js_click(self, element):
        """Dispatches a full pointer/mouse event sequence via JS instead of
        WebDriver's native click.

        Root cause (confirmed via debugging): SauceDemo's React front end
        doesn't reliably react to WebDriver's native click on some buttons
        (e.g. "Checkout") — the click registers at the browser/OS level
        (confirmed via elementFromPoint at the click coordinates: the button
        itself, not an overlay, receives it) but React's onClick handler
        simply never fires, so no navigation happens. This reproduced
        consistently in both headless and headed Chrome, ruling out a
        headless-only quirk. Dispatching the event sequence
        (pointerdown/mousedown/pointerup/mouseup/click) directly on the
        element via `execute_script` reliably triggers React's synthetic
        event system (verified 5/5 across fresh runs), where native
        `.click()` was intermittent to consistently failing.
        """
        self.driver.execute_script(
            """
            const el = arguments[0];
            for (const type of ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click']) {
                el.dispatchEvent(new MouseEvent(type, {bubbles: true, cancelable: true, view: window}));
            }
            """,
            element,
        )

    def type(self, locator, text: str, retries: int = 3):
        """Sets `text` into the element at `locator` and verifies it stuck.

        Root cause (confirmed via debugging, same family of issue as
        `_js_click`): SauceDemo's checkout form inputs are React-controlled,
        and `send_keys()` (which drives real per-key CDP input events)
        intermittently fails to trigger React's onChange, so the input's
        value gets reset by the next re-render. The fix is the same idea used
        for clicks: bypass WebDriver's native typing and instead set the
        value through the input's native property setter, then dispatch a
        real `input` event via JS so React's synthetic event system picks it
        up (verified 5/5 across fresh runs, where `send_keys` was flaky).
        Retries remain as a safety net in case a value still doesn't stick.
        """
        for attempt in range(retries):
            if attempt > 0:
                time.sleep(0.4)
            element = self.find(locator)
            self.driver.execute_script(
                """
                const el = arguments[0];
                const nativeSetter = Object.getOwnPropertyDescriptor(
                    window.HTMLInputElement.prototype, 'value'
                ).set;
                nativeSetter.call(el, arguments[1]);
                el.dispatchEvent(new Event('input', {bubbles: true}));
                """,
                element,
                text,
            )
            if element.get_attribute("value") == text:
                return
            if attempt == retries - 1:
                raise AssertionError(
                    f"Failed to type '{text}' into {locator} after {retries} attempts"
                )

    def text_of(self, locator) -> str:
        return self.find(locator).text

    def wait_for_url_contains(self, fragment: str):
        """Waits until the browser has actually navigated to a URL containing
        `fragment`. SauceDemo's React front end sometimes fails to register a
        click that triggers client-side navigation if it fires immediately
        after the previous page transition, so callers should wait for the
        resulting URL rather than assuming the click always succeeds.
        """
        self.wait.until(EC.url_contains(fragment))
        return self

    def click_until_url_contains(self, locator, fragment: str, retries: int = 3):
        """Clicks `locator` (via `_js_click`, see its docstring for why) and
        confirms navigation by polling the URL, retrying as a safety net in
        case a click still doesn't register. A brief settle pause after
        navigation gives the destination page's React components time to
        finish mounting before the caller interacts with them.
        """
        for attempt in range(retries):
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self._js_click(element)
            try:
                WebDriverWait(self.driver, 3).until(EC.url_contains(fragment))
                time.sleep(0.3)
                return self
            except TimeoutException:
                if attempt == retries - 1:
                    raise
        return self
