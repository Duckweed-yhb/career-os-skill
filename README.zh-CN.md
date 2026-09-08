# CareerOS

![CareerOS banner](assets/careeros-banner.jpg)

> 一套为你的职业成长而设计的操作系统。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](CHANGELOG.md)
[![Last Commit](https://img.shields.io/github/last-commit/Duckweed-yhb/career-os-skill)](https://github.com/Duckweed-yhb/career-os-skill)

**[English](README.md) | [简体中文](README.zh-CN.md)**

---

## 简介

**CareerOS** 不只是一个学习指南，它是一个动态的职业成长引擎。它帮你明确目标岗位，梳理所需技能栈，评估当前水平，并通过**真实项目推荐**来弥合差距。

它不只是告诉你"该学什么"，而是让你"动手去做"。根据你的领域、经验水平和学习节奏量身定制，最终带走的不只是新技能，还有一个能拿得出手的**作品集**。

## 安装

1. **克隆仓库**（或下载后解压）：

   ```bash
   git clone https://github.com/Duckweed-yhb/career-os-skill.git
   ```

2. **找到你所用 AI 助手的 skills 目录：**

   | 助手 | Skills 目录 |
   |---|---|
   | Claude Code | `~/.claude/skills/` |
   | 豆包 Agent | `<workspace>/.skills/` |
   | 其他助手 | 查阅对应助手的文档，确认 skills 目录位置 |

3. **把 Skill 复制到该目录下的 `career-os/` 文件夹：**

   ```bash
   # 示例（Claude Code）
   mkdir -p ~/.claude/skills/career-os
   cp SKILL.md ~/.claude/skills/career-os/
   ```

   想用中文版的话，复制 `SKILL.zh-CN.md` 即可。

4. **重启助手会话**并验证：

   ```text
   /CareerOS init
   ```

   看到初始化欢迎语，就说明安装成功了。

## 核心模块

就像操作系统管理硬件资源一样，CareerOS 管理你的职业资源：

### 1. 目标定位
- 解析你的兴趣与背景，锁定高潜力的目标岗位。
- 生成该岗位的能力雷达图。

### 2. 技能差距分析
- 对比你当前的简历/技能与目标岗位的要求。
- 识别出关键的缺失环节。

### 3. 项目生成器
- **拒绝玩具项目。** 根据缺失的技能点，生成具有工业级复杂度的实战项目构思。
- 包含技术栈建议、难点预测和验收标准。

### 4. 作品集构建
- 将项目转化为面试中的亮点。
- 提供简历描述优化建议和 GitHub README 撰写指南。

## 使用方式

在你的 AI 助手中加载 `CareerOS` Skill，然后尝试：

```text
/CareerOS init
/CareerOS analyze [你的简历内容或当前技能列表]
/CareerOS generate project --focus=[具体技术点，如 Redis/微服务]
```

完整流程示例见 [examples/frontend-to-fullstack.md](examples/frontend-to-fullstack.md)。

## 为什么选择 CareerOS？

- **行动导向** —— 从"输入模式"切换到"输出模式"。
- **语境感知** —— 理解你的经验水平，不推荐过难或过简单的任务。
- **结果驱动** —— 一切为了那个能写在简历上的作品。

## 许可证

[MIT License](LICENSE)

---

Made with ❤️ by Duckweed-yhb
