#!/bin/bash

# 昌叔助手启动脚本
# 使用方法: ./start.sh [命令]

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# 如果没有参数，显示帮助
if [ $# -eq 0 ]; then
    python3 scripts/changshu-assistant.py help
else
    python3 scripts/changshu-assistant.py "$@"
fi
