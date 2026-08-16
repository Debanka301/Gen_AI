from langchain_ollama import ChatOllama

from models import ProductReview
from prompts import prompt


def analyze_review(review: str) -> ProductReview:

    llm = ChatOllama(
        model="llama3.2",
        temperature=0
    )

    structured_llm = llm.with_structured_output(
        ProductReview
    )

    chain = prompt | structured_llm

    result = chain.invoke({
        "review": review
    })

    return result