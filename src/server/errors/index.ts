export class AppError extends Error {
  readonly code: string;
  readonly status: number;
  // Alias used by some parts of the codebase
  get statusCode() { return this.status; }

  constructor(message: string, code = "INTERNAL_ERROR", status = 500) {
    super(message);
    this.name = "AppError";
    this.code = code;
    this.status = status;
  }
}

export const Errors = {
  unauthorized: () => new AppError("يجب تسجيل الدخول أولاً", "UNAUTHORIZED", 401),
  forbidden:    () => new AppError("ليس لديك صلاحية للوصول", "FORBIDDEN", 403),
  notFound:     (r = "العنصر") => new AppError(`${r} غير موجود`, "NOT_FOUND", 404),
  validation:   (msg: string) => new AppError(msg, "VALIDATION_ERROR", 422),
  quota:        () => new AppError("وصلت إلى الحد اليومي. يرجى الترقية للاستمرار", "QUOTA_EXCEEDED", 429),
  internal:     () => new AppError("حدث خطأ داخلي، يرجى المحاولة مجددًا", "INTERNAL_ERROR", 500),
} as const;
