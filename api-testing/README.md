# API Testing (Postman + Newman)

Postman collection covering functional, negative-path, and contract-testing
scenarios against the public [PokéAPI](https://pokeapi.co), designed to run
headlessly in CI using **Newman** (Postman's command-line collection runner)
— the same tool used in my current QA role to gate API regressions in CI/CD
pipelines.

## Why a separate Postman/Newman folder

Both automation suites in this repo (`selenium-suite`, `playwright-suite`)
already touch APIs and UIs, but this folder focuses specifically on the
Postman/Newman workflow many QA teams already use for API contract and
regression testing, independent of any test framework/language — collections
can be shared with non-technical stakeholders, imported into Postman for
manual exploration, and still run unattended in CI.

## What's covered

- `GET /pokemon/{name}` — happy path: status code, **JSON schema validation**
  (`pm.response.to.have.jsonSchema`), field values, and a response-time budget
- `GET /pokemon/{unknown}` — negative path: expects a 404
- `GET /pokemon?limit=10` — pagination behavior
- `GET /ability/{name}` → `GET /pokemon/{chainedPokemonName}` — a **chained
  request**: the pokemon name returned by the first call is captured into a
  collection variable and reused as the path parameter of the second call,
  demonstrating stateful/contract-style flows rather than isolated requests

`baseUrl` is defined in an external environment file
(`environments/pokeapi.postman_environment.json`) rather than hardcoded in
the collection, so the same collection can be pointed at a different
environment (staging, local, etc.) without editing requests.

## Running locally

```bash
cd api-testing
npm install -g newman newman-reporter-htmlextra
newman run collections/pokeapi.postman_collection.json \
  -e environments/pokeapi.postman_environment.json \
  --reporters cli,htmlextra \
  --reporter-htmlextra-export report.html
```

## Continuous Integration

This collection runs automatically on every push via GitHub Actions
(see `.github/workflows/api-testing.yml`), with the HTML report uploaded
as a build artifact.
