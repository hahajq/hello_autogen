#!/bin/bash
cd "$(
    cd "$(dirname "$0")" >/dev/null 2>&1
    pwd -P
)/" || exit
set -e

litellm --model ollama_chat/llama3 --config litellm.yaml
