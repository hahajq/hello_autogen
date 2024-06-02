# autogen

<https://microsoft.github.io/autogen/docs/tutorial/introduction>

- The whole is greater than the sum of its parts.
- -Aristotle

## install

```sh
python -m venv autogen_env
# git bash
source autogen_env/Scripts/activate
# cmd
.\autogen_env\Scripts\activate.bat
# powershell
.\autogen_env\Scripts\activate.ps1

which python
```

```sh
python -m pip install --upgrade pip
# Python version >= 3.8, < 3.13
pip install pyautogen
pip install litellm[proxy]
pip install python-dotenv
```

## run

### run with local llm

#### pull LLM

<https://microsoft.github.io/autogen/docs/topics/non-openai-models/local-litellm-ollama>

```sh
ollama pull llama3
ollama list
```

#### start LLM APIs using the OpenAI

- <https://www.litellm.ai/>
- <https://github.com/BerriAI/litellm>

```sh
litellm --model ollama_chat/llama3
```

```sh
python hello_autogen_llama3.py
```

#### result

### run with moonshot

```sh
# https://platform.moonshot.cn/console/api-keys
echo "MOONSHOT_API_KEY=" > .env

python hello_autogen_moonshot.py
```
