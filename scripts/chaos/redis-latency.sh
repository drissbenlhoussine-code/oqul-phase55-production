#!/usr/bin/env sh
set -e

echo "Latency injection requires Linux tc/netem privileges."
echo "Recommended command:"
echo "tc qdisc add dev lo root netem delay 200ms 50ms distribution normal"
