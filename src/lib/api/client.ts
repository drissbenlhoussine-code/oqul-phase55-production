import type { ApiErrorPayload, ApiResponse, ApiSuccessPayload } from "@/types";

type RequestOptions = Omit<RequestInit, "body"> & {
  body?: unknown;
};

type ServerSuccessPayload<T> = ApiSuccessPayload<T> & {
  success?: true;
  requestId?: string;
};

type ServerFailurePayload = ApiErrorPayload & {
  success?: false;
  error?: string;
  requestId?: string;
};

type ServerPayload<T> = ServerSuccessPayload<T> | ServerFailurePayload;

function isServerSuccess<T>(payload: ServerPayload<T>): payload is ServerSuccessPayload<T> {
  const runtimePayload = payload as { ok?: boolean; success?: boolean };
  return runtimePayload.ok === true || runtimePayload.success === true;
}

function getErrorMessage(payload: ServerFailurePayload | null) {
  return payload?.message ?? payload?.error ?? "تعذر الاتصال بالخادم.";
}

async function request<T>(input: RequestInfo | URL, init?: RequestOptions): Promise<T> {
  const response = await fetch(input, {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...(init?.headers ?? {}),
    },
    body: init?.body === undefined ? undefined : JSON.stringify(init.body),
  });

  const payload = (await response.json().catch(() => null)) as ServerPayload<T> | null;

  if (!response.ok) {
    throw new Error(getErrorMessage(payload as ServerFailurePayload | null));
  }

  if (!payload) {
    throw new Error("استجابة غير صالحة من الخادم.");
  }

  if (!isServerSuccess(payload)) {
    throw new Error(getErrorMessage(payload));
  }

  return payload.data;
}

export const apiClient = {
  get: <T>(url: string, init?: RequestOptions) => request<T>(url, { ...init, method: "GET" }),
  post: <T>(url: string, body?: unknown, init?: RequestOptions) =>
    request<T>(url, { ...init, method: "POST", body }),
  patch: <T>(url: string, body?: unknown, init?: RequestOptions) =>
    request<T>(url, { ...init, method: "PATCH", body }),
  delete: <T>(url: string, init?: RequestOptions) => request<T>(url, { ...init, method: "DELETE" }),
};

export const apiRequest = request;
export type { ApiResponse };
