import streamlit as st
import os

from src.langgrapg_agentic_ai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_stream_lit_ui(self):
        st.set_page_config(page_title=" 🤖 " + self.config.get_page_title(), layout="wide")
        st.header(" 🤖 " + self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked =False

        with st.sidebar:
            #get option form config
            llm_options=self.config.get_llm_options()
            usercase_option=self.config.get_usecase_options()

            #LLm selection 
            self.user_controls["selected_llm"]=st.selectbox("Select LLM",llm_options)
            selected_llm = self.user_controls["selected_llm"].strip().lower()

            if selected_llm == 'groq':
                # Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"]=st.text_input("API Key",type="password")
                # Validate API key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning(" ⚠ Please enter your GROQ API key to proceed. Don't have? refer : https://groq.com ")

            elif selected_llm == 'openai':
                # Model selection for OpenAI
                model_options = self.config.get_openai_model_options()
                self.user_controls["selected_openai_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["OPENAI_API_KEY"] = st.session_state["OPENAI_API_KEY"] = st.text_input("OpenAI API Key", type="password")
                
                # Validate OpenAI API key
                if not self.user_controls["OPENAI_API_KEY"]:
                    st.warning(" ⚠ Please enter your OpenAI API key to proceed. Don't have? refer: https://openai.com ")

            ##use Case Selection
            self.user_controls["selected_usecase"]=st.selectbox("Select Usecase",usercase_option)

            if self.user_controls["selected_usecase"] == "Chatbot with Web" or  self.user_controls["selected_usecase"] == "AI News":
              self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("TAVILY API KEY", type="password")

              # Validate API key
              if not self.user_controls["TAVILY_API_KEY"]:
                  st.warning("⚠️ Please enter your TAVILY_API_KEY key to proceed. Don't have? refer : https://tavily.com")

                  with st.sidebar:
                    time_frame = st.selectbox(
                        "📅 Select Time Frame",
                        ["Daily", "Weekly", "Monthly"],
                        index=0
                    )
                  if st.button("🔍 Fetch Latest AI News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeframe = time_frame


        return self.user_controls