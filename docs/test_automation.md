name: test-automation
version: 1.0.0
description: 测试自动化工具 - 支持pytest和unittest框架
author: Hermes Agent
tags: [testing, automation, pytest, unittest]

# 测试自动化工具

## 概述

这是一个为昌叔量身定制的测试自动化工具，支持pytest和unittest测试框架，可以自动生成测试用例、运行测试并生成测试报告。

## 功能特性

### 1. 测试用例自动生成
- 支持pytest和unittest框架
- 根据源代码自动生成测试模板
- 智能识别函数和类定义

### 2. 测试执行
- 运行pytest测试
- 运行unittest测试
- 生成详细的测试报告

### 3. 覆盖率分析
- 代码覆盖率统计
- 未覆盖行标识
- 覆盖率报告生成

## 安装依赖

```bash
# 安装pytest
pip install pytest

# 安装覆盖率分析工具
pip install coverage
```

## 使用方法

### 生成测试用例

```bash
# 为Python文件生成pytest测试用例
python test_automation_tool.py generate --source app.py --framework pytest

# 为Python文件生成unittest测试用例
python test_automation_tool.py generate --source app.py --framework unittest
```

### 运行测试

```bash
# 运行pytest测试
python test_automation_tool.py run --test-file test_app.py --framework pytest

# 运行unittest测试
python test_automation_tool.py run --test-file test_app.py --framework unittest
```

### 分析覆盖率

```bash
# 分析测试覆盖率
python test_automation_tool.py analyze --test-file test_app.py --source app.py
```

## 配置文件

```yaml
test_automation:
  frameworks:
    pytest:
      enabled: true
      options:
        verbose: true
        tb_style: short
    unittest:
      enabled: true
      options:
        verbosity: 2
  
  coverage:
    enabled: true
    report_type: html
    omit_patterns:
      - "test_*"
      - "*_test.py"
      - "*/tests/*"
```

## 集成方式

### 与昌叔助手集成

```python
# 在昌叔助手中调用测试自动化工具
from test_automation_tool import TestAutomationTool

# 创建测试自动化工具实例
test_tool = TestAutomationTool()

# 生成测试用例
test_file = test_tool.generate_test_cases("app.py", "pytest")

# 运行测试
results = test_tool.run_tests(test_file, "pytest")

# 生成报告
report = test_tool.generate_test_report(results)
```

## 最佳实践

### 1. 测试用例编写
```python
# TODO注释提供编写指导
def test_function_name(self):
    """测试函数说明"""
    # TODO: 添加测试逻辑
    # 示例:
    # result = module.function()  # 调用函数
    # assert result is not None  # 验证结果
    pass
```

### 2. 测试数据准备
- 使用setUp和tearDown方法准备测试数据
- 使用setUpClass和tearDownClass方法准备类级别数据

### 3. 断言使用
- 使用适当的断言方法
- 提供有意义的断言消息

## 常见问题

### Q: 如何处理测试依赖？
A: 在测试文件中使用setUp方法准备依赖，或使用pytest fixture。

### Q: 如何处理数据库测试？
A: 使用内存数据库或测试数据库，确保测试数据隔离。

### Q: 如何处理外部服务依赖？
A: 使用mock或stub模拟外部服务响应。

## 扩展功能

### 1. CI/CD集成
```yaml
# GitHub Actions示例
name: Test Automation
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8
    - name: Install dependencies
      run: |
        pip install pytest
        pip install -r requirements.txt
    - name: Run tests
      run: python test_automation_tool.py run --test-file test_app.py
```

### 2. 测试报告集成
- 生成HTML测试报告
- 集成到CI/CD流水线
- 发送测试结果通知

## 贡献指南

欢迎贡献代码和改进建议：
1. Fork项目
2. 创建特性分支
3. 提交更改
4. 发起Pull Request

## 许可证

MIT License - 专为昌叔定制