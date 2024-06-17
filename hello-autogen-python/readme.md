# autogen

## install

```sh
python -m venv autogen_env
# macos
source autogen_env/bin/activate
# windows(git bash)
source autogen_env/Scripts/activate
# windows(cmd)
.\autogen_env\Scripts\activate.bat
# windows(powershell)
.\autogen_env\Scripts\activate.ps1

which python
```

```sh
python -m pip install --upgrade pip
# Python version >= 3.8, < 3.13
pip install pyautogen
pip install python-dotenv
pip install "litellm[proxy]"
```
