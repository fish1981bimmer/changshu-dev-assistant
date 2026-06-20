# 昌叔助手 - 超简单使用指南

## 🚀 一键安装

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant
./quick_install.sh
```

就这么简单！安装脚本会自动完成所有配置。

## 🔧 配置大模型（可选）

要启用大模型功能，需要配置API密钥：

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant

# 编辑配置文件
vi config.yaml
```

在 `ai` 部分添加你的API密钥：

```yaml
ai:
  provider: "openai"
  api_key: "你的API密钥"
  model_name: "gpt-3.5-turbo"
```

详细配置说明请查看 `LLM_CONFIG_GUIDE.md`

## 📝 三种使用方式（任选一种）

### 方式1：使用启动脚本（最简单）

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant

# 查看帮助
./start.sh help

# 查看状态
./start.sh status

# 分析SQL
./dmt.sh analyze /tmp/test.sql

# 生成存储过程
./dmt.sh procedure user_sync
```

### 方式2：使用快捷命令

```bash
# 先使快捷命令生效
source ~/.bashrc  # 或 source ~/.zshrc

# 然后使用
csa help
csa status
dmt analyze /tmp/test.sql
dmt procedure user_sync
```

### 方式3：使用完整路径

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant

python3 scripts/changshu-assistant.py help
python3 scripts/dameng-tool.py analyze /tmp/test.sql
```

## 🎯 常用命令速查表

| 功能 | 启动脚本 | 快捷命令 |
|------|---------|---------|
| 查看帮助 | `./start.sh help` | `csa help` |
| 查看状态 | `./start.sh status` | `csa status` |
| 系统诊断 | `./start.sh diagnose` | `csa diagnose` |
| **交互对话** | `./start.sh chat` | `csa chat` |
| 分析SQL | `./dmt.sh analyze 文件` | `dmt analyze 文件` |
| 优化SQL | `./dmt.sh optimize 文件` | `dmt optimize 文件` |
| 存储过程 | `./dmt.sh procedure 名字` | `dmt procedure 名字` |
| 函数模板 | `./dmt.sh function 名字` | `dmt function 名字` |
| 触发器模板 | `./dmt.sh trigger 名字 表名` | `dmt trigger 名字 表名` |

## 💡 实际使用示例

### 示例1：分析达梦SQL

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant

# 创建测试SQL
cat > /tmp/test.sql << 'EOF'
SELECT user_name + ' - ' + dept_name
FROM users u
JOIN departments d ON u.dept_id = d.id;
EOF

# 分析SQL
./dmt.sh analyze /tmp/test.sql
```

### 示例2：生成存储过程

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant

# 生成存储过程模板
./dmt.sh procedure user_data_sync
```

### 示例3：日常使用

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant

# 查看助手状态
./start.sh status

# 系统诊断
./start.sh diagnose
```

### 示例4：交互式对话（新功能！）

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant

# 启动交互式对话
./start.sh chat

# 然后你可以：
# - 提问：如何优化达梦数据库查询？
# - 查看状态：status
# - 系统诊断：diagnose
# - 查看帮助：help
# - 退出：quit
```

## 🔧 快速开始

安装完成后，试试这些命令：

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant

# 1. 查看帮助
./start.sh help

# 2. 查看状态
./start.sh status

# 3. 启动交互式对话（新功能！）
./start.sh chat

# 4. 分析一个SQL文件
./dmt.sh analyze /tmp/test.sql

# 5. 生成一个存储过程模板
./dmt.sh procedure my_procedure
```

## 📚 更多帮助

```bash
# 查看完整帮助
./start.sh help

# 查看达梦工具帮助
./dmt.sh --help

# 查看README文档
cat README.md

# 查看快速指南
cat QUICK_GUIDE.md
```

## 🎉 推荐工作流程

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant

# 早上开始工作
./start.sh status

# 启动交互式对话，连续提问
./start.sh chat

# 写了SQL，检查问题
./dmt.sh analyze /path/to/query.sql

# 需要写存储过程
./dmt.sh procedure procedure_name

# 写完代码，审查一下
./start.sh review --file /path/to/code.py
```

## 💡 提示

1. **推荐使用启动脚本**：`./start.sh` 和 `./dmt.sh` 最简单
2. **记住目录**：所有命令都要在助手目录下运行
3. **查看帮助**：忘记命令时，运行 `./start.sh help`

就这么简单！有问题随时问我。
