#!/usr/bin/env sh
set -e

echo "[phase20.5] verifying failover write path before partition"
npm run test:failover-write

echo "[phase20.5] applying partition"
npm run partition:redis || true

echo "[phase20.5] verifying partition correctness policies"
npm run test:partition-correctness

echo "[phase20.5] verifying replay and ordering after partition cycle"
npm run test:replay-real
npm run test:ordering-real

echo "[phase20.5] partition correctness cycle completed"
