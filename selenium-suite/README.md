# Selenium Suite (Python + pytest)

Cross-browser end-to-end automation suite built with **Selenium WebDriver** and **pytest**,
using the **Page Object Model (POM)** pattern to keep tests readable and maintainable.

This suite targets [SauceDemo](https://www.saucedemo.com), a public site built for
practicing test automation, and validates critical business flows: login (valid,
invalid and locked-out users), adding items to cart, and product sorting.

## Why Selenium here

This suite intentionally uses Selenium (rather than Playwright, see the sibling
`playwright-suite`) to demonstrate the classic, widely-adopted automation stack most
teams still run in production today — the same approach used daily in my current QA
role for regression testing over real APIs and UIs.

## Stack

- Python 3.11+
- Selenium 4 (WebDriver)
- pytest + pytest-html for reporting
- webdriver-manager (no manual driver downloads needed)

## Project structure

```
selenium-suite/
├── pages/              # Page Object classes (BasePage, LoginPage, InventoryPage)
├── tests/               # Test cases, grouped by feature
├── conftest.py          # Shared pytest fixtures (WebDriver setup/teardown)
├── pytest.ini           # Pytest configuration
└── requirements.txt
```

## Running the tests locally

```bash
cd selenium-suite
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest
```

An HTML report is generated at `report.html` after each run.

## Continuous Integration

This suite runs automatically on every push via GitHub Actions
(see `.github/workflows/selenium.yml`), using a headless Chrome browser.
