import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env (if present)
load_dotenv()

from src.langgrapg_agentic_ai.ui.streamlit_ui.loadui import LoadStreamlitUI
from src.langgrapg_agentic_ai.LLMS.groqllm import GroqLLM
from src.langgrapg_agentic_ai.LLMS.openai import OpenAILLM
from src.langgrapg_agentic_ai.graph.graph_builder import GrapBuilder
from src.langgrapg_agentic_ai.ui.streamlit_ui.display_result import DisplayResultStreamlit


def load_langgraph_agentiai_app():
    """Loads and runs the LangGraph AgenticAI application with Streamlit UI."""

    ui = LoadStreamlitUI()
    user_input = ui.load_stream_lit_ui()

    if not user_input:
        st.error("Error: Failed to load model not be initialized")
        return

    #TExt input for user
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            selected_llm = (user_input.get("selected_llm") or "").strip().lower()
            if selected_llm == "openai":
                llm_config = OpenAILLM(user_controls_input=user_input)
            else:
                llm_config = GroqLLM(user_controls_input=user_input)

            model = llm_config.get_llm_model()
            if not model:
                st.error("Error: LLM model could not be initialized")
                return

            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("Error: No usecase selected")
                return

            graph_builder = GrapBuilder(model, user_controls_input=user_input)
            graph = graph_builder.setup_graph(usecase)
            DisplayResultStreamlit(usecase=usecase, graph=graph, user_message=user_message).display_result_on_ui()

        except Exception as e:
            st.error(f"Error: Graph set up failed: {e}")
            return