# Load Testing (Apache JMeter)

A basic load test plan against the public [PokéAPI](https://pokeapi.co),
run headlessly (non-GUI mode) so it can execute in CI just like any other
suite in this repo — the same tool and workflow used in my current QA role
to validate performance budgets before a release.

## What it tests

- **Endpoint:** `GET /api/v2/pokemon/pikachu`
- **Load profile:** 10 concurrent threads (users), ramped up over 5 seconds,
  each looping 5 times (50 total requests)
- **Assertions per request:**
  - Response code is `200`
  - Response time is under 2 seconds

This is intentionally small in scope — the goal is to demonstrate a working,
CI-integrated load-testing pipeline (test plan, headless execution, HTML
report as a build artifact), not to load-test a third-party public API
aggressively.

## Running locally

```bash
cd jmeter
jmeter -n -t pokeapi-load-test.jmx -l results.jtl -e -o report/
```

- `-n` runs JMeter in non-GUI (headless) mode
- `-l results.jtl` writes raw results to a file
- `-e -o report/` generates an HTML dashboard report from the results

## Continuous Integration

This test plan runs automatically on every push via GitHub Actions
(see `.github/workflows/jmeter.yml`), with the HTML dashboard report
uploaded as a build artifact.
