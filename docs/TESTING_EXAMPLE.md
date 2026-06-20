name: test-automation-example
version: 1.0.0
description: 测试自动化功能使用示例
author: Hermes Agent
tags: [dev, testing, example]

# 测试自动化功能使用示例

## 概述

这个技能展示了昌叔助手的测试自动化功能，包括测试用例生成、测试运行和覆盖率分析。

## 使用方法

### 1. 生成测试用例
```bash
# 生成测试用例
changshu-assistant test-generate --file <source_file> --type <framework>
```

### 2. 运行测试
```bash
# 运行测试
changshu-assistant test-run --file <test_file> --type <framework>
```

### 3. 分析测试覆盖率
```bash
# 分析测试覆盖率
changshu-assistant test-analyze --file <source_file> --test-file <test_file>
```

## 示例

### 生成测试用例
```bash
# 生成pytest测试用例
changshu-assistant test-generate --file myapp.py --type pytest

# 生成unittest测试用例
changshu-assistant test-generate --file myapp.py --type unittest
```

### 运行测试
```bash
# 运行pytest测试
changshu-assistant test-run --file test_myapp.py --type pytest

# 运行unittest测试
changshu-assistant test-run --file test_myapp.py --type unittest
```

### 分析测试覆盖率
```bash
# 分析测试覆盖率
changshu-assistant test-analyze --file myapp.py --test-file test_myapp.py
```

## 配置

在昌叔助手的配置文件中启用测试自动化功能:
```yaml
features:
  test_automation: true

testing:
  frameworks:
    - pytest
    - unittest
```

## 常见问题

### Q: 如何生成测试用例？
A: 使用`changshu-assistant test-generate`命令生成测试用例。

### Q: 如何运行测试？
A: 使用`changshu-assistant test-run`命令运行测试。

### Q: 如何分析测试覆盖率？
A: 使用`changshu-assistant test-analyze`命令分析测试覆盖率。