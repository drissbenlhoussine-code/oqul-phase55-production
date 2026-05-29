#!/usr/bin/env sh
set -e

echo "Stopping Redis container..."
docker stop oqul-phase15-redis || true
sleep 5

echo "Starting Redis container..."
docker start oqul-phase15-redis || true
