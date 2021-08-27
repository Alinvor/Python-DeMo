#!/usr/bin/env bash

### THE DELETE FILES
find . -type f -name '*.pyc' -delete

### THE DELETE DIRECTORY
## .tox/*
find .tox -path "*" ! -name ".tox" -delete
## ./build/*
find ./build -path "*" ! -name "build" -delete
## ./src/com.dvsnier.*.egg-info
find ./src -path "*com.dvsnier*" -delete
# find ./src -path "*com.dvsnier.*" -type d -exec rm -r {} +
# find ./src -path "*com.dvsnier.*" -type f -delete
## ./dist/*
find ./dist -path "*" ! -name "dist" -delete
## ./out/log/*
find ./out/log -path "*" ! -name "log" -delete
## __pycache__
find . -type d -name __pycache__ -exec rm -r {} +
