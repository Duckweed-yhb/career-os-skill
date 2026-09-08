# Template: Web Full-Stack

## Domain & typical roles

- Roles: Full-Stack Engineer, Backend Engineer (Node.js), Frontend Engineer with API ownership
- User domains: web apps, SaaS products, internal tools, e-commerce

## Canonical tech stack

| Layer | Default | Alternatives |
|---|---|---|
| Frontend | React + TypeScript + Vite | Vue 3, Next.js |
| Backend | Node.js + Fastify/Express + TypeScript | NestJS, Python FastAPI |
| Database | PostgreSQL | MySQL, MongoDB |
| Cache/Queue | Redis | — |
| Ops | Docker + GitHub Actions | — |

## Project archetypes

1. **Team task / project management tool** — auth, CRUD, state machine, notifications (Difficulty 2)
2. **URL shortener + analytics** — redirect service, link tracking, aggregation queries (Difficulty 1–2)
3. **E-commerce checkout flow** — cart, order state machine, payment-webhook simulation, inventory (Difficulty 2–3)
4. **Real-time collaboration board** — WebSocket, presence, conflict handling (Difficulty 3)

## Typical milestones

- **M1 Skeleton**: project scaffold, DB schema + migrations, auth (register/login), CI pipeline stub
- **M2 Core features**: domain CRUD, business rules/state machine, tests
- **M3 Hardening**: caching, performance (indexes, P95 targets), error handling, deploy (Docker)

## Lesson patterns

Web full-stack courses usually slice as:

1. Environment & first running API (env, framework basics, hello world route)
2. Data modeling & migrations (schema, seed, first query)
3. Auth (sessions/JWT, middleware)
4. Core CRUD (each entity one lesson: model → route → UI)
5. Business rules / state transitions
6. Caching & performance
7. Testing
8. Docker & CI/CD
9. Polish: README, demo, deploy

Each lesson pairs one knowledge increment with one project increment.
