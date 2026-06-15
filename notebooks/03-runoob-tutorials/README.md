# Runoob LangChain 教程系列

本目录基于 [菜鸟教程 RUNOOB](https://www.runoob.com/langchain/) 的 LangChain 教程创建，涵盖从基础到实战的完整学习路径。

## 目录结构

```
03-runoob-tutorials/
├── 01-basics/              # 基础篇（3个教程）
│   ├── 00-intro.ipynb               # LangChain 简介
│   ├── 01-env-setup.ipynb          # 环境搭建
│   └── 02-deepseek.ipynb           # 集成 DeepSeek
│
├── 02-agent-core/         # Agent 核心篇（13个教程）
│   ├── 00-first-agent.ipynb         # LangChain Agent
│   ├── 01-init-chat-model.ipynb    # 模型调用
│   ├── 02-model-params.ipynb       # 常用参数
│   ├── 03-model-advanced.ipynb     # Chat Model 高级用法
│   ├── 04-messages.ipynb           # 消息类型
│   ├── 05-tool-basics.ipynb        # @tool 基础
│   ├── 06-tool-advanced.ipynb      # 工具高级特性
│   ├── 07-state-store.ipynb        # 工具访问/状态存储
│   ├── 08-create-agent.ipynb       # create_agent() 函数
│   ├── 09-agent-workflow.ipynb    # Agent 工作流程
│   ├── 10-agent-state.ipynb        # AgentState 状态管理
│   ├── 11-system-prompt.ipynb     # 提示词（System/Dynamic Prompt）
│   └── 12-streaming.ipynb          # 流式输出 Streaming
│
├── 03-middleware/          # 中间件篇（5个教程）
│   ├── 00-middleware-concepts.ipynb # 中间件概念
│   ├── 01-before-after-model.ipynb  # @before_model 与 @after_model
│   ├── 02-wrap-model-call.ipynb    # 模型调用拦截
│   ├── 03-wrap-tool-call.ipynb     # 工具调用拦截
│   └── 04-before-after-agent.ipynb  # @before_agent 与 @after_agent
│
├── 04-memory/              # 对话记忆篇（3个教程）
│   ├── 00-checkpointer.ipynb        # Checkpointer 对话记忆
│   ├── 01-store.ipynb               # Store 跨会话存储
│   └── 02-human-in-the-loop.ipynb   # 人工介入
│
├── 05-multi-agent/         # 多 Agent 篇（1个教程）
│   └── 00-multi-agent.ipynb          # 多 Agent 协作
│
├── 06-rag/                 # RAG 应用篇（6个教程）
│   ├── 00-rag-overview.ipynb        # RAG 概述
│   ├── 01-document-loaders.ipynb   # 文档加载与切分
│   ├── 02-rag-agent.ipynb           # RAG Agent
│   ├── 03-customer-service.ipynb    # 智能客服机器人
│   ├── 04-knowledge-qa.ipynb        # 个人知识库问答系统
│   └── 05-personal-assistant.ipynb   # 多工具个人助手
│
└── 07-engineering/         # 工程化篇（2个教程）
    ├── 00-langsmith.ipynb           # LangSmith 可观测性
    └── 01-error-handling.ipynb      # 错误处理与调试
```

## 教程来源

所有内容基于 [菜鸟教程 RUNOOB - LangChain 教程](https://www.runoob.com/langchain/langchain-tutorial.html)

## 学习路径

1. **基础篇** → 了解 LangChain 是什么，搭建环境，集成 DeepSeek
2. **Agent 核心篇** → 掌握 Agent 开发的核心概念和技能
3. **中间件篇** → 学习如何拦截和控制模型/工具调用
4. **对话记忆篇** → 实现 Agent 的记忆和跨会话存储
5. **多 Agent 篇** → 学习多个 Agent 协作
6. **RAG 应用篇** → 构建检索增强生成应用
7. **工程化篇** → 掌握可观测性和错误处理

## 进度

- [ ] 01-basics/ (0/3)
- [ ] 02-agent-core/ (0/13)
- [ ] 03-middleware/ (0/5)
- [ ] 04-memory/ (0/3)
- [ ] 05-multi-agent/ (0/1)
- [ ] 06-rag/ (0/6)
- [ ] 07-engineering/ (0/2)

**总计：33 个教程，0 个完成**

## 使用说明

每个 Notebook 对应 runoob 网站的一个教程页面，包含：
- 教程内容总结
- 代码示例（使用 DeepSeek 模型）
- 运行结果展示
- 流程图（Mermaid）
- 术语解释

建议按顺序学习，每个目录完成后再进入下一目录。
