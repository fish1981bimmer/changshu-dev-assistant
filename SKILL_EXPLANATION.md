# 关于Skill安装的说明

## 重要概念

**昌叔助手本身就是一个Hermes skill**，它位于：
```
~/.hermes/skills/devops/changshu-dev-assistant
```

## 目录结构说明

### Hermes的skill目录
```
~/.hermes/skills/
├── apple/                    # Apple相关skills
├── autonomous-ai-agents/    # AI代理相关skills
├── creative/                 # 创意相关skills
├── database/                # 数据库相关skills
│   └── dameng-stored-procedure-review/
├── devops/                   # DevOps相关skills
│   ├── changshu-dev-assistant/  # 昌叔助手（就是这个）
│   ├── clawhub-publish/
│   ├── skill-orchestration-core/
│   └── ...
├── github/                   # GitHub相关skills
├── mlops/                    # MLOps相关skills
└── ...
```

### 昌叔助手的目录
```
~/.hermes/skills/devops/changshu-dev-assistant/
├── scripts/                  # 脚本文件
│   ├── changshu-assistant.py
│   └── dameng-tool.py
├── templates/                # 模板文件
├── config.yaml              # 配置文件
├── start.sh                 # 启动脚本
├── README.md                # 说明文档
└── SKILL.md                 # Skill定义
```

## 如何安装Skill

### 方法1：从Skills Hub安装（推荐）

```bash
# 搜索skill
hermes skills search <关键词>

# 安装skill
hermes skills install <skill-identifier>

# 示例
hermes skills search github
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
# 1. 进入目标分类目录
cd ~/.hermes/skills/<category>/

# 2. 克隆skill
git clone <skill-repo> <skill-name>

# 3. 确保有SKILL.md
cd <skill-name>
ls SKILL.md

# 4. 重新扫描
hermes skills audit
```

## 如何在昌叔助手中使用Skill

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

## 实际例子

### 例子1：使用达梦数据库skill

```bash
# 1. 查看skill详情
cd ~/.hermes/skills/devops/changshu-dev-assistant
./start.sh skill dameng-stored-procedure-review

# 2. 运行skill
./start.sh run dameng-stored-procedure-review "帮我审查这个存储过程"
```

### 例子2：使用Claude Code skill

```bash
# 1. 查看skill详情
cd ~/.hermes/skills/devops/changshu-dev-assistant
./start.sh skill claude-code

# 2. 运行skill
./start.sh run claude-code "帮我审查这段代码"
```

## 常用命令

```bash
# 搜索skill
hermes skills search <关键词>

# 列出已安装的skills
hermes skills list

# 查看skill详情
hermes skills inspect <skill-name>

# 安装skill
hermes skills install <skill-identifier>

# 卸载skill
hermes skills uninstall <skill-identifier>

# 更新skill
hermes skills update <skill-identifier>

# 检查更新
hermes skills check

# 重新扫描本地skills
hermes skills audit
```

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

## 常见问题

### Q: 昌叔助手有自己的skill目录吗？

A: 没有。昌叔助手本身就是一个Hermes skill，它通过调用Hermes的其他skill来扩展功能。

### Q: 如何为昌叔助手添加新功能？

A: 有两种方式：
1. 安装现有的Hermes skill，然后通过`run`命令调用
2. 修改昌叔助手的代码，添加新的功能模块

### Q: 安装的skill在哪里？

A: 安装的skill会放在`~/.hermes/skills/`目录下的对应分类中。

## 推荐阅读

- [Skill安装指南](SKILL_INSTALL_GUIDE.md) - 详细的安装和使用说明
- [Skill常见问题](SKILL_FAQ.md) - 常见问题解答
- [README.md](README.md) - 昌叔助手完整文档

## 总结

1. **昌叔助手本身就是一个Hermes skill**
2. **通过`hermes skills install`安装其他skill**
3. **通过`run`命令在昌叔助手中调用这些skill**
4. **所有skill都存储在`~/.hermes/skills/`目录中**
5. **昌叔助手通过`hermes chat -s <skill>`命令来调用skill**

---

**昌叔，现在明白了吗？** 😊

简单来说：
- 昌叔助手 = 一个Hermes skill
- 其他skill = 安装到Hermes，然后昌叔助手可以调用
- 不需要在昌叔助手目录下创建skill目录
