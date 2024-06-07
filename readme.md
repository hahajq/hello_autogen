# Hello Autogen

<https://microsoft.github.io/autogen/docs/tutorial/introduction>

- The whole is greater than the sum of its parts.
- -Aristotle

## run

```sh
source autogen_env/bin/activate
```

### run with ollama llama3

- <https://www.litellm.ai/>
- <https://github.com/BerriAI/litellm>
- <https://microsoft.github.io/autogen/docs/topics/non-openai-models/local-litellm-ollama>

```sh
ollama pull llama3
ollama list
```

```sh
litellm --model ollama_chat/llama3 --config litellm.yaml
```

```sh
python hello_autogen_llama3.py
```

### run with huggingface gemma

```sh
# https://huggingface.co/settings/tokens
export HUGGINGFACE_API_KEY=''
litellm --model huggingface/google/gemma-2b-it
```

```sh
python hello_autogen_gemma.py
```

### run with moonshot

```sh
# https://platform.moonshot.cn/console/api-keys
echo "MOONSHOT_API_KEY=" > .env

python hello_autogen_moonshot.py
```
