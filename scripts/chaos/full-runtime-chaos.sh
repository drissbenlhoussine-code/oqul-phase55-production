#!/usr/bin/env sh
set -e

echo "[chaos] redis outage simulation"
docker stop oqul-runtime-redis || true

sleep 5

echo "[chaos] redis recovery"
docker start oqul-runtime-redis || true

sleep 5

echo "[chaos] worker termination"
docker kill oqul-runtime-worker-a || true

sleep 3

echo "[chaos] worker restart"
docker start oqul-runtime-worker-a || true

echo "[chaos] runtime chaos cycle completed"
