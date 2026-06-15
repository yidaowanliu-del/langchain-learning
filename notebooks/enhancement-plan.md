# Notebooks 完善计划

## 对比分析

### ✅ 已有内容（01-core-concepts）
- 00-langchain-overview - LangChain 概览
- 01-chat-models - 聊天模型
- 02-prompt-parsers - 提示词解析
- 03-lcel - LCEL
- 04-tools - 工具
- 05-streaming - 流式输出
- 06-middleware - 中间件
- 07-agent - Agent
- 08-messages-runnable - 消息与 Runnable
- 09-callbacks - 回调
- 10-document - 文档

### 📋 待补充内容

#### 基础配置
- [ ] 环境搭建指南（新建 00-setup.ipynb）
- [ ] DeepSeek 配置说明（整合到现有 notebook）

#### 核心概念补充
- [ ] 常用参数（补充到 01-chat-models）
- [ ] Chat Model 高级用法（补充到 01-chat-models）
- [ ] 消息类型详解（补充到 08-messages-runnable）
- [ ] 工具高级特性（补充到 04-tools）
- [ ] 提示词最佳实践（补充到 02-prompt-parsers）

#### Agent 进阶
- [ ] create_agent() 函数详解（补充到 07-agent）
- [ ] AgentState 管理（补充到 07-agent）
- [ ] Agent 工作流程详解（补充到 07-agent）
- [ ] 结构化输出（新建 11-structured-output.ipynb）
- [ ] 输出策略（补充到 11-structured-output）
- [ ] 模型调用拦截（补充到 06-middleware）
- [ ] 工具调用拦截（补充到 06-middleware）
- [ ] @before_agent 钩子（补充到 06-middleware）
- [ ] 对话记忆（新建 12-memory.ipynb）
- [ ] 跨会话存储（补充到 12-memory）
- [ ] 人工介入（补充到 12-memory）
- [ ] 多 Agent 协作（新建 13-multi-agent.ipynb）

#### RAG 应用
- [ ] RAG 基础（新建 02-rag/00-rag-intro.ipynb）
- [ ] 文档加载器（补充到 10-document）
- [ ] RAG Agent（新建 02-rag/01-rag-agent.ipynb）
- [ ] 智能客服实战（新建 02-rag/02-smart-customer-service.ipynb）
- [ ] 个人知识库（新建 02-rag/03-personal-kb.ipynb）
- [ ] 个人助手（新建 02-rag/04-personal-assistant.ipynb）

#### 工程化
- [ ] LangSmith 链路追踪（新建 03-engineering/00-langsmith.ipynb）
- [ ] 错误处理（新建 03-engineering/01-error-handling.ipynb）
- [ ] 配置管理（新建 03-engineering/02-config.ipynb）

#### API 参考
- [ ] Chat Model API（新建 04-reference/00-chat-model-api.ipynb）
- [ ] Agent API（新建 04-reference/01-agent-api.ipynb）
- [ ] Messages API（新建 04-reference/02-messages-api.ipynb）
- [ ] Tools API（新建 04-reference/03-tools-api.ipynb）
- [ ] Middleware API（新建 04-reference/04-middleware-api.ipynb）

## 优先级

### P0 - 核心缺失（立即补充）
1. 00-setup.ipynb - 环境搭建
2. 11-structured-output.ipynb - 结构化输出
3. 12-memory.ipynb - 对话记忆
4. 02-rag/00-rag-intro.ipynb - RAG 基础

### P1 - 进阶内容（重要但不紧急）
1. 补充现有 notebook 的高级特性
2. 13-multi-agent.ipynb - 多 Agent
3. RAG 实战系列（智能客服、知识库）

### P2 - 工程化与参考（可后续补充）
1. LangSmith、错误处理
2. API 参考手册

## 目录结构规划

```
notebooks/
├── 00-setup.ipynb                 [新建] 环境搭建
├── 01-core-concepts/
│   ├── 00-langchain-overview.ipynb
│   ├── 01-chat-models.ipynb      [补充] 高级用法、常用参数
│   ├── 02-prompt-parsers.ipynb   [补充] 最佳实践
│   ├── 03-lcel.ipynb
│   ├── 04-tools.ipynb            [补充] 高级特性
│   ├── 05-streaming.ipynb
│   ├── 06-middleware.ipynb       [补充] 拦截器、钩子
│   ├── 07-agent.ipynb            [补充] create_agent、AgentState、工作流程
│   ├── 08-messages-runnable.ipynb [补充] 消息类型详解
│   ├── 09-callbacks.ipynb
│   ├── 10-document.ipynb         [补充] 文档加载器
│   ├── 11-structured-output.ipynb [新建] 结构化输出
│   ├── 12-memory.ipynb           [新建] 对话记忆、跨会话存储、人工介入
│   └── 13-multi-agent.ipynb      [新建] 多 Agent 协作
├── 02-rag/
│   ├── 00-rag-intro.ipynb        [新建] RAG 基础
│   ├── 01-rag-agent.ipynb        [新建] RAG Agent
│   ├── 02-smart-customer-service.ipynb [新建] 智能客服实战
│   ├── 03-personal-kb.ipynb      [新建] 个人知识库
│   └── 04-personal-assistant.ipynb [新建] 个人助手
├── 03-engineering/
│   ├── 00-langsmith.ipynb        [新建] 链路追踪
│   ├── 01-error-handling.ipynb   [新建] 错误处理
│   └── 02-config.ipynb           [新建] 配置管理
└── 04-reference/
    ├── 00-chat-model-api.ipynb   [新建]
    ├── 01-agent-api.ipynb        [新建]
    ├── 02-messages-api.ipynb     [新建]
    ├── 03-tools-api.ipynb        [新建]
    ├── 04-middleware-api.ipynb   [新建]
    └── 05-config-error.ipynb     [新建] 配置与错误类
```
