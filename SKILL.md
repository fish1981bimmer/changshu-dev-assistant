---
name: changshu-dev-assistant
version: 3.0.0
description: 昌叔专属软件开发助手 - 以达梦数据库工具为核心，专注SQL Server→达梦迁移、代码安全扫描、知识库搜索
author: Hermes Agent
tags: [dev, assistant, local, database, ai, system]
---

# 昌叔专属软件开发助手

为昌叔量身定制的专属软件开发助手，以达梦数据库工具为核心，专注SQL Server→达梦迁移、代码安全扫描、知识库检索。

## v3.0.0 — 重写重构

基于v2.3.0全面重构：删除6个stub/冗余脚本，重写全部6个核心模块，确保每个功能都真实可用。

### 核心改进
- **dameng_tool.py v3.0** — 15→16种兼容性检测、search_by_tags真实实现、字符串拼接+→||修复、test connect命令、sql format命令
- **changshu_assistant_main.py v3.0** — 修复6个AttributeError、review接入真实扫描、diagnose接入真实分析、删除假数据客户端
- **code_scanner.py** — 安全扫描+代码质量分析合二为一，修复误报，加白名单
- **knowledge_searcher.py** — 修复拼写错误+中文分词(jieba/bigram)+tag搜索实现+缓存过期
- **model_monitor.py** — 持久化到JSON+综合推荐模型
- **prompt_template_manager.py** — 变量替换+增删改+持久化

## 实际可用功能

### 1. 达梦数据库工具 (核心)
- 16种SQL Server→达梦兼容性检测（含NOLOCK）
- SQL自动优化（函数映射、字符串拼接+→||、WITH(NOLOCK)移除）
- 存储过程/函数/触发器模板生成
- SQL Server→达梦批量转换（接入dm_converter）
- 达梦数据库连接测试（需dmPython）
- SQL格式化（关键字大写+缩进）
- 知识库tag搜索（YAML frontmatter）

```bash
# 兼容性检测
python3 scripts/dameng_tool.py check input.sql

# SQL优化
python3 scripts/dameng_tool.py optimize input.sql output.sql

# SQL Server→达梦转换
python3 scripts/dameng_tool.py convert input_dir output_dir schema_prefix

# SQL格式化
python3 scripts/dameng_tool.py sql format input.sql

# 达梦连接测试
python3 scripts/dameng_tool.py test connect host port user password

# 知识库tag搜索
python3 scripts/dameng_tool.py search "sql conversion" --path ~/wiki --type tags
```

### 2. 代码安全扫描 + 质量分析
- 5类漏洞检测（SQL注入、硬编码密码、不安全文件操作、命令注入、XSS）
- 白名单排除机制
- 行长度检测、圈复杂度估算、重复代码检测
- 分级报告（critical/warning/info）

```bash
# 安全+质量全扫描
python3 scripts/code_scanner.py /path/to/project

# 仅安全扫描
python3 scripts/code_scanner.py /path/to/project --security-only

# 仅质量分析
python3 scripts/code_scanner.py /path/to/project --quality-only

# 排除目录
python3 scripts/code_scanner.py /path/to/project --whitelist-dir tests --whitelist-dir docs
```

### 3. 知识库搜索
- 内容搜索（关键词匹配+上下文摘录）
- Tag搜索（YAML frontmatter）
- 语义搜索（jieba中文分词/bigram fallback）
- 缓存过期机制

```bash
# 内容搜索
python3 scripts/knowledge_searcher.py content "达梦转换" --path ~/wiki

# Tag搜索
python3 scripts/knowledge_searcher.py tags "sql" "database" --path ~/wiki

# 语义搜索
python3 scripts/knowledge_searcher.py semantic "SQL Server迁移达梦" --path ~/wiki
```

