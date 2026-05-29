from langchain_ollama import ChatOllama


def get_llm():

    llm = ChatOllama(
        model="qwen3:8b",
        temperature=0,
        base_url="http://localhost:11434"
    )

    return llm
    