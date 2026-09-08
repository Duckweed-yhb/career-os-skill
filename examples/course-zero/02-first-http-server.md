# 第 02 课：你的第一个网页服务（零基础）

> 示例课程：零基础用户的第一课——不引入任何框架，用 Node 内置模块做出一个浏览器能访问的服务。让"后端"这个概念第一次变得可见。

## 学习目标

- 理解 HTTP 是什么：浏览器发请求 → 服务器回内容
- 理解"端口"和 `localhost`
- 用 Node 内置的 `http` 模块写一个返回 JSON 的服务

## 前置要求

- 完成第 01 课（Node 环境可用）

## 最小知识

**HTTP 一句话**：你的浏览器向服务器要东西（请求），服务器把东西给回来（响应）。

**localhost 与端口**：`localhost` 就是"我自己的电脑"。`:3000` 是"门牌号"（端口）。浏览器访问 `http://localhost:3000`，就是让本机的服务把内容给你。

**最小服务代码**（Node 内置，不用装任何东西）：

```js
const http = require('http')

const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'application/json')
  res.end(JSON.stringify({ hello: 'world' }))
})

server.listen(3000, () => {
  console.log('服务已启动: http://localhost:3000')
})
```

- `http.createServer(函数)`：创建服务，每次收到请求就调用这个函数
- `res.end(...)`：把内容发回给浏览器
- `server.listen(3000)`：让服务在 3000 端口等着

## 动手任务

1. 在 `taskflow` 文件夹里新建 `server.js`，粘贴上面的代码。
2. 终端运行：`node server.js`，看到"服务已启动"。
3. 打开浏览器访问 `http://localhost:3000`——你会看到 `{"hello":"world"}`。
4. 改动：把返回内容改成项目名和版本：

   ```js
   res.end(JSON.stringify({ project: 'TaskFlow', version: '0.0.1' }))
   ```

5. **改完必须重启服务**：在终端按 `Ctrl+C` 停掉，再 `node server.js` 启动。刷新浏览器看变化。

## 验收标准

- [ ] 浏览器访问 `http://localhost:3000` 能看到 `{"project":"TaskFlow","version":"0.0.1"}`
- [ ] 理解并说出：请求是谁发的、响应是谁回的
- [ ] 改代码 → 重启 → 刷新，这个循环你独立走通了一遍

## 常见坑

- **改完代码浏览器没变化**：99% 是没重启服务——`Ctrl+C` 停掉再启动
- **`EADDRINUSE` 报错**：3000 端口被占了，把代码里的 `3000` 改成 `3001` 再试
- **终端卡住不动**：那不是卡死，是服务在运行。想退出就按 `Ctrl+C`

## 预计时长

- 约 1.5–2 小时

---

**下一课预告**：你会学到"数组和对象"，然后很快就能给服务加上真实的数据了。
