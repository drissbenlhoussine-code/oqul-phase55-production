export type CycleSlug = "primary" | "middle" | "high";
export type UserRole = "user" | "admin";
export type PlanSlug = "free" | "basic" | "advanced" | "family" | "school";

export interface ApiErrorPayload {
  ok: false;
  message: string;
  code?: string;
}

export interface ApiSuccessPayload<T> {
  ok: true;
  data: T;
}

export type ApiResponse<T> = ApiSuccessPayload<T> | ApiErrorPayload;

export interface NavigationItem {
  label: string;
  href: string;
  description?: string;
}
