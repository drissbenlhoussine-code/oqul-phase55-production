#!/usr/bin/env sh
set -e

echo "[chaos] stopping Redis master..."
docker stop oqul-redis-master || true

echo "[chaos] waiting for Sentinel promotion window..."
sleep 8

echo "[chaos] restarting Redis master..."
docker start oqul-redis-master || true

echo "[chaos] Redis master kill/restart cycle completed"
