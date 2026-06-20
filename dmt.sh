#!/bin/bash

# 达梦数据库工具启动脚本
# 使用方法: ./dmt.sh [命令] [参数]

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

python3 scripts/dameng-tool.py "$@"
