#!/bin/bash

# 昌叔专属软件开发助手 - 一键安装脚本
# 作者: Hermes Agent
# 创建时间: 2026-04-26

set -e  # 遇到错误立即退出

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 打印带颜色的消息
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

print_header() {
    echo ""
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}"
    echo ""
}

# 检查命令是否存在
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# 主安装函数
main() {
    print_header "昌叔专属软件开发助手 - 一键安装"
    
    # 获取脚本所在目录
    SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    cd "$SCRIPT_DIR"
    
    print_info "安装目录: $SCRIPT_DIR"
    
    # 步骤1: 检查Python环境
    print_header "步骤 1/5: 检查Python环境"
    
    if command_exists python3; then
        PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
        print_success "Python3已安装: $PYTHON_VERSION"
    else
        print_error "未找到Python3，请先安装Python3"
        print_info "macOS: brew install python3"
        exit 1
    fi
    
    # 步骤2: 安装Python依赖
    print_header "步骤 2/5: 安装Python依赖"
    
    print_info "正在安装依赖包..."
    
    if command_exists pip3; then
        pip3 install pyyaml requests psutil -q
        print_success "依赖包安装完成"
    elif command_exists pip; then
        pip install pyyaml requests psutil -q
        print_success "依赖包安装完成"
    else
        print_warning "未找到pip，尝试使用python3 -m pip"
        python3 -m pip install pyyaml requests psutil -q
        print_success "依赖包安装完成"
    fi
    
    # 步骤3: 创建配置文件
    print_header "步骤 3/5: 创建配置文件"
    
    if [ -f "config.yaml" ]; then
        print_warning "配置文件已存在，跳过创建"
    else
        if [ -f "templates/config.example.yaml" ]; then
            cp templates/config.example.yaml config.yaml
            print_success "配置文件创建完成"
        else
            print_error "配置模板文件不存在"
            exit 1
        fi
    fi
    
    # 步骤4: 测试安装
    print_header "步骤 4/5: 测试安装"
    
    print_info "测试助手命令..."
    if python3 scripts/changshu-assistant.py help > /dev/null 2>&1; then
        print_success "助手命令测试通过"
    else
        print_error "助手命令测试失败"
        exit 1
    fi
    
    print_info "测试达梦数据库工具..."
    if python3 scripts/dameng-tool.py --help > /dev/null 2>&1; then
        print_success "达梦数据库工具测试通过"
    else
        print_error "达梦数据库工具测试失败"
        exit 1
    fi
    
    # 步骤5: 创建快捷命令
    print_header "步骤 5/5: 创建快捷命令"
    
    # 检测shell类型
    if [ -n "$ZSH_VERSION" ]; then
        SHELL_CONFIG="$HOME/.zshrc"
        print_info "检测到zsh shell"
    elif [ -n "$BASH_VERSION" ]; then
        SHELL_CONFIG="$HOME/.bashrc"
        print_info "检测到bash shell"
    else
        SHELL_CONFIG="$HOME/.profile"
        print_info "使用默认配置文件"
    fi
    
    # 检查是否已经添加过快捷命令
    if grep -q "昌叔助手快捷命令" "$SHELL_CONFIG" 2>/dev/null; then
        print_warning "快捷命令已存在，跳过添加"
    else
        # 添加快捷命令
        cat >> "$SHELL_CONFIG" << 'EOF'

# 昌叔助手快捷命令
alias csa='python3 /Users/a1234/.hermes/skills/devops/changshu-dev-assistant/scripts/changshu-assistant.py'
alias dmt='python3 /Users/a1234/.hermes/skills/devops/changshu-dev-assistant/scripts/dameng-tool.py'
EOF
        print_success "快捷命令已添加到 $SHELL_CONFIG"
        print_warning "请运行以下命令使快捷命令生效:"
        echo "  source $SHELL_CONFIG"
    fi
    
    # 安装完成
    print_header "安装完成！"
    
    echo ""
    print_success "昌叔助手安装成功！"
    echo ""
    echo "快速开始:"
    echo "  1. 使快捷命令生效: source $SHELL_CONFIG"
    echo "  2. 查看帮助: csa help"
    echo "  3. 查看状态: csa status"
    echo "  4. 分析SQL: dmt analyze <sql文件>"
    echo ""
    echo "或者直接使用完整路径:"
    echo "  python3 scripts/changshu-assistant.py help"
    echo "  python3 scripts/dameng-tool.py analyze <sql文件>"
    echo ""
    print_info "详细文档: cat README.md"
    echo ""
}

# 运行主函数
main
