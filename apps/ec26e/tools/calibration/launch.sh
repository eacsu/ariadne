#!/usr/bin/env bash
set -euo pipefail
exec "${EC_PYTHON:-python3}" -m ec_26_e.calibration_console "$@"
