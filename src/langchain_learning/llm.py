"""LLM 初始化工具 — 默认使用 DeepSeek"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def get_llm(
    model: str = "deepseek-chat",
    temperature: float = 0,
    **kwargs,
) -> ChatOpenAI:
    """获取 DeepSeek LLM 实例

    Args:
        model: deepseek-chat(V3) 或 deepseek-reasoner(R1)
        temperature: 生成温度 0-2
    """
    return ChatOpenAI(
        model=model,
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com",
        temperature=temperature,
        **kwargs,
    )


__all__ = ["get_llm"]
