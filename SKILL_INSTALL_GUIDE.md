# Skill安装指南

## 概念说明

**昌叔助手本身就是一个Hermes skill**，位于：
```
~/.hermes/skills/devops/changshu-dev-assistant
```

昌叔助手通过调用Hermes的其他skill来扩展功能，而不是自己管理skill目录。

## 安装Hermes Skill

### 方法1：从Skills Hub安装（推荐）

```bash
# 搜索skill
hermes skills search <关键词>

# 安装skill
hermes skills install <skill-identifier>

# 示例：安装一个skill
hermes skills install skills-sh/github/github-code-review
```

### 方法2：从GitHub安装

```bash
# 从GitHub仓库安装
hermes skills install github:<username>/<repo>

# 示例
hermes skills install github:fish1981bimmer/skill-orchestration-core
```

### 方法3：手动安装

```bash
# 1. 克隆skill到本地目录
cd ~/.hermes/skills/<category>/
git clone <skill-repo> <skill-name>

# 2. 确保skill目录包含SKILL.md文件
cd <skill-name>
ls SKILL.md

# 3. 重新扫描skill
hermes skills audit
```

## 查看已安装的Skills

```bash
# 列出所有已安装的skills
hermes skills list

# 查看特定skill的详情
hermes skills inspect <skill-name>

# 检查skill更新
hermes skills check
```

## 在昌叔助手中使用Skill

安装skill后，就可以在昌叔助手中使用了：

### 命令行模式

```bash
cd ~/.hermes/skills/devops/changshu-dev-assistant

# 查看skill详情
./start.sh skill <skill-name>

# 运行skill
./start.sh run <skill-name> "你的问题"
```

### 交互模式

```bash
cd ~/.hermes/skills/devops/changshu-dev-assistant
./start.sh chat

# 在chat中：
> skill <skill-name>              # 查看skill详情
> run <skill-name> "你的问题"     # 运行skill
```

## 示例

### 示例1：安装并使用达梦数据库skill

```bash
# 1. 搜索达梦相关的skill
hermes skills search dameng

# 2. 假设找到了 dameng-stored-procedure-review
# 3. 查看skill详情（已内置）
./start.sh skill dameng-stored-procedure-review

# 4. 运行skill
./start.sh run dameng-stored-procedure-review "帮我审查这个存储过程"
```

### 示例2：安装GitHub相关skill

```bash
# 1. 搜索GitHub相关的skill
hermes skills search github

# 2. 安装一个skill
hermes skills install skills-sh/github/github-code-review

# 3. 在昌叔助手中使用
./start.sh run github-code-review "审查这个PR"
```

## Skill目录结构

Hermes的skill目录结构：

```
~/.hermes/skills/
├── apple/                    # Apple相关skills
├── autonomous-ai-agents/    # AI代理相关skills
├── creative/                 # 创意相关skills
├── database/                # 数据库相关skills
├── devops/                   # DevOps相关skills
│   └── changshu-dev-assistant/  # 昌叔助手（就是这个）
├── github/                   # GitHub相关skills
├── mlops/                    # MLOps相关skills
└── ...
```

## 常见问题

### Q: 昌叔助手有自己的skill目录吗？

A: 没有。昌叔助手本身就是一个Hermes skill，它通过调用Hermes的其他skill来扩展功能。

### Q: 如何为昌叔助手添加新功能？

A: 有两种方式：
1. 安装现有的Hermes skill，然后通过`run`命令调用
2. 修改昌叔助手的代码，添加新的功能模块

### Q: 安装的skill在哪里？

A: 安装的skill会放在`~/.hermes/skills/`目录下的对应分类中。

### Q: 如何卸载skill？

A: 使用以下命令：
```bash
hermes skills uninstall <skill-identifier>
```

### Q: 如何更新skill？

A: 使用以下命令：
```bash
hermes skills update <skill-identifier>
```

## 推荐Skills

根据昌叔的工作需求，推荐以下skills：

### 数据库相关
- `dameng-stored-procedure-review` - 达梦存储过程审查（已内置）

### 开发相关
- `github-code-review` - GitHub代码审查
- `test-driven-development` - 测试驱动开发
- `systematic-debugging` - 系统化调试

### DevOps相关
- `ssh-ops-optimization` - SSH运维优化
- `config-hot-reload` - 配置热重载

### 协同相关
- `openclaw-collab` - OpenClaw协同
- `hermes-skill-publishing` - Skill发布

## 技术细节

### Skill调用原理

昌叔助手通过以下方式调用skill：

```python
# 实际执行的是：
hermes chat -s <skill-name> -q "<query>"

# 参数说明：
# -s: 预加载skill
# -q: 查询内容
```

### Skill查找顺序

1. 首先在本地`~/.hermes/skills/`目录查找
2. 如果本地找不到，尝试从远程查找
3. 直接读取SKILL.md文件

## 总结

- 昌叔助手本身就是一个Hermes skill
- 通过`hermes skills install`安装其他skill
- 通过`run`命令在昌叔助手中调用这些skill
- 所有skill都存储在`~/.hermes/skills/`目录中
