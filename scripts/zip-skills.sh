#!/bin/sh
# One .zip per skill for claude.ai (Settings > Capabilities > Skills > Upload). Run from the repo root.
set -e
rm -rf dist && mkdir dist
cd skills
for d in */; do n=${d%/}; zip -qr "../dist/$n.zip" "$n"; done
echo "$(ls ../dist | wc -l) zips in dist/"
