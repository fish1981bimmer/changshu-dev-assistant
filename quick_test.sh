#!/bin/bash

# 昌叔助手 - 快速测试脚本
# 用于验证一键安装是否成功

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}昌叔助手 - 快速测试${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# 测试1：检查Python环境
echo -e "${YELLOW}[1/5] 检查Python环境...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓ Python已安装: $PYTHON_VERSION${NC}"
else
    echo -e "${RED}✗ Python未安装${NC}"
    exit 1
fi

# 测试2：检查依赖
echo -e "${YELLOW}[2/5] 检查依赖...${NC}"
python3 -c "import yaml, requests, psutil" 2>/dev/null
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ 所有依赖已安装${NC}"
else
    echo -e "${RED}✗ 依赖缺失${NC}"
    exit 1
fi

# 测试3：检查配置文件
echo -e "${YELLOW}[3/5] 检查配置文件...${NC}"
if [ -f "config.yaml" ]; then
    echo -e "${GREEN}✓ 配置文件存在${NC}"
else
    echo -e "${YELLOW}⚠ 配置文件不存在，将使用默认配置${NC}"
fi

# 测试4：测试主程序
echo -e "${YELLOW}[4/5] 测试主程序...${NC}"
if [ -f "start.sh" ]; then
    OUTPUT=$(./start.sh status 2>&1)
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ 主程序运行正常${NC}"
    else
        echo -e "${RED}✗ 主程序运行失败${NC}"
        echo "$OUTPUT"
        exit 1
    fi
else
    echo -e "${RED}✗ start.sh不存在${NC}"
    exit 1
fi

# 测试5：测试达梦工具
echo -e "${YELLOW}[5/5] 测试达梦工具...${NC}"
if [ -f "dmt.sh" ]; then
    OUTPUT=$(./dmt.sh --help 2>&1)
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ 达梦工具运行正常${NC}"
    else
        echo -e "${RED}✗ 达梦工具运行失败${NC}"
        echo "$OUTPUT"
        exit 1
    fi
else
    echo -e "${RED}✗ dmt.sh不存在${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}✓ 所有测试通过！${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "${BLUE}快速开始：${NC}"
echo -e "  查看帮助: ${GREEN}./start.sh help${NC}"
echo -e "  查看状态: ${GREEN}./start.sh status${NC}"
echo -e "  分析SQL:  ${GREEN}./dmt.sh analyze <文件>${NC}"
echo ""
