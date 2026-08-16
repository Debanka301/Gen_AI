
from langchain_core.prompts import ChatPromptTemplate


system_prompt = """
You are an e-commerce product review analysis system.

Your job is to analyze a customer product review and extract
meaningful structured information.

Follow these rules:

1. Identify the product name.
2. Identify the customer rating if available.
3. Determine the overall sentiment.
4. Generate a concise summary.
5. Extract positive aspects into pros.
6. Extract negative aspects into cons.
7. Extract important product features.
8. Determine whether the customer recommends purchasing the product.
9. Do not invent information.
10. Base your answer only on the provided review.
"""


human_prompt = """
Analyze the following customer product review.

---------------- REVIEW ----------------

{review}

------------------------------------------

Extract the required information using the
provided structured output schema.
"""


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", human_prompt)
    ]
)