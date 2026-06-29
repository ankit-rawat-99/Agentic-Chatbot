import os
import streamlit as st
from langchain_openai import ChatOpenAI

class OpenAILLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            openai_api_key = self.user_controls_input.get("OPENAI_API_KEY", "")
            selected_openai_model = (
                self.user_controls_input.get("selected_openai_model")
                or os.environ.get("OPENAI_MODEL")
                or "gpt-4.1-nano"
            )

            # Check user input key first, then fall back to environment variables
            if not openai_api_key and not os.environ.get("OPENAI_API_KEY"):
                st.error("Please enter the OpenAI API KEY")
                st.stop()

            # Initialize the model with user input key or environment variable fallback
            llm = ChatOpenAI(
                api_key=openai_api_key or os.environ.get("OPENAI_API_KEY"), 
                model=selected_openai_model
            )

        except Exception as e:
            raise ValueError(f"Error occurred with Exception: {e}")
            
        return llm
