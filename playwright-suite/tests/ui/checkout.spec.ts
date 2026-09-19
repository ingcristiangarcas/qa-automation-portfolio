import { test, expect } from '@playwright/test';
import { LoginPage } from '../../pages/LoginPage';
import { InventoryPage } from '../../pages/InventoryPage';
import { CheckoutPage } from '../../pages/CheckoutPage';

/**
 * End-to-end checkout flow: login -> add item to cart -> checkout info ->
 * order overview -> confirmation. This is the critical business flow (order
 * creation) referenced across the portfolio's README as the kind of flow
 * validated in production QA work.
 */
test.describe('SauceDemo checkout flow', () => {
  test.beforeEach(async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.goto();
    await loginPage.login('standard_user', 'secret_sauce');
  });

  test('a user can complete a full purchase end to end', async ({ page }) => {
    const inventoryPage = new InventoryPage(page);
    const checkoutPage = new CheckoutPage(page);

    await inventoryPage.addFirstItemToCart();
    await checkoutPage.goToCart();
    await checkoutPage.startCheckout();
    await checkoutPage.fillCheckoutInfo('Cristian', 'Garcia', '760001');

    const summary = await checkoutPage.getOrderSummary();
    expect(summary.total).toBeCloseTo(summary.subtotal + summary.tax, 2);

    await checkoutPage.finishOrder();
    await checkoutPage.expectOrderComplete();
  });

  test('checkout info step requires all fields before continuing', async ({ page }) => {
    const inventoryPage = new InventoryPage(page);
    const checkoutPage = new CheckoutPage(page);

    await inventoryPage.addFirstItemToCart();
    await checkoutPage.goToCart();
    await checkoutPage.startCheckout();

    await checkoutPage.continueButton.click();

    await expect(checkoutPage.errorMessage).toContainText('First Name is required');
  });
});
