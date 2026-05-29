import client from "prom-client";

export const registry = new client.Registry();

client.collectDefaultMetrics({
  register: registry,
});

export const httpRequestCounter = new client.Counter({
  name: "oqul_http_requests_total",
  help: "Total HTTP requests",
  labelNames: ["method", "route", "status"],
});

export const aiRequestHistogram = new client.Histogram({
  name: "oqul_ai_request_duration_seconds",
  help: "AI request duration in seconds",
  labelNames: ["provider", "model", "success"],
});

registry.registerMetric(httpRequestCounter);
registry.registerMetric(aiRequestHistogram);
