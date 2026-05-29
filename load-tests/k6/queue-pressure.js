import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  vus: 60,
  duration: "90s",
  thresholds: {
    http_req_failed: ["rate<0.20"],
  },
};

export default function () {
  const res = http.post(
    "http://localhost:3000/api/ai/leila",
    JSON.stringify({ message: "اختبار ضغط واقعي على runtime" }),
    { headers: { "Content-Type": "application/json" } }
  );

  check(res, {
    "request handled": (r) => r.status < 500,
  });

  sleep(0.5);
}
