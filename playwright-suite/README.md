# Playwright Suite (TypeScript)

Modern end-to-end and API automation suite built with **Playwright** and
**TypeScript**, using the **Page Object Model** pattern and Playwright's
built-in auto-waiting, tracing and API testing capabilities.

This suite covers two very different scenarios on purpose:

- **UI tests** against [SauceDemo](https://www.saucedemo.com) — login flows
  (valid, invalid, locked-out user), cart, and product sorting.
- **API tests** against the public [PokéAPI](https://pokeapi.co) — status
  codes, response shape/schema assertions, and edge cases (404 handling),
  with no browser involved.

## Why Playwright here

This suite exists side-by-side with the `selenium-suite` in this repo on
purpose: it demonstrates a modern automation stack (auto-waiting locators,
built-in trace viewer for debugging failures, native API testing, parallel
execution) rather than testing the exact same thing twice with two tools.

## Stack

- TypeScript
- @playwright/test
- Playwright's `request` fixture for API testing (no extra HTTP client needed)

## Project structure

```
playwright-suite/
├── pages/                  # Page Object classes
├── tests/
│   ├── ui/                 # Browser E2E tests (SauceDemo)
│   └── api/                # API tests (PokéAPI)
└── playwright.config.ts    # Projects: chromium (UI) and api (no browser)
```

## Running the tests locally

```bash
cd playwright-suite
npm install
npx playwright install --with-deps chromium
npm test              # runs both UI and API projects
npm run test:ui       # UI tests only
npm run test:api      # API tests only
npm run report        # opens the last HTML report
```

## Continuous Integration

This suite runs automatically on every push via GitHub Actions
(see `.github/workflows/playwright.yml`). Traces and HTML reports are
uploaded as build artifacts for easy debugging of failures.
