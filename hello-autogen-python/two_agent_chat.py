import pprint
from autogen import ConversableAgent, UserProxyAgent,AssistantAgent
import autogen
local_llm_config = {
    "config_list": [
        {
            "model": "NotRequired",  # Loaded with LiteLLM command
            "api_key": "NotRequired",  # Not needed
            "base_url": "http://127.0.0.1:4000" # Your LiteLLM URL
        }
    ],
    "cache_seed": None,  # Turns off caching, useful for testing different models
}

student_agent = ConversableAgent(
    name="Student_Agent",
    system_message="You are a student willing to learn.",
    llm_config=local_llm_config,
)
teacher_agent = ConversableAgent(
    name="Teacher_Agent",
    system_message="You are a math teacher.",
    llm_config=local_llm_config,
)

chat_result = student_agent.initiate_chat(
    teacher_agent,
    #三角不等式
    message="What is triangle inequality?",
    summary_method="reflection_with_llm",
    max_turns=2,
)
pprint.pprint(chat_result.chat_history)
