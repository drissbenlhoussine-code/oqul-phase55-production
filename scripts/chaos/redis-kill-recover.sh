#!/usr/bin/env sh
set -e

echo "[chaos] stopping redis..."
docker stop oqul-runtime-redis || true

sleep 5

echo "[chaos] starting redis..."
docker start oqul-runtime-redis || true

echo "[chaos] redis recovery triggered"
