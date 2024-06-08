import os
import pprint
from autogen import ConversableAgent

local_llm_config = {
    "config_list": [
        {
            "model": "NotRequired",  # Loaded with LiteLLM command
            "api_key": "NotRequired",  # Not needed
            "base_url": "http://localhost:4000"  # Your LiteLLM URL
        }
    ],
    "cache_seed": None  # Turns off caching, useful for testing different models
}


student = ConversableAgent(
    "student",
    system_message="你是一名语言学研究生",
    llm_config=local_llm_config,
    human_input_mode="NEVER",
)
teacher = ConversableAgent(
    "teacher",
    system_message="你是一名语言学老师",
    llm_config=local_llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
)

result = teacher.initiate_chat(
    student,
    message="欧洲的书写体系有哪些",
    summary_method="reflection_with_llm",
    max_turns=4,
)

pprint.pprint(result.summary)
pprint.pprint(result.chat_history)
pprint.pprint(result.cost)
