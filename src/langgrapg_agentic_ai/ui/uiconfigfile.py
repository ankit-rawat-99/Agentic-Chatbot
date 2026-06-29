##To read .ini file
from configparser import ConfigParser

class Config:
    ## when the obj is called it will read the config file
    def __init__(self,config_file="./src/langgrapg_agentic_ai/ui/uiconfigfile.ini"):
        self.config=ConfigParser()
        self.config.read(config_file)

    
    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")

    def get_openai_model_options(self):
        raw_value = (
            self.config["DEFAULT"].get("OPENAI_MODEL_OPTIONS")
            or self.config["DEFAULT"].get("OPEN_AI_MODEL")
            or "gpt-4.1-mini"
        )
        return [model.strip() for model in raw_value.split(",") if model.strip()]
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")