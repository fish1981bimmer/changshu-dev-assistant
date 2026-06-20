#!/bin/bash
# 昌叔专属软件开发助手 - 安装脚本

set -e

echo "=========================================="
echo "  昌叔专属软件开发助手 - 安装向导"
echo "=========================================="
echo ""

# 检查Python版本
echo "检查Python版本..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    echo "✓ 找到Python $PYTHON_VERSION"
else
    echo "✗ 未找到Python3，请先安装Python 3.8或更高版本"
    exit 1
fi

# 检查pip
echo "检查pip..."
if command -v pip3 &> /dev/null; then
    echo "✓ 找到pip3"
else
    echo "✗ 未找到pip3"
    exit 1
fi

# 进入skill目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"
echo "✓ 工作目录: $SCRIPT_DIR"

# 安装依赖
echo ""
echo "安装Python依赖..."
pip3 install pyyaml requests psutil 2>/dev/null || {
    echo "⚠ 部分依赖安装失败，尝试使用用户安装..."
    pip3 install --user pyyaml requests psutil
}

# 复制配置文件
echo ""
echo "配置助手..."
if [ ! -f "config.yaml" ]; then
    cp templates/config.example.yaml config.yaml
    echo "✓ 已创建配置文件: config.yaml"
    echo "  请根据需要编辑 config.yaml"
else
    echo "✓ 配置文件已存在: config.yaml"
fi

# 设置脚本权限
echo ""
echo "设置脚本权限..."
chmod +x scripts/changshu-assistant.py
chmod +x scripts/dameng-tool.py
echo "✓ 脚本权限已设置"

# 测试运行
echo ""
echo "测试运行..."
if python3 scripts/changshu-assistant.py status &> /dev/null; then
    echo "✓ 助手运行正常"
else
    echo "✗ 助手运行测试失败"
    exit 1
fi

# 创建快捷命令（可选）
echo ""
echo "创建快捷命令..."
if [ -d "$HOME/.local/bin" ]; then
    BIN_DIR="$HOME/.local/bin"
elif [ -d "/usr/local/bin" ]; then
    BIN_DIR="/usr/local/bin"
else
    BIN_DIR="$HOME/bin"
    mkdir -p "$BIN_DIR"
fi

# 创建启动脚本
cat > "$BIN_DIR/changshu-assistant" << 'EOF'
#!/bin/bash
cd ~/.hermes/skills/devops/changshu-dev-assistant
python3 scripts/changshu-assistant.py "$@"
EOF

chmod +x "$BIN_DIR/changshu-assistant"
echo "✓ 快捷命令已创建: $BIN_DIR/changshu-assistant"

# 检查PATH
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    echo ""
    echo "⚠ 请将以下目录添加到你的PATH环境变量中:"
    echo "   export PATH=\"$BIN_DIR:\$PATH\""
    echo ""
    echo "   可以添加到 ~/.bashrc 或 ~/.zshrc 中"
fi

# 完成
echo ""
echo "=========================================="
echo "  安装完成！"
echo "=========================================="
echo ""
echo "快速开始:"
echo "  1. 查看帮助: changshu-assistant help"
echo "  2. 查看状态: changshu-assistant status"
echo "  3. 直接提问: changshu-assistant ask \"你的问题\""
echo ""
echo "或者直接运行:"
echo "  python3 scripts/changshu-assistant.py help"
echo ""
echo "昌叔，准备开始使用吧！🚀"
echo ""
