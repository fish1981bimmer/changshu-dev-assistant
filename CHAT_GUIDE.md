# 昌叔助手 - Chat 功能使用说明

## 🎉 Chat 功能已完善！

现在 `csa chat` 命令已经可以正常使用了！

## 🚀 使用方法

### 方式1：使用启动脚本（推荐）

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant

# 启动交互式对话
./start.sh chat
```

### 方式2：使用快捷命令

```bash
# 先使快捷命令生效
source ~/.bashrc  # 或 source ~/.zshrc

# 启动交互式对话
csa chat
```

### 方式3：使用完整路径

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant

python3 scripts/changshu-assistant.py chat
```

## 💬 交互式对话功能

启动后，你可以：

### 1. 提问
```
昌叔助手 > 如何优化达梦数据库查询？
```

### 2. 查看状态
```
昌叔助手 > status
```

### 3. 系统诊断
```
昌叔助手 > diagnose
```

### 4. 查看帮助
```
昌叔助手 > help
```

### 5. 退出
```
昌叔助手 > quit
# 或
昌叔助手 > exit
# 或
昌叔助手 > q
```

## 🎯 实际使用示例

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant

# 启动对话
./start.sh chat

# 然后你可以：
# - 提问：如何优化SQL查询？
# - 查看状态：status
# - 系统诊断：diagnose
# - 查看帮助：help
# - 退出：quit
```

## 💡 使用技巧

1. **连续对话**：可以连续提问，不需要重新启动
2. **快捷命令**：在对话中可以直接使用 status、diagnose 等命令
3. **优雅退出**：使用 quit、exit 或 q 退出，或者按 Ctrl+C

## 📝 可用命令

在 chat 模式中，你可以使用：

| 命令 | 说明 |
|------|------|
| `help` | 显示帮助信息 |
| `status` | 查看助手状态 |
| `diagnose` | 系统诊断 |
| `quit/exit/q` | 退出对话 |
| 其他输入 | 提问 |

## 🎉 现在试试吧！

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant
./start.sh chat
```

有问题随时问我！
