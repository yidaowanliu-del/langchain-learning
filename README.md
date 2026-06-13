# LangChain 系统化学习

基于 [LangChain 中文文档 v1](https://langchain-doc.cn/v1/python/) 的完整学习路径，从核心概念到 Agent 系统实战。

## 目录

- [学习计划](#学习计划)
- [项目结构](#项目结构)
- [快速开始](#快速开始)
- [VS Code 配置详解](#vs-code-配置详解)
- [启动调试](#启动调试)
- [Notebook 说明](#notebook-说明)
- [常见问题](#常见问题)
- [学习建议](#学习建议)
- [参考链接](#参考链接)

---

## 学习计划

```
第一阶段 ────────────────────── 约 9 天
    Chat Models & Messages         ████████████████ 3d
    Prompt Templates & Output      ██████████       2d
    Tools & Structured Output      ██████████       2d
    Streaming & Middleware         ██████████       2d

第二阶段 ────────────────────── 约 9 天
    Document Loaders & Splitters   ██████████       2d
    Embeddings & VectorStore       ██████████       2d
    Retrieval & RAG                ████████████████ 3d
    Long-term Memory               ██████████       2d

第三阶段 ────────────────────── 约 9 天
    StateGraph & Conditional       ████████████████ 3d
    Subgraphs & Time Travel        ██████████       2d
    Persistence & Checkpoint       ██████████       2d
    Streaming & Interrupts         ██████████       2d

第四阶段 ────────────────────── 约 9 天
    Tool Calling Agent             ██████████       2d
    Multi-agent Systems            ████████████████ 3d
    Human-in-the-Loop              ██████████       2d
    MCP Protocol                   ██████████       2d

第五阶段 ────────────────────── 约 10 天
    Testing & Observability        ██████████       2d
    Deploy & LangGraph Studio      ██████████       2d
    Agentic RAG 实战               ████████████████ 3d
    SQL Agent 实战                 ████████████████ 3d
```

---

## 项目结构

```
langchain-learning/
├── notebooks/                  # Jupyter Notebook（主学习入口）
│   └── 01-core-concepts/       # 第一阶段：核心组件
│       ├── 01-chat-models.ipynb       # Chat Models 消息体系
│       ├── 02-prompt-parsers.ipynb    # Prompt 模板与输出解析器
│       ├── 03-lcel.ipynb              # LCEL 表达式语言
│       ├── 04-tools.ipynb             # 工具定义与调用
│       ├── 05-streaming.ipynb         # 流式输出与事件流
│       ├── 06-middleware.ipynb        # 中间件与回调
│       └── 07-agent.ipynb            # create_agent 智能体
├── src/
│   └── langchain_learning/     # 项目工具包（已安装为可编辑包）
│       ├── __init__.py
│       └── llm.py              # get_llm() 统一获取 LLM 实例
├── scripts/                    # Python 脚本（适合 LangGraph 等复杂场景）
├── .env                        # API Key 配置文件（不要提交到 git）
├── .env.example                # 环境变量模板
├── pyproject.toml              # 项目配置与依赖
└── README.md
```

---

## 快速开始

### 前置要求

- Python 3.12+
- [UV](https://docs.astral.sh/uv/)（推荐）或 pip

### 安装步骤

```bash
# 1. 克隆项目
git clone <repo-url>
cd langchain-learning

# 2. 创建虚拟环境并安装依赖
uv sync

# 3. 将项目安装为可编辑包（关键！否则 Notebook 无法导入）
uv pip install -e .

# 4. 配置环境变量
cp .env.example .env
# 编辑 .env 填入你的 DEEPSEEK_API_KEY
```

> **注意**：第 3 步 `uv pip install -e .` 是必须的，否则 Notebook 中 `from langchain_learning.llm import get_llm` 会报 `ModuleNotFoundError`。

---

## VS Code 配置详解

本项目使用 Jupyter Notebook（`.ipynb`），**推荐使用 VS Code 打开**，无需单独启动 Jupyter 服务。

### 第一步：在 VS Code 中打开项目

```bash
# 终端中进入项目目录
cd langchain-learning
code .
```

### 第二步：选择 Python 解释器（关键！）

VS Code 需要知道使用哪个 Python 环境（.venv 还是系统 Python）：

**方法 A：通过命令面板设置（推荐，全局生效）**

1. 按 `Cmd+Shift+P` 打开命令面板
2. 输入并选择 **`Python: Select Interpreter`**
3. 从列表中选择 **`.venv/bin/python`**（路径包含 `.venv` 的那个）
4. 如果没有出现，选择 **`Enter interpreter path`** → 手动输入 `./.venv/bin/python`

**方法 B：通过 Notebook 内核选择（仅对当前文件生效）**

1. 打开任意 `.ipynb` 文件
2. 点击编辑器右上角的 **内核名称**（可能显示 "Python 3.x"）
3. 选择 **`.venv`** 对应的 Python 环境

### 第三步：验证配置

打开 `notebooks/01-core-concepts/01-chat-models.ipynb`，运行第一个代码单元格：

```python
from langchain_learning.llm import get_llm
llm = get_llm()
```

如果输出 **没有报错**，说明环境配置成功。

---

## 启动调试

### 方式一：VS Code（推荐）

直接打开 `.ipynb` 文件，点击单元格左侧的 ▶ 运行按钮，或按 `Shift+Enter`。

**快捷键**：
- `Shift+Enter` — 运行当前单元格并跳到下一个
- `Ctrl+Enter` — 运行当前单元格并停留在原地
- `Option+Enter` — 运行当前单元格并在下方插入新单元格

### 方式二：Jupyter Notebook 服务

```bash
# 启动 Jupyter
uv run jupyter notebook
```

浏览器打开后进入 `notebooks/` 目录，按编号顺序运行。

### 方式三：Python 脚本

适合第三、五阶段。

```bash
uv run python scripts/05-langgraph/01-state-graph.py
```

---

## Notebook 说明

### 代码单元格

每个 Notebook 包含三种类型的单元格：

| 类型 | 说明 |
|------|------|
| **代码单元格** | 可执行的 Python 代码，点击 ▶ 运行 |
| **Markdown（标题）** | `###` 开头的章节标题 |
| **Markdown（说明）** | 含 **术语：** 标签的解释文字，含代码示例和 Mermaid 流程图 |

### 术语说明

每个代码单元格下方有一段以 **术语：** 开头的解释，对初学者友好，例如：

> **术语：**
> - **LLM** = Large Language Model（大语言模型），如 ChatGPT、DeepSeek
> - **invoke** = "调用"，让 LLM 处理输入并返回结果
> - **.content** = LLM 返回的消息对象中的文本内容

### Mermaid 流程图

部分说明包含 Mermaid 图表（如 LCEL 链式调用流程图），VS Code 可以直接渲染显示。

---

## 常见问题

### 1. `ModuleNotFoundError: No module named 'src'`

**原因**：导入路径用了 `src.langchain_learning`，应改为 `langchain_learning`。

**解决**：
```bash
uv pip install -e .    # 确保包已安装
```
然后在代码中将 `from src.langchain_learning` 改为 `from langchain_learning`。

### 2. 无法解析导入 "langchain_core"

**原因**：VS Code 使用了系统 Python（未安装 langchain），而不是项目的 `.venv`。

**解决**：按上方 [VS Code 配置详解](#vs-code-配置详解) 的步骤选择 `.venv/bin/python` 作为解释器。

### 3. LangChainDeprecationWarning（pydantic v1）

```
LangChainDeprecationWarning: As of langchain-core 0.3.0, LangChain uses pydantic v2 internally.
```

**原因**：代码中使用了 `from langchain_core.pydantic_v1 import ...`。

**解决**：将导入改为 `from pydantic import BaseModel, Field`（已修复）。

### 4. LangSmith 403 Forbidden 错误

```
Failed to POST https://api.smith.langchain.com/runs/multipart
HTTPError('403 Client Error: Forbidden')
```

**原因**：`LANGSMITH_API_KEY` 无效或未配置，但 LLM 调用本身不受影响。

**解决**（任选一种）：
- 去 [smith.langchain.com](https://smith.langchain.com) 获取有效 API Key 填入 `.env`
- 或关闭追踪：`.env` 中设置 `LANGSMITH_TRACING=false`

### 5. VS Code 中 Notebook 内核一直显示 "连接中"

**原因**：Jupyter 内核启动超时或 Python 解释器路径不对。

**解决**：
1. 重启 VS Code
2. `Cmd+Shift+P` → `Developer: Reload Window`
3. 重新选择解释器：`Cmd+Shift+P` → `Python: Select Interpreter` → `.venv/bin/python`

---

## 学习建议

1. **按顺序学**：每个阶段依赖前一阶段的概念
2. **边学边写**：每看完一个模块，立刻写代码验证
3. **术语优先**：每个 Notebook 都标注了关键术语，先理解术语再看代码
4. **先 LCEL，再 LangGraph**：LCEL 是基础，LangGraph 是进阶编排
5. **有问题先看常见问题**：大部分环境问题在上方都有说明

## 参考链接

- [LangChain 中文文档 v1](https://langchain-doc.cn/v1/python/)
- [LangChain 官方文档](https://python.langchain.com/)
- [LangGraph 文档](https://langchain-ai.github.io/langgraph/)
- [LangSmith](https://smith.langchain.com/)
- [DeepSeek 平台](https://platform.deepseek.com/)
