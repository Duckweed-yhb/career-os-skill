# 第 01 课：环境搭建与第一个 API

> 示例课程文档，展示每节课的完整结构。对应项目 TaskFlow 的第一课。

## 学习目标

- 装好 Node.js 与包管理器，理解 `npm` 的基本命令
- 用 Fastify 创建一个能返回 JSON 的最小 API 服务
- 理解"路由 → 处理器 → 响应"的最小后端链路

## 前置要求

- 无需任何后端经验；会打开终端即可
- 有任意代码编辑器（VS Code 推荐）

## 最小知识

**Node.js 是什么**：一个让你用 JavaScript 写后端程序的运行时。`node` 执行 `.js` 文件，`npm` 管理依赖包。

**路由与处理器**：每个接口 = 一个 URL（路由）+ 一个函数（处理器）。请求来了，框架把请求交给匹配的路由的处理器，处理器返回响应。

**Fastify 最小示例**（10 分钟能跑通）：

```js
import Fastify from 'fastify'

const app = Fastify()

app.get('/ping', async () => ({ pong: true }))

app.listen({ port: 3000 }).then(() => {
  console.log('Server on http://localhost:3000')
})
```

## 动手任务

**目标**：把 TaskFlow 的骨架立起来，跑通 `/health` 接口。

1. 安装 Node.js 20+（官网下载 LTS 版，`node -v` 确认版本）
2. 创建项目目录并初始化：

   ```bash
   mkdir taskflow && cd taskflow
   npm init -y
   npm install fastify typescript tsx @types/node
   ```

3. 创建 `src/server.ts`，实现两个接口：
   - `GET /health` → `{ "status": "ok" }`
   - `GET /` → 返回项目名和版本
4. 在 `package.json` 加启动脚本：`"dev": "tsx watch src/server.ts"`
5. 运行 `npm run dev`，用浏览器或 `curl` 访问 `http://localhost:3000/health`，看到 `{"status":"ok"}`

## 验收标准

- [ ] `node -v` 输出 v20 或更高
- [ ] `npm run dev` 启动无报错
- [ ] 访问 `/health` 返回 `{"status":"ok"}`
- [ ] 修改处理器代码后服务自动重启（tsx watch 生效）

## 常见坑

- **`npm install` 很慢或失败**：换国内镜像 `npm config set registry https://registry.npmmirror.com`
- **端口被占用**：`EADDRINUSE` 报错 → 换 `3001` 或杀掉占用进程
- **中文路径导致 TS 报错**：把项目放到纯英文路径下

## 预计时长

- 约 1–2 小时（含环境安装）
