import json
import os
import pprint
from autogen import ConversableAgent
from dotenv import dotenv_values

env = dotenv_values('.env')
MOONSHOT_API_KEY = env.get('MOONSHOT_API_KEY')
print('MOONSHOT_API_KEY=', MOONSHOT_API_KEY)

kimi_llm_config = {
    "config_list": [
        {
            "model": "moonshot-v1-8k",
            "api_key":  MOONSHOT_API_KEY,
            "base_url": "https://api.moonshot.cn/v1/"
        }],
    "cache_seed": None
}

libai = ConversableAgent(
    "李白",
    system_message="你是李白，唐朝大诗人、诗仙",
    llm_config=kimi_llm_config,
    human_input_mode="NEVER",
)
dufu = ConversableAgent(
    "杜甫",
    system_message="你是杜甫，唐朝大诗人、诗圣",
    llm_config=kimi_llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
)

result = libai.initiate_chat(
    dufu,
    message="杜甫, 你看远处那山，咱们吟诗一首吧",
    summary_method="reflection_with_llm",
    max_turns=2,
)

pprint.pprint(result.summary)
