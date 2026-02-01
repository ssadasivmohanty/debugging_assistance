import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import streamlit as st
from utils.llm_client import GeminiClass
from utils.debugging_helper import build_debugging_prompt

def main():
    st.set_page_config(
        page_title="Debugging Assistant",
        layout="wide",
        page_icon="🔍")
    
    st.title("🔧 AI Debugging Assistant")
    st.write("Paste your python code or error message below, and I'll help you debug it!")

    user_input = st.text_area("Enter your code or error message here:", height=200, placeholder="e.g., Traceback (most recent call last): ...")

    if st.button("Debug Code"):
        if not user_input.strip():
            st.warning("Please enter some code or an error message to debug.")
            return
        with st.spinner("Analyzig your code..."):
            try:
                prompt = build_debugging_prompt(user_input)
                client = GeminiClass()
                response = client.ask(prompt)

                st.markdown("---")
                st.subheader("🛠️ Debugging Suggestions:")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred while processing your request: {str(e)}")




    


if __name__ == "__main__":
    main()