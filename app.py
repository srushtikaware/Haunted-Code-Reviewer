import os
import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(
    page_title="Haunted Code Reviewer",
    page_icon="👻",
    layout="centered"
)

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

st.title("👻 Haunted Code Reviewer")
st.caption("A ghost in the machine reviews your code...")

hf_token = os.getenv("HF_TOKEN")

if not hf_token:
    st.warning("HF_TOKEN is missing. Add it in your app's Secrets.")
    st.stop()

code = st.text_area(
    "Paste your code here:",
    height=300,
    placeholder="def haunted_function():\n    pass"
)

language = st.selectbox(
    "Programming language:",
    ["Python", "Java", "C++", "JavaScript", "C", "Other"]
)

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

                response = client.chat_completion(
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a ghostly code reviewer. "
                                "Find real bugs, logic errors, security "
                                "issues, and improvements. Explain fixes "
                                "clearly with brief spooky commentary. "
                                "Do not invent errors. Be beginner-friendly."
                            )
                        },
                        {
                            "role": "user",
                            "content": (
                                f"Review this {language} code:\n"
                                f"```{language.lower()}\n{code}\n```"
                            )
                        }
                    ],
                    max_tokens=700,
                    temperature=0.4
                )

                st.subheader("📜 The Ghost's Review")
                st.markdown(response.choices[0].message.content)

            except Exception as e:
                st.error(f"The spirits encountered an error: {e}")
