import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  vus: 60,
  duration: "90s",
};

export default function () {
  const payload = JSON.stringify({
    message: "اختبار ضغط تشغيلي على runtime",
  });

  const res = http.post("http://localhost:3000/api/ai/leila", payload, {
    headers: { "Content-Type": "application/json" },
  });

  check(res, {
    "AI endpoint handled request": (r) => r.status < 500,
  });

  sleep(0.5);
}
