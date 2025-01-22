# Github actions for CI

TOOD: video

<!-- <a href="https://youtu.be/3_ZZ80Symjc" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/python_videos/packaging.png?raw=true" alt="course structure" width="600">
</a> -->

In this continous integration (CI) with github actions, we'll configure a few tools to run for automatically linting our code. The purpose for this is to make sure that the whole team has the same formatting so that you don't code review code changes that are only formatting and instead code review on actual changes. 

For simplicity we'll just use linting however CI can be used to run automatic unit testing before pushing or pull request. 

## Setup configurations 

Install the following linting and formatting packages to your virtual environment

```bash
uv pip install flake8 black
```

Now create a folder called `.github` and inside that folder create `workflows` folder. Inside the workflows folder, create a file called `ci.yml`, here is the CI code that you will write that will be run automatically on a trigger event e.g. a push or a pull request. 

## ci.yml 

The ci.yml file should contain 

```yml

name: Python project CI

on:
  pull_request:
    branches:
      - main

jobs:
  lint:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v5.3.0
        with:
          python-version: 3.11
 
      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run flake8
        run: flake8 .

      - name: Run black
        run: black --check .
```

This will create an environment with ubuntu, checkouts your code in your repo and setup python with dependencies in your requirements.txt when you do pull requesting to main. Then it will run flake8 to check linting on all your python scripts and it will check that your scripts are formatted according to black. All the steps will be run in order and the uses will take an existing action in the marketplace, while run will run a command in the command line. 

Go into repository setting in github and under branch protection rule, add one to protect the main branch with `require status checks to pass before merging`. Also search for lint in status checks required.

<img src="https://github.com/kokchun/assets/blob/main/ci_cd/ci_merge_protect.png?raw=true" alt="protection branch rule" width="600">

Now when merging if any of the steps fails, it won't let you merge.


## pre-commit hooks

It is good to protect pull request with CI but can we automate these fixes before committing the code at all. Yes with pre-commit, we can add hooks that will check the code when committing, and if they fail, it won't let you commit. This forces you to fix them before committing. So install pre-commit

```bash
uv pip install pre-commit
```

Then create this `.pre-commit-config.yaml` in the root of your repo and add the following code

```yaml
repos:
  # formatting according to PEP8 style
  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black

  # linting - style and checks 
  - repo: https://github.com/PyCQA/flake8
    rev: 6.1.0 
    hooks:
      - id: flake8 
        args: ["--max-line-length=88"]

  # sorts imports automatically
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: ["--profile", "black"]  
```

This will check black, flake8 and sort your packages automatically before committing the code. 


## Marketplace

To find predefined actions go into [github actions marketplace](https://github.com/marketplace?type=actions) to find different predefined actions and how to use them in your CI/CD pipelines.

For example we find setup-python in the market place.

<img src="https://github.com/kokchun/assets/blob/main/ci_cd/marketplace.png?raw=true" alt="marketplace" width="300">

You can see here how to use this action.

<img src="https://github.com/kokchun/assets/blob/main/ci_cd/setup_python_action.png?raw=true" alt="marketplace" width="400">