### 4. 主程序交互模式
```bash
# 交互式对话（接入LLM）
python3 scripts/changshu_assistant_main.py chat

# SQL子命令
python3 scripts/changshu_assistant_main.py sql analyze input.sql
python3 scripts/changshu_assistant_main.py sql optimize input.sql
python3 scripts/changshu_assistant_main.py sql check input.sql
python3 scripts/changshu_assistant_main.py sql convert input_dir output_dir prefix
python3 scripts/changshu_assistant_main.py sql format input.sql
python3 scripts/changshu_assistant_main.py sql connect host port user pass

# 扫描子命令
python3 scripts/changshu_assistant_main.py scan security /path/to/project
python3 scripts/changshu_assistant_main.py scan quality /path/to/project

# 搜索子命令
python3 scripts/changshu_assistant_main.py search content "关键词" --path ~/wiki
python3 scripts/changshu_assistant_main.py search tags "tag1" "tag2" --path ~/wiki
```

### 5. 模型监控 + Prompt模板
```bash
# 模型使用统计
python3 scripts/model_monitor.py stats

# 推荐最佳模型
python3 scripts/model_monitor.py recommend

# Prompt模板使用
python3 scripts/prompt_template_manager.py list
python3 scripts/prompt_template_manager.py get code review
python3 scripts/prompt_template_manager.py render code review --var code="SELECT * FROM users" --var language=SQL
python3 scripts/prompt_template_manager.py add mycategory mytask "模板内容{var}" --desc "描述"
python3 scripts/prompt_template_manager.py delete mycategory mytask
```

## 文件结构

```
changshu-dev-assistant/
├── SKILL.md
├── scripts/
│   ├── changshu_assistant_main.py  # 主程序 v3.0 (交互+LLM+统一入口)
│   ├── dameng_tool.py              # 达梦数据库工具 v3.0 (核心模块)
│   ├── code_scanner.py             # 代码安全扫描+质量分析
│   ├── knowledge_searcher.py       # 知识库搜索(中文分词+tag)
│   ├── model_monitor.py            # 模型性能监控(持久化)
│   └── prompt_template_manager.py  # Prompt模板管理(变量替换+CRUD)
├── templates/
│   └── config.example.yaml
├── references/
│   ├── dameng_database_guide.md
│   └── audit-2026-06-06.md
└── config/
    └── (可选配置)
```

## 已删除的模块 (v3.0清理)

| 原脚本 | 删除原因 |
|--------|---------|
| code_generator.py | Stub — 只做文本插值，无智能代码生成 |
| ai_enhanced_client.py | Stub — API调用返回假数据，会污染主程序 |
| ai_model_selector.py | 冗余 — 与enhanced_client重复，功能过简 |
| test_automation_tool.py | 致命BUG — 文件以markdown标记开头无法执行 |
| test_automation_example.py | Stub — 仅打印说明文本 |
| test_automation_integration.py | 冗余 — 纯包装层无额外价值 |

## 更新日志

### v3.0.0 (2026-06-20)
- 🔄 **全面重构** — 以dameng-tool.py为核心重写，12个脚本→6个
- 🗑️ **删减虚功能** — 删除6个stub/冗余脚本，SKILL.md去虚存实
- ✅ **修复所有已知BUG** — 6个AttributeError、假数据review/diagnose、假API客户端、拼写错误、markdown标记
- 🆕 **dameng_tool v3.0** — search_by_tags真实实现、test connect命令、sql format命令、字符串拼接修复
- 🆕 **code_scanner** — 安全扫描+质量分析合二为一，白名单机制，分级报告
- 🆕 **knowledge_searcher** — 中文分词(jieba/bigram)、tag搜索、缓存过期、环境变量WIKI_PATH
- 🆕 **model_monitor** — JSON持久化、综合推荐、CLI
- 🆕 **prompt_template_manager** — 变量替换、增删改、持久化

### v2.3.0 (2026-06-06)
- 去重整合：19个脚本精简到12个

### v2.2.0 (2026-05-17)
- 新增AI增强客户端、模型监控、配置热重载、测试自动化

### v2.1.0 (2026-05-10)
- 新增12个核心功能模块

### v1.0.0 (2026-04-26)
- 初始版本发布
