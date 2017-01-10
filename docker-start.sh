#!/bin/sh

set -eu

if [ "${1-}" = "test" ]; then
  py.test tests
else
  python -m lserver
fi