import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  retries: process.env.CI ? 2 : 0,
  reporter: [['html', { open: 'never' }], ['list']],
  use: {
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      testDir: './tests/ui',
      use: { ...devices['Desktop Chrome'], baseURL: 'https://www.saucedemo.com' },
    },
    {
      name: 'api',
      testDir: './tests/api',
      // The public PokéAPI rate-limits bursts of concurrent requests, so this
      // project runs its tests serially to keep the suite reliable in CI.
      fullyParallel: false,
      workers: 1,
      use: {
        baseURL: 'https://pokeapi.co/api/v2',
        // GitHub-hosted runners share IPs that PokeAPI's edge network
        // occasionally challenges; a descriptive User-Agent avoids that.
        extraHTTPHeaders: {
          'User-Agent': 'qa-automation-portfolio-playwright-suite',
          Accept: 'application/json',
        },
      },
    },
  ],
});
