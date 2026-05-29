let degradedMode = false;

export function enableDegradedMode() {
  degradedMode = true;
}

export function disableDegradedMode() {
  degradedMode = false;
}

export function isDegradedMode() {
  return degradedMode;
}
