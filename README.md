# QA Automation Portfolio

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
| [`api-testing/`](./api-testing) | Postman + Newman | API regression/contract testing runnable in CI, shareable with non-technical stakeholders |

All suites target public, purpose-built demo services so anyone can clone and
run them with zero setup cost:
- UI tests: [SauceDemo](https://www.saucedemo.com)
- API tests: [PokéAPI](https://pokeapi.co)

## Continuous Integration

Every suite has its own GitHub Actions workflow under
[`.github/workflows/`](./.github/workflows), triggered on every push to its
folder, with HTML reports uploaded as build artifacts. This mirrors how test
suites should be gated in a real CI/CD pipeline: independent, fast to run,
and producing evidence a team can review without re-running tests locally.

## Related work

- Live QA/dev profile: [LinkedIn](https://www.linkedin.com/in/cristian-benjamin-garcia-casierra-216126206)
- Mobile app portfolio: `pokedex-flutter` (companion repo, Flutter + PokéAPI)
