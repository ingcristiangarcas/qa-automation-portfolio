import { test, expect } from '@playwright/test';

/**
 * API tests against the public PokéAPI (https://pokeapi.co), showcasing
 * Playwright's built-in `request` fixture for API testing without a browser.
 *
 * Note: request paths are relative (no leading slash) because Playwright's
 * `request` fixture resolves URLs like `new URL(path, baseURL)`; a leading
 * slash would replace the `/api/v2/` segment of the baseURL entirely.
 */
test.describe('PokeAPI - pokemon endpoint', () => {
  test('GET pokemon/pikachu returns expected core fields', async ({ request }) => {
    const response = await request.get('pokemon/pikachu');

    expect(response.status()).toBe(200);

    const body = await response.json();
    expect(body.name).toBe('pikachu');
    expect(body.id).toBe(25);
    expect(body.types.some((t: any) => t.type.name === 'electric')).toBeTruthy();
  });

  test('GET pokemon/{unknown} returns 404', async ({ request }) => {
    const response = await request.get('pokemon/not-a-real-pokemon');

    expect(response.status()).toBe(404);
  });

  test('GET pokemon?limit=10 returns exactly 10 results', async ({ request }) => {
    const response = await request.get('pokemon?limit=10');
    const body = await response.json();

    expect(response.status()).toBe(200);
    expect(body.results).toHaveLength(10);
  });
});
