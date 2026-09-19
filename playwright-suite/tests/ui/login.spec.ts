import { test } from '@playwright/test';
import { LoginPage } from '../../pages/LoginPage';
import { InventoryPage } from '../../pages/InventoryPage';

const STANDARD_USER = 'standard_user';
const LOCKED_USER = 'locked_out_user';
const PASSWORD = 'secret_sauce';

test.describe('SauceDemo login', () => {
  test('valid credentials redirect to the inventory page', async ({ page }) => {
    const loginPage = new LoginPage(page);
    const inventoryPage = new InventoryPage(page);

    await loginPage.goto();
    await loginPage.login(STANDARD_USER, PASSWORD);

    await inventoryPage.expectLoaded();
  });

  test('locked out user sees a descriptive error', async ({ page }) => {
    const loginPage = new LoginPage(page);

    await loginPage.goto();
    await loginPage.login(LOCKED_USER, PASSWORD);

    await loginPage.expectErrorContains('locked out');
  });

  test('invalid password shows an error message', async ({ page }) => {
    const loginPage = new LoginPage(page);

    await loginPage.goto();
    await loginPage.login(STANDARD_USER, 'wrong-password');

    await loginPage.expectErrorContains('do not match');
  });
});
