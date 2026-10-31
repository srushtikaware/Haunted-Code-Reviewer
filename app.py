
import os
import streamlit as st
from huggingface_hub import InferenceClient

# Page configuration
st.set_page_config(
    page_title="Haunted Code Reviewer",
        page_icon="👻",
            layout="centered"
            )

            # Ghost-themed styling
            st.markdown("""
            <style>
            .stApp {
                background: linear-gradient(135deg, #0b1020, #1b1230);
                    color: #e8e8ff;
                    }
                    h1, h2, h3 {
                        color: #c4b5fd !important;
                        }
                        .stButton > button {
                            background-color: #6d28d9;
                                color: white;
                                    border-radius: 10px;
                                        border: none;
                                        }
                                        </style>
                                        """, unsafe_allow_html=True)

                                        # App title
                                        st.title("👻 Haunted Code Reviewer")
                                        st.caption("A ghost in the machine reviews your code...")

                                        # Hugging Face API token
                                        hf_token = os.getenv("HF_TOKEN")

                                        if not hf_token:
                                            st.warning("HF_TOKEN is missing. Set it in your Codespaces secrets.")
                                                st.stop()

                                                # Code input
                                                code = st.text_area(
                                                    "Paste your code here:",
                                                        height=300,
                                                            placeholder="def haunted_function():\n    pass"
                                                            )

                                                            language = st.selectbox(
                                                                "Programming language:",
                                                                    ["Python", "Java", "C++", "JavaScript", "C", "Other"]
                                                                    )

                                                                    # Review button
                                                                    if st.button("👻 Summon the Reviewer"):
                                                                        if not code.strip():
                                                                                st.warning("The spirits need code to inspect!")
                                                                                    else:
                                                                                            with st.spinner("The ghost is examining your code..."):
                                                                                                        try:
                                                                                                                        client = InferenceClient(
                                                                                                                                            model="meta-llama/Llama-3.1-8B-Instruct",
                                                                                                                                                                token=hf_token
                                                                                                                                                                                )

                                                                                                                                                                                                system_prompt = """
                                                                                                                                                                                                                You are Haunted Code Reviewer, a ghost trapped inside a computer.
                                                                                                                                                                                                                                Review the user's code accurately and helpfully.
                                                                                                                                                                                                                                                Identify real bugs, logic errors, security issues, and improvements.
                                                                                                                                                                                                                                                                Explain each issue clearly and suggest fixes.
                                                                                                                                                                                                                                                                                Use a spooky ghostly personality with brief eerie commentary.
                                                                                                                                                                                                                                                                                                Do not invent errors. If the code is correct, say so.
                                                                                                                                                                                                                                                                                                                Keep the review structured and beginner-friendly.
                                                                                                                                                                                                                                                                                                                                """

                                                                                                                                                                                                                                                                                                                                                response = client.chat_completion(
                                                                                                                                                                                                                                                                                                                                                                    messages=[
                                                                                                                                                                                                                                                                                                                                                                                            {"role": "system", "content": system_prompt},
                                                                                                                                                                                                                                                                                                                                                                                                                    {
                                                                                                                                                                                                                                                                                                                                                                                                                                                "role": "user",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            "content": (
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            f"Review this {language} code:\n\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            f"```{language.lower()}\n{code}\n```"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        )
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        max_tokens=700,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            temperature=0.4
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            )

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            review = response.choices[0].message.content

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            st.subheader("📜 The Ghost's Review")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            st.markdown(review)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        except Exception as e:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        st.error(f"The spirits encountered an error: {e}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        