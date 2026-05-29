#!/usr/bin/env sh
set -e

NETWORK_NAME=${NETWORK_NAME:-oqul_phase19_work_default}
TARGET=${TARGET:-oqul-redis-replica}

echo "[partition] disconnecting $TARGET from $NETWORK_NAME"
docker network disconnect "$NETWORK_NAME" "$TARGET" || true

sleep ${PARTITION_SECONDS:-10}

echo "[partition] reconnecting $TARGET to $NETWORK_NAME"
docker network connect "$NETWORK_NAME" "$TARGET" || true

echo "[partition] partition cycle completed"
