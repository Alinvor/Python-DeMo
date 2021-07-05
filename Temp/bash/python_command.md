# 常用命令

- [一. pip](#一-pip)
  - [1.1. pip --editable](#11-pip---editable)
  - [1.2. pip list or freeze](#12-pip-list-or-freeze)
  - [1.3. pip install](#13-pip-install)
    - [1.3.1. pip install -r requirements.txt](#131-pip-install--r-requirementstxt)
    - [1.3.2. pip install xxx](#132-pip-install-xxx)
- [二. flake8](#二-flake8)

## 一. pip

### 1.1. pip --editable

```bash
pip2 install -e .
pip3 install -e .
```

### 1.2. pip list or freeze

```bash
# pip list
pip2 list > ./Temp/txt/pip2_list.txt
pip3 list > ./Temp/txt/pip3_list.txt
pip2 list > ./Temp/txt/2021_pip2_list.txt
pip3 list > ./Temp/txt/2021_pip3_list.txt
# pip freeze
pip2 freeze > ./Temp/txt/pip2_freeze.txt
pip3 freeze > ./Temp/txt/pip3_freeze.txt
pip2 freeze > ./Temp/txt/2021_pip2_freeze.txt
pip3 freeze > ./Temp/txt/2021_pip3_freeze.txt
```

### 1.3. pip install

#### 1.3.1. pip install -r requirements.txt

```bash
# the base component requirements
pip2 install -r ./requirements.txt
pip3 install -r ./requirements.txt

# the base chain component requirements
pip2 install -r ./Temp/archives/material/requirements.txt
pip3 install -r ./Temp/archives/material/requirements.txt
```

#### 1.3.2. pip install xxx

```bash
pip2 install xxx
pip3 install xxx
```

## 二. flake8

```bash

flake8 ./src/ > ./Temp/flake8_recorder.txt
flake8 --exclude [*.pyc] ./src/
flake8 --exclude [*.pyc] ./src/ > ./Temp/flake8_recorder.txt
flake8 --help > ./Temp/flake8_help.txt

```
