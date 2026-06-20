# Skill安装常见问题

## Q1: 昌叔助手有自己的skill目录吗？

**A:** 没有。昌叔助手本身就是一个Hermes skill，位于：
```
~/.hermes/skills/devops/changshu-dev-assistant
```

昌叔助手通过调用Hermes的其他skill来扩展功能，而不是自己管理skill目录。

## Q2: 如何为昌叔助手添加新功能？

**A:** 有两种方式：

### 方式1：安装现有的Hermes skill（推荐）
```bash
# 搜索skill
hermes skills search <关键词>

# 安装skill
hermes skills install <skill-identifier>

# 在昌叔助手中使用
cd ~/.hermes/skills/devops/changshu-dev-assistant
./start.sh run <skill-name> "你的问题"
```

### 方式2：修改昌叔助手的代码
直接修改`scripts/changshu-assistant.py`，添加新的功能模块。

## Q3: 安装的skill在哪里？

**A:** 安装的skill会放在`~/.hermes/skills/`目录下的对应分类中：

```
~/.hermes/skills/
├── apple/                    # Apple相关skills
├── autonomous-ai-agents/    # AI代理相关skills
├── creative/                 # 创意相关skills
├── database/                # 数据库相关skills
├── devops/                   # DevOps相关skills
│   └── changshu-dev-assistant/  # 昌叔助手
├── github/                   # GitHub相关skills
└── ...
```

## Q4: 如何查看已安装的skills？

**A:** 使用以下命令：

```bash
# 列出所有已安装的skills
hermes skills list

# 查看特定skill的详情
hermes skills inspect <skill-name>

# 在昌叔助手中查看
cd ~/.hermes/skills/devops/changshu-dev-assistant
./start.sh skill <skill-name>
```

## Q5: 如何卸载skill？

**A:** 使用以下命令：

```bash
hermes skills uninstall <skill-identifier>
```

## Q6: 如何更新skill？

**A:** 使用以下命令：

```bash
# 检查更新
hermes skills check

# 更新特定skill
hermes skills update <skill-identifier>
```

## Q7: 为什么有些skill找不到？

**A:** 可能的原因：

1. **skill未安装** - 需要先安装skill
2. **skill名称错误** - 检查skill名称是否正确
3. **skill在本地但未注册** - 运行`hermes skills audit`重新扫描

解决方法：
```bash
# 重新扫描本地skills
hermes skills audit

# 搜索skill
hermes skills search <关键词>

# 安装skill
hermes skills install <skill-identifier>
```

## Q8: 如何从GitHub安装skill？

**A:** 使用以下命令：

```bash
# 从GitHub仓库安装
hermes skills install github:<username>/<repo>

# 示例
hermes skills install github:fish1981bimmer/skill-orchestration-core
```

## Q9: 如何手动安装skill？

**A:** 使用以下步骤：

```bash
# 1. 确定skill的分类（category）
cd ~/.hermes/skills/<category>/

# 2. 克隆skill到本地
git clone <skill-repo> <skill-name>

# 3. 确保skill目录包含SKILL.md文件
cd <skill-name>
ls SKILL.md

# 4. 重新扫描skill
hermes skills audit
```

## Q10: 昌叔助手如何调用skill？

**A:** 昌叔助手通过以下方式调用skill：

```bash
# 实际执行的是：
hermes chat -s <skill-name> -q "<query>"

# 参数说明：
# -s: 预加载skill
# -q: 查询内容
```

## Q11: Skill调用失败怎么办？

**A:** 检查以下几点：

1. **skill是否已安装**
   ```bash
   hermes skills list | grep <skill-name>
   ```

2. **skill名称是否正确**
   ```bash
   hermes skills inspect <skill-name>
   ```

3. **hermes命令是否可用**
   ```bash
   which hermes
   hermes --version
   ```

4. **查看详细错误信息**
   ```bash
   cd ~/.hermes/skills/devops/changshu-dev-assistant
   ./start.sh run <skill-name> "test" 2>&1
   ```

## Q12: 推荐安装哪些skill？

**A:** 根据昌叔的工作需求，推荐以下skills：

### 数据库相关
- `dameng-stored-procedure-review` - 达梦存储过程审查（已内置在database/）

### 开发相关
- `claude-code` - Claude Code集成（已内置）
- `test-driven-development` - 测试驱动开发
- `systematic-debugging` - 系统化调试

### DevOps相关
- `ssh-ops-optimization` - SSH运维优化
- `config-hot-reload` - 配置热重载

### 协同相关
- `openclaw-collab` - OpenClaw协同
- `hermes-skill-publishing` - Skill发布

## Q13: 如何创建自己的skill？

**A:** 创建skill的步骤：

1. **创建skill目录结构**
   ```bash
   mkdir -p ~/.hermes/skills/<category>/<skill-name>
   cd ~/.hermes/skills/<category>/<skill-name>
   ```

2. **创建SKILL.md文件**
   ```bash
   touch SKILL.md
   ```

3. **编写skill内容**
   SKILL.md格式：
   ```yaml
   ---
   name: your-skill-name
   description: Your skill description
   version: 1.0
   ---

   # Skill Title

   ## 触发条件
   - When to use this skill

   ## 步骤
   1. Step 1
   2. Step 2

   ## 注意事项
   - Important notes
   ```

4. **测试skill**
   ```bash
   hermes skills audit
   hermes skills inspect <skill-name>
   ```

## Q14: Skill和插件有什么区别？

**A:**

- **Skill**: 功能模块，提供特定领域的知识和工作流程
  - 存储在`~/.hermes/skills/`
  - 通过`hermes skills`命令管理
  - 可以被agent调用

- **Plugin**: 扩展Hermes核心功能的组件
  - 存储在`~/.hermes/plugins/`
  - 通过`hermes plugins`命令管理
  - 扩展Hermes本身的能力

## Q15: 如何分享自己创建的skill？

**A:** 有几种方式：

1. **发布到GitHub**
   ```bash
   # 创建GitHub仓库
   # 推送skill代码
   # 其他人可以通过以下方式安装：
   hermes skills install github:<username>/<repo>
   ```

2. **发布到Skills Hub**
   - 需要注册skills.sh账户
   - 提交skill到skills.sh
   - 其他人可以通过以下方式安装：
   ```bash
   hermes skills install skills-sh/<category>/<skill-name>
   ```

3. **直接分享**
   - 打包skill目录
   - 其他人手动安装到`~/.hermes/skills/`

## 更多帮助

- 详细文档：[SKILL_INSTALL_GUIDE.md](SKILL_INSTALL_GUIDE.md)
- Hermes官方文档：运行`hermes --help`
- 社区支持：Hermes GitHub仓库
