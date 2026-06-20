#!/bin/bash

# Skill安装示例脚本
# 演示如何为昌叔助手安装和使用Hermes skill

echo "=========================================="
echo "  昌叔助手 - Skill安装示例"
echo "=========================================="
echo ""

# 1. 搜索skill
echo "1. 搜索skill示例："
echo "   命令: hermes skills search github"
echo ""
hermes skills search github 2>&1 | head -15
echo ""

# 2. 查看已安装的skills
echo "2. 查看已安装的skills："
echo "   命令: hermes skills list"
echo ""
hermes skills list 2>&1 | head -20
echo ""

# 3. 查看特定skill详情
echo "3. 查看skill详情示例："
echo "   命令: hermes skills inspect claude-code"
echo ""
hermes skills inspect claude-code 2>&1 | head -30
echo ""

# 4. 在昌叔助手中使用skill
echo "4. 在昌叔助手中使用skill示例："
echo ""
echo "   方式1：命令行模式"
echo "   命令: ./start.sh skill claude-code"
echo ""
echo "   方式2：交互模式"
echo "   命令: ./start.sh chat"
echo "   然后输入: skill claude-code"
echo ""

# 5. 安装新skill示例（注释掉，避免实际安装）
echo "5. 安装新skill示例（需要时取消注释）："
echo "   # 搜索skill"
echo "   hermes skills search <关键词>"
echo ""
echo "   # 安装skill"
echo "   hermes skills install <skill-identifier>"
echo ""
echo "   # 示例："
echo "   # hermes skills install skills-sh/github/github-code-review"
echo ""

echo "=========================================="
echo "  更多信息请参考: SKILL_INSTALL_GUIDE.md"
echo "=========================================="
