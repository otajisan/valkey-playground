#!/bin/bash

POETRY_BIN=.venv/bin/poetry

if [ ! -f $POETRY_BIN ]; then
    echo "Installing poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
fi

$POETRY_BIN run python -m valkey_playground_python