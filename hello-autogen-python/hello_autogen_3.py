import os
from autogen import UserProxyAgent,AssistantAgent,GroupChat,GroupChatManager
os.environ['AUTOGEN_USE_DOCKER']='no'
llm_config = {
    "config_list": [
        {
            "model": "NotRequired",  # Loaded with LiteLLM command
            "api_key": "NotRequired",  # Not needed
            "base_url": "http://localhost:4000"  # Your LiteLLM URL
        }
    ],
    "cache_seed": None  # Turns off caching, useful for testing different models
}
user_proxy=UserProxyAgent(
    name="User_proxy",
system_message="A human admin.",
code_execution_config={"last_n_messages":2,"work_dir":"groupchat"},
human_input_mode="NEVER"
)
doris = AssistantAgent(
name="Doris",
system_message="你是语言学家",
llm_config=llm_config,
)
mavis = AssistantAgent(
name="Mavis",
system_message="你是历史学家",
llm_config=llm_config,
)
cara =AssistantAgent(
name="Cara",
system_message="你是周游世界，熟悉各个国家人文的旅行家",
llm_config=llm_config
)
eric = AssistantAgent(
name="Eric",
system_message="你是专栏编辑，你负责对其他人的发言进行总结",
llm_config=llm_config,
)
groupchat = GroupChat(
agents=[user_proxy, doris, mavis, cara, eric],
messages=[],
max_round=12
)
manager = GroupChatManager(groupchat=groupchat,llm_config=llm_config)
user_proxy.initiate_chat(manager,messag="写一篇关于法语的形成的科普文章")