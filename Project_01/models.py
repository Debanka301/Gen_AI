from typing import List, Literal

from pydantic import BaseModel, Field


class ProductReview(BaseModel):

    product_name: str = Field(
        description="Name of the product mentioned in the review"
    )

    rating: int = Field(
        description="Customer rating from 1 to 5",
        ge=1,
        le=5
    )

    sentiment: Literal[
        "positive",
        "negative",
        "neutral",
        "mixed"
    ] = Field(
        description="Overall sentiment of the customer review"
    )

    summary: str = Field(
        description="Short summary of the customer review"
    )

    pros: List[str] = Field(
        description="Positive aspects of the product mentioned by the customer"
    )

    cons: List[str] = Field(
        description="Negative aspects of the product mentioned by the customer"
    )

    mentioned_features: List[str] = Field(
        description="Important product features mentioned in the review"
    )

    purchase_recommendation: bool = Field(
        description="Whether the customer recommends purchasing the product"
    )