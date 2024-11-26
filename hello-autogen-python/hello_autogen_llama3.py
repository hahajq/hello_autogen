import pprint
from autogen import ConversableAgent

config_list = [
    {
        "model": "llama3.2",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",
    }
]
local_llm_config = {"config_list": config_list}

student = ConversableAgent(
    "student",
    system_message="你是一名高中生",
    llm_config=local_llm_config,
    human_input_mode="NEVER",
)
teacher = ConversableAgent(
    "teacher",
    system_message="你是一名数学老师",
    llm_config=local_llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
)

result = teacher.initiate_chat(
    student,
    message="什么是三角不等式",
    summary_method="reflection_with_llm",
    max_turns=4,
)

pprint.pprint(result.summary)
pprint.pprint(result.chat_history)
pprint.pprint(result.cost)
