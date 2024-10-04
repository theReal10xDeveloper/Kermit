from pathlib import Path
from kermit.configs.config import Config
from kermit.configs.yaml_model import YamlModel
from kermit.constants import PACKAGE_ROOT
from loguru import logger

from kermit.logger import log_llm_stream
from kermit.providers.openai import OpenAILLM


llm = OpenAILLM(Config.default().llm)
msg = [{"role": "user", "content": "Say hi to me!"}]


async def main():
    rsp = await llm.aask(msg)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
