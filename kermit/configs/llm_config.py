from typing import Optional
import yaml
from enum import Enum
from kermit.configs.yaml_model import YamlModel


class LLMType(Enum):
    OPENAI = "openai"

    def __missing__(self, key):
        return self.OPENAI

class LLMConfig(YamlModel):
    api_key: str = "sk-"
    api_type: LLMType = LLMType.OPENAI
    base_url: str = "https://api.openai.com/v1"
    api_version: Optional[str] = None

    model: Optional[str] = None  # also stands for DEPLOYMENT_NAME
    pricing_plan: Optional[str] = None  # Cost Settlement Plan Parameters.
