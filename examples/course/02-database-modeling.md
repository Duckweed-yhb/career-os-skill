# 第 02 课：数据库建模与迁移

> 示例课程文档，展示每节课的完整结构。对应项目 TaskFlow 的第二课。

## 学习目标

- 理解关系型数据库的基本概念：表、主键、外键、关系
- 学会用迁移（migration）管理表结构，而不是手工改库
- 为 TaskFlow 设计并创建四张核心表

## 前置要求

- 完成第 01 课（Node 环境可用）
- 安装 Docker（本课用 Docker 跑 PostgreSQL，避免本机安装）

## 最小知识

**表与关系**：数据存在"表"里，表之间用外键关联。本项目的四张表：

```
users   1───∞ projects   1───∞ tasks   1───∞ comments
              (创建者)          (所属项目)      (所属任务)
                                 ↑
                                 └──∞ assignees（任务-用户多对多）
```

**迁移（Migration）**：用代码文件描述表结构的变化，按顺序执行。好处：团队和 CI 环境能复现完全相同的库结构。

**主键 vs 外键**：主键唯一标识一行；外键指向另一张表的行，保证引用完整。

## 动手任务

**目标**：用 Docker 启动 PostgreSQL，创建四张表并写入种子数据。

1. 启动数据库：

   ```bash
   docker run -d --name taskflow-db \
     -e POSTGRES_PASSWORD=devpass -e POSTGRES_DB=taskflow \
     -p 5432:5432 postgres:16
   ```

2. 安装迁移工具：

   ```bash
   npm install pg dotenv
   npm install -D tsx @types/pg
   ```

3. 创建 `db/migrations/001-init.sql`，按上面的 ER 图写四张表：
   - `users`：id（uuid 主键）、email（唯一）、password_hash、created_at
   - `projects`：id、name、owner_id（外键→users）
   - `tasks`：id、title、status（默认 'todo'）、project_id（外键→projects）
   - `comments`：id、content、task_id（外键→tasks）、author_id（外键→users）
4. 写一个 `db/migrate.ts` 脚本：连接数据库，按文件名顺序执行 `migrations/` 下的 SQL
5. 写 `db/seed.sql` 插入 1 个用户、1 个项目、2 个任务，运行后验证

## 验收标准

- [ ] `docker ps` 看到 taskflow-db 运行中
- [ ] `npm run migrate` 执行成功无报错
- [ ] 用 `psql` 或 GUI 客户端（如 DBeaver）能看到四张表
- [ ] 种子数据插入成功，`SELECT count(*) FROM tasks;` 返回 2

## 常见坑

- **Docker 端口冲突**：`5432` 被占用 → 换 `5433:5432`，并同步改连接串
- **迁移脚本重复执行报错**：先 `DROP TABLE IF EXISTS` 或加版本表
- **连接失败 ECONNREFUSED**：确认容器启动了（`docker start taskflow-db`）

## 预计时长

- 约 2 小时
