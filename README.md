# LangChain 系统化学习

基于 [LangChain 中文文档 v1](https://langchain-doc.cn/v1/python/) 的完整学习路径。

## 学习计划

```mermaid
gantt
    title LangChain 学习路线图
    dateFormat  YYYY-MM-DD
    section 第一阶段 核心组件
    Chat Models & Messages      :a1, 3d
    Prompt Templates & Output   :a2, 2d
    Tools & Structured Output   :a3, 2d
    Streaming & Middleware      :a4, 2d
    section 第二阶段 检索与记忆
    Document Loaders & Splitters :b1, 2d
    Embeddings & VectorStore    :b2, 2d
    Retrieval & RAG             :b3, 3d
    Long-term Memory            :b4, 2d
    section 第三阶段 LangGraph
    StateGraph & Conditional    :c1, 3d
    Subgraphs & Time Travel     :c2, 2d
    Persistence & Checkpoint    :c3, 2d
    Streaming & Interrupts      :c4, 2d
    section 第四阶段 Agent 系统
    Tool Calling Agent          :d1, 2d
    Multi-agent Systems         :d2, 3d
    Human-in-the-Loop           :d3, 2d
    MCP Protocol                :d4, 2d
    section 第五阶段 生产与实战
    Testing & Observability     :e1, 2d
    Deploy & LangGraph Studio   :e2, 2d
    Agentic RAG 实战            :e3, 3d
    SQL Agent 实战              :e4, 3d
```

---

## 第一阶段：核心组件（LangChain Core）

对标官方文档 [LangChain > Overview](https://langchain-doc.cn/v1/python/langchain/overview.html) 和 Core Components。

| 模块 | 内容 | 参考文档 |
|------|------|----------|
| **Chat Models** | 多模型调用、消息体系（System/Human/AI）、多供应商切换 | Models, Messages |
| **Prompt Templates** | 模板变量、FewShot、ChatPromptTemplate | - |
| **Output Parsers** | StrOutputParser、PydanticOutputParser、结构化输出 | Structured Output |
| **Tools** | @tool 装饰器、Tool 类、参数 schema | Tools |
| **Streaming** | 同步/异步流式、事件流 | Streaming |
| **Middleware** | 请求拦截、日志、速率限制 | Middleware |

**练习项目**：多模型对话 CLI

---

## 第二阶段：检索增强生成（RAG）

对标文档的 Retrieval 和长期记忆。

| 模块 | 内容 | 参考文档 |
|------|------|----------|
| **Document Loaders** | PDF/HTML/CSV/Web 加载器 | Retrieval |
| **Text Splitters** | RecursiveCharacter、语义分割 | Retrieval |
| **Embeddings** | OpenAI/TexteEmbedding、自定义 | Retrieval |
| **Vector Stores** | ChromaDB、FAISS、检索策略（MMR/阈值） | Retrieval |
| **RAG Chain** | 上下文压缩、MultiQuery 检索、RAPTOR | Retrieval |
| **Long-term Memory** | 持久化记忆、对话摘要 | Long-term Memory |

**练习项目**：本地 PDF 知识库问答机器人

---

## 第三阶段：LangGraph

对标 [LangGraph 官方文档](https://langchain-doc.cn/v1/python/langgraph/overview.html)。

| 模块 | 内容 | 参考文档 |
|------|------|----------|
| **Graph API** | StateGraph、Node、Edge、条件路由 | Graph API |
| **Functional API** | 函数式编排（轻量） | Functional API |
| **Subgraphs** | 子图组合、嵌套流程 | Subgraphs |
| **Time Travel** | 状态回溯、分支恢复 | Time Travel |
| **Persistence** | Checkpointer、MemorySaver、SQLite/Postgres | Persistence |
| **Streaming** | 节点级流式、自定义事件 | Streaming |
| **Interrupts** | 断点、人工介入点 | Interrupts |

**练习项目**：带人工审核的多步写作工作流

---

## 第四阶段：Agent 系统

对标文档的 Agents、Multi-agent、Human-in-the-Loop、MCP。

| 模块 | 内容 | 参考文档 |
|------|------|----------|
| **Tool Calling Agent** | create_tool_calling_agent、AgentExecutor | Agents |
| **Custom Agent** | 自定义 prompt、工具选择逻辑 | Agents |
| **Multi-agent** | Supervisor、协作模式、竞争模式 | Multi-agent |
| **Human-in-the-Loop** | 审批节点、人工反馈 | Human-in-the-Loop |
| **MCP** | 模型上下文协议、工具发现 | MCP |
| **Guardrails** | 输入/输出守卫、安全边界 | Guardrails |

**练习项目**：多 Agent 协作的研究助手

---

## 第五阶段：生产化与实战

对标文档的 Production、DeepAgents。

| 模块 | 内容 | 参考文档 |
|------|------|----------|
| **Testing** | 单元测试、回归测试、LangSmith 评估 | Test |
| **Observability** | 链路追踪、LangSmith trace | Observability |
| **Deploy** | LangGraph Cloud/Server 部署 | Deploy |
| **Studio** | 可视化调试 | Studio |
| **DeepAgents** | 子Agent、长期记忆、自定义Agent框架 | DeepAgents |
| **Agentic RAG** | 带推理的 RAG 代理 | Agentic RAG |
| **SQL Agent** | 自然语言查库 | SQL Agent |

**实战项目 1**：Agentic RAG 问答系统（PDF + 推理）
**实战项目 2**：自然语言 SQL 查询 Agent

---

## 技术栈

- Python 3.11+（由 UV 管理）
- **模型：DeepSeek**（deepseek-chat / deepseek-reasoner，OpenAI 兼容 API）
- LangChain Core / LangChain-Community 0.3.x
- LangGraph 0.4.x
- LangSmith 0.3.x
- ChromaDB（本地向量数据库）

## 快速开始

```bash
# 配置 UV（确保已安装）
# brew install uv

# 创建虚拟环境并安装依赖
uv sync

# 配置环境变量
cp .env.example .env
# 编辑 .env 填入你的 DEEPSEEK_API_KEY
```

## 启动调试

### 方式一：Jupyter Notebook（推荐学习阶段使用）

适合第一、二、四阶段，逐单元格运行，即时看结果。

```bash
# 启动 Jupyter
uv run jupyter notebook
```
浏览器打开后进入 `notebooks/` 目录，按编号顺序运行。

**调试技巧**：
- `Shift+Enter` 运行当前单元格并跳到下一个
- 在代码单元格末尾不加 `print()`，变量值会自动显示
- 报错时修改代码重新运行即可，不需要重启 Kernel

### 方式二：Python 脚本（适合 LangGraph 和实战）

适合第三、五阶段。

```bash
# 运行 Notebook（用 jupytext 或 uv run python 直接跑 .py 文件）
uv run python scripts/05-langgraph/01-state-graph.py
```

### 验证环境

```python
# 在 Jupyter 或终端中运行
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# DeepSeek 是 OpenAI 兼容 API
llm = ChatOpenAI(
    model="deepseek-chat",
    api_key="sk-your-deepseek-api-key",
    base_url="https://api.deepseek.com",
    temperature=0,
)

print(llm.invoke("Hello!").content)
```

> **注意**：DeepSeek 兼容 OpenAI SDK，所以用 `langchain_openai`/`ChatOpenAI` 包，只需修改 `base_url` 和 `api_key`。
> 模型名：`deepseek-chat` = DeepSeek V3，`deepseek-reasoner` = DeepSeek R1。

### 查看追踪（可选）

开启 LangSmith 后可看到每次调用的完整链路：

```bash
# 1. 去 https://smith.langchain.com 注册获取 API Key
# 2. 填入 .env 的 LANGSMITH_API_KEY
# 3. 开启 tracing
export LANGSMITH_TRACING=true
```

所有 Notebook 和脚本都会自动上报 trace，方便调试。web界面查看：https://smith.langchain.com

---

## 学习建议

1. **按顺序学**：每个阶段依赖前一阶段的概念
2. **边学边写**：每看完一个模块，立刻写代码验证
3. **用 LangSmith 追踪**：所有示例都建议开启 tracing，观察每一步的执行
4. **先 LCEL，再 LangGraph**：LCEL 是基础，LangGraph 是进阶编排

## 参考链接

- [LangChain 中文文档 v1](https://langchain-doc.cn/v1/python/)
- [LangChain 官方文档](https://python.langchain.com/)
- [LangGraph 文档](https://langchain-ai.github.io/langgraph/)
- [LangSmith](https://smith.langchain.com/)
