# QA Automation Portfolio

![Playwright](https://github.com/ingcristiangarcas/qa-automation-portfolio/actions/workflows/playwright.yml/badge.svg)
![Selenium](https://github.com/ingcristiangarcas/qa-automation-portfolio/actions/workflows/selenium.yml/badge.svg)
![Newman](https://github.com/ingcristiangarcas/qa-automation-portfolio/actions/workflows/api-testing.yml/badge.svg)
![JMeter](https://github.com/ingcristiangarcas/qa-automation-portfolio/actions/workflows/jmeter.yml/badge.svg)

A hands-on quality engineering portfolio demonstrating end-to-end test
automation across UI, API, and multiple tools/languages — built to showcase
real-world QA engineering practices: Page Object Model, CI/CD integration,
and negative-path/edge-case testing, not just happy-path demos.

## Why this repo exists

I work as a Quality Engineer combining manual and automated testing, and this
repo shows the kind of automation work I do day-to-day: designing
maintainable test suites, wiring them into CI/CD pipelines, and choosing the
right tool for the job rather than defaulting to a single favorite stack.

## What's inside

| Folder | Stack | Focus |
|---|---|---|
| [`selenium-suite/`](./selenium-suite) | Python + Selenium + pytest | Classic, widely-adopted E2E automation with Page Object Model |
| [`playwright-suite/`](./playwright-suite) | TypeScript + Playwright | Modern E2E (auto-waiting, tracing) + native API testing |
| [`api-testing/`](./api-testing) | Postman + Newman | API contract/regression testing runnable in CI, shareable with non-technical stakeholders |
| [`jmeter/`](./jmeter) | Apache JMeter | Basic load testing, run headlessly in CI |

All suites target public, purpose-built demo services so anyone can clone and
run them with zero setup cost:
- UI tests: [SauceDemo](https://www.saucedemo.com)
- API tests: [PokéAPI](https://pokeapi.co)

## Quick start

```bash
# Selenium (Python)
cd selenium-suite && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && pytest

# Playwright (TypeScript)
cd playwright-suite && npm install && npx playwright install --with-deps chromium && npm test

# API testing (Postman/Newman)
cd api-testing && npm install -g newman newman-reporter-htmlextra && newman run collections/pokeapi.postman_collection.json -e environments/pokeapi.postman_environment.json --reporters cli,htmlextra --reporter-htmlextra-export report.html

# Load testing (JMeter)
cd jmeter && jmeter -n -t pokeapi-load-test.jmx -l results.jtl
```

## Continuous Integration

Every suite has its own GitHub Actions workflow under
[`.github/workflows/`](./.github/workflows), triggered on every push to its
folder, with HTML reports uploaded as build artifacts. This mirrors how test
suites should be gated in a real CI/CD pipeline: independent, fast to run,
and producing evidence a team can review without re-running tests locally.

## Related work

- Live QA/dev profile: [LinkedIn](https://www.linkedin.com/in/cristian-benjamin-garcia-casierra-216126206)
