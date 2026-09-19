import { APIRequestContext, APIResponse } from '@playwright/test';

/**
 * Retries a GET request against a flaky third-party API until it returns a
 * successful (2xx/4xx expected) JSON payload, guarding against transient edge
 * network hiccups (e.g. shared CI runner IPs being momentarily challenged).
 */
export async function getWithRetry(
  request: APIRequestContext,
  url: string,
  attempts = 3,
): Promise<APIResponse> {
  let lastResponse: APIResponse | undefined;

  for (let attempt = 1; attempt <= attempts; attempt++) {
    const response = await request.get(url);
    const contentType = response.headers()['content-type'] ?? '';

    if (contentType.includes('application/json')) {
      return response;
    }

    // eslint-disable-next-line no-console
    console.log(
      `[getWithRetry] attempt ${attempt} for ${url} -> status ${response.status()}, ` +
        `content-type "${contentType}", body preview: ${(await response.text()).slice(0, 300)}`,
    );

    lastResponse = response;
    await new Promise((resolve) => setTimeout(resolve, attempt * 500));
  }

  return lastResponse!;
}
