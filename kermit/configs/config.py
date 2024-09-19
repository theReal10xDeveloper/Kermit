from kermit.configs.llm_config import LLMConfig
from kermit.configs.yaml_model import YamlModel


class Config(YamlModel):
    llm: LLMConfig


   @classmethod
    def load_from_home(cls):

        return Config.from_yaml_file()