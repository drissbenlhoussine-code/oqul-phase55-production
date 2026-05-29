import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  vus: 50,
  duration: "60s",
  thresholds: {
    http_req_failed: ["rate<0.20"],
    http_req_duration: ["p(95)<3000"],
  },
};

export default function () {
  const res = http.get("http://localhost:3000/api/health");

  check(res, {
    "health endpoint responds": (r) => r.status === 200,
  });

  sleep(1);
}
