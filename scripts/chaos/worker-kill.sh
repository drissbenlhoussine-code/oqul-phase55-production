#!/usr/bin/env sh
set -e

echo "[chaos] killing worker A..."
docker kill oqul-runtime-worker-a || true

sleep 3

echo "[chaos] restarting worker A..."
docker start oqul-runtime-worker-a || true

echo "[chaos] worker recovery triggered"
