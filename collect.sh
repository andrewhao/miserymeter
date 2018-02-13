#!/usr/bin/env bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
RECORDING_FILE="${DIR}/recordings/sample.wav"
arecord --device=hw:1,0 --format S16_LE --rate 48000 -c1 -d 5 --quiet "${RECORDING_FILE}"
sox -V3 ${RECORDING_FILE} -n stats 2>&1 | grep dB
