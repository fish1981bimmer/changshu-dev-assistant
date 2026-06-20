# 昌叔助手运行模式说明

## 核心问题

**昌叔助手能否独立运行？**

**答案：可以独立运行核心功能，但skill调用功能需要hermes**

## 两种运行模式

### 模式1：完全独立运行（推荐用于工作环境）

昌叔助手的核心功能可以完全独立运行，不依赖hermes。

#### 独立运行的功能

✅ **大模型调用**
- 支持OpenAI API
- 支持Anthropic API
- 支持自定义API
- 完全独立，直接调用API

✅ **配置管理**
- 独立的配置文件（config.yaml）
- 配置热重载
- 完全独立

✅ **命令行界面**
- 交互式对话
- 命令行参数
- 完全独立

✅ **达梦数据库工具**
- SQL分析
- 存储过程生成
- 完全独立

✅ **系统诊断**
- 系统状态检查
- 完全独立

#### 独立运行示例

```bash
# 1. 配置API密钥
cd ~/.hermes/skills/devops/changshu-dev-assistant
cp templates/config.example.yaml config.yaml
# 编辑config.yaml，设置api_key

# 2. 运行助手
./start.sh chat

# 3. 直接提问
> 如何优化达梦数据库查询？

# 4. 使用达梦工具
> 在另一个终端：
./dmt.sh analyze /tmp/test.sql
```

#### 独立运行的优势

- ✅ 完全独立，不依赖hermes
- ✅ 适合工作环境（单位限制）
- ✅ 轻量级，资源占用低
- ✅ 安全，数据本地处理

### 模式2：依赖hermes运行（扩展功能）

如果需要使用skill调用功能，需要hermes。

#### 依赖hermes的功能

❌ **Skill调用**
- 查看skill详情：依赖hermes命令
- 运行skill：依赖hermes chat命令
- 需要hermes环境

#### 依赖hermes运行示例

```bash
# 1. 确保hermes可用
which hermes
hermes --version

# 2. 运行助手
cd ~/.hermes/skills/devops/changshu-dev-assistant
./start.sh chat

# 3. 调用skill
> skill claude-code
> run claude-code "帮我审查这段代码"
```

#### 依赖hermes的用途

- 📚 调用Hermes的丰富skill生态
- 🔄 扩展功能能力
- 🤝 与Hermes生态集成

## 功能对比

| 功能 | 独立运行 | 依赖hermes |
|------|---------|-----------|
| 大模型调用 | ✅ | ✅ |
| 配置管理 | ✅ | ✅ |
| 命令行界面 | ✅ | ✅ |
| 达梦数据库工具 | ✅ | ✅ |
| 系统诊断 | ✅ | ✅ |
| Skill查看 | ❌ | ✅ |
| Skill运行 | ❌ | ✅ |

## 推荐使用场景

### 场景1：工作环境（单位限制）

**推荐：完全独立运行**

```bash
# 配置API密钥
cd ~/.hermes/skills/devops/changshu-dev-assistant
cp templates/config.example.yaml config.yaml
# 编辑config.yaml，设置api_key

# 运行
./start.sh chat
```

**优势：**
- 不依赖hermes
- 符合单位环境限制
- 数据安全

### 场景2：个人开发（无限制）

**推荐：依赖hermes运行**

```bash
# 确保hermes可用
hermes --version

# 运行
cd ~/.hermes/skills/devops/changshu-dev-assistant
./start.sh chat

# 使用skill功能
> skill claude-code
> run claude-code "帮我审查这段代码"
```

**优势：**
- 可以调用Hermes的skill生态
- 功能更强大
- 扩展性更好

## 技术细节

### 独立运行的原理

昌叔助手的核心功能通过以下方式实现：

```python
# LLMClient - 直接调用API
class LLMClient:
    def call_llm(self, prompt, system_prompt=None):
        # 直接调用OpenAI/Anthropic/自定义API
        # 不依赖hermes
        pass

# 配置管理 - 读取本地配置文件
def load_config(self, config_path):
    # 读取config.yaml
    # 不依赖hermes
    pass

# 命令行界面 - Python argparse
def main():
    # 使用argparse解析命令行参数
    # 不依赖hermes
    pass
```

### 依赖hermes的原理

Skill调用功能通过以下方式实现：

```python
# SkillClient - 调用hermes命令
class SkillClient:
    def call_skill(self, skill_name, args=None):
        # 调用hermes chat命令
        cmd = ["hermes", "chat", "-s", skill_name, "-Q"]
        # 依赖hermes
        pass
```

## 如何选择运行模式

### 选择独立运行，如果：

- ✅ 工作环境有限制
- ✅ 不需要skill调用功能
- ✅ 只需要核心功能
- ✅ 追求轻量级

### 选择依赖hermes，如果：

- ✅ 需要skill调用功能
- ✅ 需要扩展功能
- ✅ 环境无限制
- ✅ 需要Hermes生态

## 配置示例

### 独立运行配置

```yaml
# config.yaml
assistant:
  name: "昌叔助手"
  personality: "专业、高效、贴心"
  language: "zh-CN"

ai:
  provider: "openai"  # 或 "anthropic" 或 "custom"
  api_key: "your-api-key"
  api_base: "https://api.openai.com/v1"  # 可选
  model_name: "gpt-3.5-turbo"
  temperature: 0.7
  max_tokens: 2000
  timeout: 30

features:
  system: true
  code: true
  database: true
  ai: true
  knowledge: true

preferences:
  output_format: "structured"
  code_style: "pep8"
  db_type: "dameng"
  ai_provider: "local"
```

### 依赖hermes配置

```yaml
# config.yaml（同上）
# 额外需要：
# 1. 安装hermes
# 2. 确保hermes命令可用
# 3. 安装需要的skills
```

## 常见问题

### Q1: 昌叔助手必须依赖hermes吗？

**A:** 不是。昌叔助手的核心功能可以完全独立运行，只有skill调用功能需要hermes。

### Q2: 工作环境限制怎么办？

**A:** 使用完全独立运行模式，只使用核心功能，不使用skill调用功能。

### Q3: 如何从独立运行切换到依赖hermes？

**A:** 只需确保hermes命令可用，然后就可以使用skill调用功能了。

### Q4: 独立运行会失去很多功能吗？

**A:** 不会。核心功能（大模型调用、达梦数据库工具、系统诊断等）都可以独立运行。

### Q5: 可以后续添加独立运行的skill功能吗？

**A:** 可以。可以修改代码，实现不依赖hermes的skill调用功能。

## 总结

**昌叔助手可以独立运行！**

- ✅ 核心功能完全独立
- ✅ 适合工作环境
- ✅ 轻量级、安全
- ❌ Skill调用需要hermes（可选）

**推荐：**
- 工作环境 → 独立运行
- 个人开发 → 依赖hermes（可选）

---

**昌叔，现在明白了吗？** 😊

简单来说：
- 昌叔助手 = 可以独立运行
- 核心功能 = 不依赖hermes
- Skill调用 = 需要hermes（可选）
- 工作环境 = 用独立运行模式
