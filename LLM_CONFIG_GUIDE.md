# 昌叔助手 - 大模型配置指南

## 支持的大模型提供商

- OpenAI兼容格式 (NVIDIA/DeepSeek/GLM/OpenRouter等)
- Anthropic格式
- 自定义API端点

## 配置步骤

### 1. 编辑配置文件

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant
vi config.yaml
```

### 2. 通过环境变量配置（推荐）

敏感信息均通过环境变量注入，不要在config.yaml中明文填写：

```bash
export LLM_PROVIDER="openai"        # API格式: openai(兼容格式)/anthropic/custom
export LLM_API_KEY="your-api-key"   # API密钥
export LLM_API_BASE="https://your-api-endpoint/v1"  # API基础URL
export LLM_MODEL_NAME="your-model-name"  # 模型名称
```

环境变量优先级高于config.yaml。

### 3. 通过配置文件设置

在 `config.yaml` 的 `ai` 段配置：

```yaml
ai:
  temperature: 0.7
  max_tokens: 2000
  context_window: 4000
  provider: ""      # 通过环境变量LLM_PROVIDER设置
  api_key: ""       # 通过环境变量LLM_API_KEY设置，勿明文填写
  api_base: ""      # 通过环境变量LLM_API_BASE设置
  model_name: ""    # 通过环境变量LLM_MODEL_NAME设置
  timeout: 120
```

### 4. 配置示例

#### OpenAI兼容格式（NVIDIA/DeepSeek/GLM等）

```yaml
ai:
  provider: "openai"  # 兼容格式
  # api_key, api_base, model_name 通过环境变量设置
  temperature: 0.7
  max_tokens: 2000
```

对应环境变量：
```bash
export LLM_API_BASE="https://integrate.api.nvidia.com/v1"
export LLM_MODEL_NAME="your-model-name"
export LLM_API_KEY="your-api-key"
```

#### Anthropic格式

```yaml
ai:
  provider: "anthropic"
  # api_key, api_base, model_name 通过环境变量设置
  temperature: 0.7
  max_tokens: 2000
```

#### 自定义API端点

```yaml
ai:
  provider: "custom"
  # api_key, api_base, model_name 通过环境变量设置
  temperature: 0.7
  max_tokens: 2000
```

## 使用方法

配置完成后：

```bash
cd /Users/a1234/.hermes/skills/devops/changshu-dev-assistant

# 启动交互式对话
./start.sh chat

# 或使用快捷命令
csa chat
```

## 注意事项

1. API密钥安全：不要将API密钥提交到公开仓库，务必通过环境变量设置
2. 费用控制：注意API调用费用，设置合理的max_tokens
3. 网络连接：确保网络可以访问API端点
4. 超时设置：根据网络情况调整timeout参数

## 故障排查

### 问题1：仍然返回模板响应

原因：API密钥未配置或配置错误

解决：
1. 检查环境变量LLM_API_KEY是否设置
2. 确认provider设置正确
3. 检查网络连接

### 问题2：调用大模型失败

原因：网络问题或API配置错误

解决：
1. 检查网络连接
2. 确认LLM_API_BASE端点可访问
3. 检查API密钥是否有效
4. 查看错误信息

### 问题3：响应很慢

原因：网络延迟或模型选择

解决：
1. 增加timeout参数
2. 选择响应更快的模型(通过LLM_MODEL_NAME环境变量切换)
3. 减少max_tokens
