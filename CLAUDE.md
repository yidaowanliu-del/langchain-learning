# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

LangChain 系统化学习项目，从核心概念到 Agent 系统实战。基于 LangChain v1 中文文档。

## 技术栈

- Python 3.11+，依赖由 UV 管理
- 模型：DeepSeek（OpenAI 兼容 API），通过 `langchain_openai.ChatOpenAI` 调用
- LangChain 0.3.x / LangGraph 0.4.x / LangSmith 0.3.x
- ChromaDB 本地向量数据库
- 代码格式：ruff
- Notebook：Jupyter (.ipynb)，推荐 VS Code 直接打开

## 常用命令

```bash
# 安装依赖
uv sync

# 安装可编辑包（Notebook 导入需要）
uv pip install -e .

# 运行 Notebook（VS Code 直接打开 .ipynb 文件）
# 或通过 Jupyter 服务：
uv run jupyter notebook

# 运行 Python 脚本
uv run python scripts/05-langgraph/<script>.py

# 代码格式化
uv run ruff check --fix src/
```

## 关键架构

### 包结构 (`src/langchain_learning/`)

- `llm.py` — 提供 `get_llm()` 统一获取 LLM 实例，默认 DeepSeek V3
  - `model="deepseek-chat"` = DeepSeek V3
  - `model="deepseek-reasoner"` = DeepSeek R1（推理模型）
- Notebook 中通过 `from langchain_learning.llm import get_llm` 导入

### Notebook 规范

- 存放于 `notebooks/`，按阶段分目录（`01-core-concepts/`）
- 每个代码 cell 下方有 markdown 说明，以 **术语：** 开头解释专业名词
- 流程图使用 Mermaid 语法写在 markdown cell 中（不要用代码 cell）
- 变量占位符用 `{role}` 和 `{question}` 格式模板

### 环境变量

复制 `.env.example` 为 `.env`，配置：
- `DEEPSEEK_API_KEY` — 必需，主模型 API Key
- `LANGSMITH_*` — 可选，链路追踪
