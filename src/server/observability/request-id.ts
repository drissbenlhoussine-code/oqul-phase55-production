export const REQUEST_ID_HEADER = "x-oqul-request-id";

export function createRequestId() {
  return crypto.randomUUID();
}

export function getRequestIdFromHeaders(headers: Headers) {
  return headers.get(REQUEST_ID_HEADER) ?? createRequestId();
}
