const DEFAULT_URL = "https://www.oqul.tech/api/auth/forgot-password";

function parseArgs(argv) {
  const args = new Map();

  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (!arg.startsWith("--")) continue;

    const keyValue = arg.slice(2);
    const equalsIndex = keyValue.indexOf("=");

    if (equalsIndex >= 0) {
      args.set(keyValue.slice(0, equalsIndex), keyValue.slice(equalsIndex + 1));
      continue;
    }

    const next = argv[index + 1];
    if (next && !next.startsWith("--")) {
      args.set(keyValue, next);
      index += 1;
      continue;
    }

    args.set(keyValue, "true");
  }

  return args;
}

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const url = args.get("url") ?? DEFAULT_URL;
  const email = args.get("email") ?? `forgot-password-production-check-${Date.now()}@example.com`;

  console.log(`POST ${url}`);
  console.log(`Email: ${email}`);

  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json",
    },
    body: JSON.stringify({ email }),
    redirect: "manual",
  });

  const contentType = response.headers.get("content-type") ?? "";
  const body = await response.text();

  assert(response.status === 200, `Expected status 200, got ${response.status}`);
  assert(contentType.includes("application/json"), `Expected application/json content-type, got ${contentType || "(missing)"}`);
  assert(body.length > 0, "Expected non-empty response body");

  let json;
  try {
    json = JSON.parse(body);
  } catch (error) {
    throw new Error(`Expected valid JSON body: ${error instanceof Error ? error.message : "parse failed"}`);
  }

  assert(json && typeof json === "object", "Expected JSON object response");
  assert(json.success === true, `Expected success true, got ${JSON.stringify(json)}`);
  assert(json.code === "RESET_EMAIL_REQUEST_ACCEPTED", `Expected RESET_EMAIL_REQUEST_ACCEPTED, got ${json.code ?? "(missing)"}`);

  console.log(JSON.stringify({
    success: true,
    status: response.status,
    contentType,
    bodyLength: body.length,
    responseBody: json,
  }, null, 2));
}

main().catch((error) => {
  console.error(JSON.stringify({
    success: false,
    message: error instanceof Error ? error.message : "Production forgot-password test failed",
  }, null, 2));
  process.exit(1);
});
