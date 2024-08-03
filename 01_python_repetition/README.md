# Python summary 

<!-- [![video](https://github.com/kokchun/assets/blob/025ae8622a25d5522d11b21108f52f1df9388ea2/data_warehouse/snowflake_free_trial.png?raw=true)](https://github.com/kokchun/assets/blob/025ae8622a25d5522d11b21108f52f1df9388ea2/data_warehouse/snowflake_free_trial.png?raw=true) -->

> [!IMPORTANT]
> [LINK TO VIDEO &nbsp; :video_camera:](https://)

In this folder, you'll find jupyter notebooks for summary of different Python concepts starting from fundamentals to object oriented programming. These concepts are useful and prepares you for your continued journey in Python into data processing.

> Study tip: if some programming concepts are unfamiliar to you, make sure to learn it. Concepts are more important than syntax, as the syntax will come the more you write in the language. Make use of lecture notes, LLM and classical googling. 

## Setup 

This setup requires that you have the following prerequisites already setup
- python
- pip 

If you haven't [installed Python](https://www.python.org/downloads/),  install **3.11**, don't install 3.12. Also remember to tick the box: `add to path` in the installation, in order for Python to be properly installed. 

> [!WARNING]
> Don't install several versions of python if you don't have experience in switching between versions, e.g. using pyenv. 

### Virtual environment

We'll be using a virtual environment with the [uv package](https://github.com/astral-sh/uv), which is a package installer and resolver for Python. Start by installing uv globally using this command

```bash
pip install uv
```

> [!NOTE]
> Make sure no virtual environment is activated when running that comamnd in order to install it globally. 


Navigate to your repository and run 

```bash
uv venv 
```
This creates a `.venv`  directory, which stores information of your virtual environment. Now you can activate this venv through 

```bash
# in windows
source .venv/Scripts/activate

# in mac/linux
source .venv/bin/activate
```

> [!NOTE]
> On `windows`, you should use git bash, and not powershell or cmd. You can configure vscode to open git bash as default terminal. 

You will see a paranthesis around your directory name in the terminal when your venv is activated. Now you can install packages without affecting the global installations.


## Other videos :video_camera:

## Read more :eyeglasses: