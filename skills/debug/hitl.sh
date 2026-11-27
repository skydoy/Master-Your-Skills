#!/usr/bin/env bash
# Human-in-the-loop repro. Copy, edit the steps between the markers, run it.
# ask = show an instruction, wait for Enter. note VAR "q" = record an answer.
# Never note a password: let the user sign in with an `ask` step.
set -euo pipefail
out=()
ask()  { printf '\n>>> %s\n' "$1"; read -r -p '    [Enter when done] ' _; }
note() { printf '\n>>> %s\n' "$2"; read -r -p '    > ' a; out+=("$1=$a"); }

# --- edit below -----------------------------------------------------------
ask  "Open http://localhost:3000 and sign in."
note FAILED "Click 'Export'. Did it fail? (y/n)"
note ERROR  "Paste the error text, or 'none':"
# --- edit above -----------------------------------------------------------

printf '\n--- result ---\n'; printf '%s\n' "${out[@]}"
