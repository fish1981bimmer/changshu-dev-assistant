# 昌叔助手 - 大模型配置指南

## 🎉 大模型功能已添加！

昌叔助手现在支持连接大模型了！配置后可以获得真正的AI回答。

## 📋 支持的大模型提供商

- **OpenAI** (GPT-3.5, GPT-4等)
- **Anthropic** (Claude等)
- **自定义API** (兼容OpenAI格式的API)

## 🔧 配置步骤

### 1. 编辑配置文件

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant

# 编辑配置文件
vi config.yaml
# 或
nano config.yaml
# 或
open config.yaml
```

### 2. 配置大模型API

找到 `ai` 部分，修改配置：

```yaml
ai:
  model: "local"
  temperature: 0.7
  max_tokens: 2000
  context_window: 4000
  # 大模型API配置
  provider: "openai"  # openai, anthropic, local, custom
  api_key: "你的API密钥"  # 在这里填入你的API密钥
  api_base: ""  # 自定义API端点，如需要
  model_name: "gpt-3.5-turbo"  # 使用的模型名称
  timeout: 30  # 请求超时时间（秒）
```

### 3. 配置示例

#### OpenAI配置

```yaml
ai:
  provider: "openai"
  api_key: "sk-xxxxxxxxxxxxxxxxxxxxxxxx"
  model_name: "gpt-3.5-turbo"
  temperature: 0.7
  max_tokens: 2000
```

#### Anthropic配置

```yaml
ai:
  provider: "anthropic"
  api_key: "sk-ant-xxxxxxxxxxxxxxxxxxxxxxxx"
  model_name: "claude-3-sonnet-20240229"
  temperature: 0.7
  max_tokens: 2000
```

#### 自定义API配置

```yaml
ai:
  provider: "custom"
  api_key: "你的API密钥"
  api_base: "https://your-api-endpoint.com/v1/chat"
  model_name: "your-model-name"
  temperature: 0.7
  max_tokens: 2000
```

## 🚀 使用方法

配置完成后，就可以使用大模型功能了：

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant

# 启动交互式对话
./start.sh chat

# 或使用快捷命令
csa chat
```

## 💬 使用示例

```
昌叔助手 > 如何优化达梦数据库查询？
昌叔助手 > status
昌叔助手 > diagnose
昌叔助手 > quit
```

## ⚠️ 注意事项

1. **API密钥安全**：不要将API密钥提交到公开仓库
2. **费用控制**：注意API调用费用，设置合理的max_tokens
3. **网络连接**：确保网络可以访问API端点
4. **超时设置**：根据网络情况调整timeout参数

## 🔍 故障排查

### 问题1：仍然返回模板响应

**原因**：API密钥未配置或配置错误

**解决**：
1. 检查config.yaml中的api_key是否正确
2. 确认provider设置正确
3. 检查网络连接

### 问题2：调用大模型失败

**原因**：网络问题或API配置错误

**解决**：
1. 检查网络连接
2. 确认API端点可访问
3. 检查API密钥是否有效
4. 查看错误信息

### 问题3：响应很慢

**原因**：网络延迟或模型选择

**解决**：
1. 增加timeout参数
2. 选择更快的模型（如gpt-3.5-turbo）
3. 减少max_tokens

## 📚 相关文档

- `CHAT_GUIDE.md` - Chat功能使用说明
- `SIMPLE_GUIDE.md` - 超简单使用指南
- `README.md` - 完整使用文档

## 🎯 推荐配置

对于日常使用，推荐以下配置：

```yaml
ai:
  provider: "openai"
  api_key: "你的API密钥"
  model_name: "gpt-3.5-turbo"
  temperature: 0.7
  max_tokens: 2000
  timeout: 30
```

这个配置平衡了响应速度、质量和成本。

## 💡 提示

- 如果没有API密钥，助手会返回模板响应，并提示配置
- 配置API密钥后，助手会提供真正的AI回答
- 可以随时修改配置文件来调整参数

有问题随时问我！
