import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  vus: 40,
  duration: "60s",
  thresholds: {
    http_req_failed: ["rate<0.10"],
    http_req_duration: ["p(95)<2500"],
  },
};

export default function () {
  const res = http.get("http://localhost:3000/api/health");

  check(res, {
    "health responds": (r) => r.status === 200,
  });

  sleep(1);
}
