#!/usr/bin/env sh
set -e

echo "[phase20] Running failover write test before partition"
npm run test:failover-write

echo "[phase20] Applying Redis network partition"
npm run partition:redis || true

echo "[phase20] Running consistency and replay tests after partition cycle"
npm run test:consistency-real
npm run test:replay-real

echo "[phase20] Partition consistency assertion cycle completed"
