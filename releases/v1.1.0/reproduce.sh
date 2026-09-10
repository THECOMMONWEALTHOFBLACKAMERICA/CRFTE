#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
if [[ "${1:-}" == "--verify-reference" ]]; then
  exec python "$ROOT/code/verify_reproduction.py" --reference-only
fi
if [[ "${CRTFE_SKIP_INSTALL:-0}" != "1" ]]; then
  python -m venv "$ROOT/.venv"
  "$ROOT/.venv/bin/python" -m pip install --upgrade pip
  "$ROOT/.venv/bin/python" -m pip install -r "$ROOT/environment/requirements-lock.txt"
  PY="$ROOT/.venv/bin/python"
else
  PY="python"
fi
"$PY" "$ROOT/code/reproduce_transferability.py" --output "$ROOT/reproduced" --workers "${CRTFE_WORKERS:-4}"
"$PY" "$ROOT/code/verify_reproduction.py" --actual "$ROOT/reproduced"
