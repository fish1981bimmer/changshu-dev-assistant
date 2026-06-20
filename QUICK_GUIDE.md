# 昌叔助手 - 超简单使用指南

## 🚀 一键安装（推荐）

只需要一个命令！

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant
./quick_install.sh
```

安装完成后，运行：
```bash
source ~/.zshrc  # 或者 source ~/.bashrc
```

## 📝 三种使用方式

### 方式1：使用快捷命令（最简单）

安装完成后，直接使用：

```bash
# 查看帮助
csa help

# 查看状态
csa status

# 分析SQL
dmt analyze /tmp/my_query.sql

# 生成存储过程
dmt procedure user_sync
```

### 方式2：使用完整路径

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant

# 查看帮助
python3 scripts/changshu-assistant.py help

# 分析SQL
python3 scripts/dameng-tool.py analyze /tmp/my_query.sql
```

### 方式3：在当前目录使用

```bash
# 进入助手目录
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant

# 使用相对路径
python3 scripts/changshu-assistant.py help
python3 scripts/dameng-tool.py analyze /tmp/my_query.sql
```

## 🎯 常用命令速查

| 功能 | 快捷命令 | 完整命令 |
|------|---------|---------|
| 查看帮助 | `csa help` | `python3 scripts/changshu-assistant.py help` |
| 查看状态 | `csa status` | `python3 scripts/changshu-assistant.py status` |
| 系统诊断 | `csa diagnose` | `python3 scripts/changshu-assistant.py diagnose` |
| 分析SQL | `dmt analyze 文件` | `python3 scripts/dameng-tool.py analyze 文件` |
| 优化SQL | `dmt optimize 文件` | `python3 scripts/dameng-tool.py optimize 文件` |
| 存储过程 | `dmt procedure 名字` | `python3 scripts/dameng-tool.py procedure 名字` |
| 函数模板 | `dmt function 名字` | `python3 scripts/dameng-tool.py function 名字` |
| 触发器模板 | `dmt trigger 名字 表名` | `python3 scripts/dameng-tool.py trigger 名字 表名` |

## 💡 实际使用示例

### 示例1：分析达梦SQL

```bash
# 创建测试SQL文件
cat > /tmp/test.sql << 'EOF'
SELECT user_name + ' - ' + dept_name
FROM users u
JOIN departments d ON u.dept_id = d.id;
EOF

# 分析SQL
dmt analyze /tmp/test.sql
```

### 示例2：生成存储过程

```bash
# 生成存储过程模板
dmt procedure user_data_sync
```

### 示例3：日常使用

```bash
# 查看助手状态
csa status

# 系统诊断
csa diagnose
```

## 🔧 如果遇到问题

### 问题1：快捷命令不生效

```bash
# 重新加载配置
source ~/.zshrc  # 或 source ~/.bashrc

# 或者重新打开终端
```

### 问题2：找不到python3

```bash
# 查找python3
which python3

# 如果没有，安装python3
brew install python3
```

### 问题3：权限问题

```bash
# 给安装脚本添加执行权限
chmod +x quick_install.sh

# 重新运行
./quick_install.sh
```

## 📚 更多帮助

```bash
# 查看完整帮助
csa help

# 查看达梦工具帮助
dmt --help

# 查看README文档
cat README.md
```

## 🎉 开始使用

安装完成后，试试这些命令：

```bash
# 1. 查看状态
csa status

# 2. 分析一个SQL文件
dmt analyze /tmp/test.sql

# 3. 生成一个存储过程模板
dmt procedure my_procedure
```

就这么简单！
