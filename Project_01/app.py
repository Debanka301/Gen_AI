import streamlit as st

from main import analyze_review


# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="E-commerce Review Analyzer",
    page_icon="🛍️",
    layout="wide"
)


# -------------------------------
# Header
# -------------------------------

st.title("🛍️ E-commerce Product Review Analyzer")

st.write(
    """
    Analyze an unstructured customer review using
    **Ollama + Llama 3.2 + LangChain + Pydantic**
    and generate a structured JSON payload.
    """
)


# -------------------------------
# Sample Review
# -------------------------------

sample_review = """
I bought the Samsung Galaxy S25 Ultra about a month ago,
and overall I am very impressed with the phone.

The display is excellent, with sharp colors and a smooth
120Hz refresh rate.

The camera takes fantastic photos during the day,
and the zoom quality is also very good.

Performance is extremely fast, even when running multiple
applications and playing demanding games.

The battery easily lasts a full day with normal usage,
although it drains faster when gaming or recording videos.

The phone feels premium and well-built, but it is quite
heavy and difficult to use comfortably with one hand.

I also think the price is a little high compared to some
competing phones.

The speakers are loud and clear, and the fingerprint sensor
works quickly.

Overall, I am happy with my purchase and would recommend
this phone to someone looking for a premium Android smartphone.

I would give it 4.5 out of 5 stars.
"""


# -------------------------------
# Input
# -------------------------------

review = st.text_area(
    "Enter Customer Review",
    value=sample_review,
    height=300,
    placeholder="Paste a customer product review here..."
)


# -------------------------------
# Analyze Button
# -------------------------------

if st.button(
    "🔍 Analyze Review",
    type="primary"
):

    if not review.strip():

        st.warning(
            "Please enter a product review."
        )

    else:

        with st.spinner(
            "Analyzing review using Llama 3.2..."
        ):

            try:

                result = analyze_review(review)

                st.success(
                    "Review analyzed successfully!"
                )

                # -------------------------------
                # Product Information
                # -------------------------------

                st.subheader(
                    "📱 Product Information"
                )

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Product",
                        result.product_name
                    )

                with col2:

                    st.metric(
                        "Rating",
                        f"{result.rating}/5"
                    )

                with col3:

                    st.metric(
                        "Sentiment",
                        result.sentiment.upper()
                    )

                # -------------------------------
                # Summary
                # -------------------------------

                st.subheader("📝 Summary")

                st.write(
                    result.summary
                )

                # -------------------------------
                # Pros & Cons
                # -------------------------------

                col1, col2 = st.columns(2)

                with col1:

                    st.subheader("👍 Pros")

                    for pro in result.pros:

                        st.write(
                            f"• {pro}"
                        )

                with col2:

                    st.subheader("👎 Cons")

                    for con in result.cons:

                        st.write(
                            f"• {con}"
                        )

                # -------------------------------
                # Features
                # -------------------------------

                st.subheader(
                    "⚙️ Mentioned Features"
                )

                for feature in result.mentioned_features:

                    st.write(
                        f"• {feature}"
                    )

                # -------------------------------
                # Recommendation
                # -------------------------------

                st.subheader(
                    "🛒 Purchase Recommendation"
                )

                if result.purchase_recommendation:

                    st.success(
                        "The customer recommends purchasing this product."
                    )

                else:

                    st.error(
                        "The customer does not recommend purchasing this product."
                    )

                # -------------------------------
                # JSON Payload
                # -------------------------------

                st.subheader(
                    "📦 Generated JSON Payload"
                )

                json_payload = result.model_dump()

                st.json(
                    json_payload
                )

                # -------------------------------
                # Download JSON
                # -------------------------------

                import json

                json_string = json.dumps(
                    json_payload,
                    indent=2
                )

                st.download_button(
                    label="⬇️ Download JSON",
                    data=json_string,
                    file_name="product_review.json",
                    mime="application/json"
                )

            except Exception as e:

                st.error(
                    f"Error while analyzing review: {e}"
                )