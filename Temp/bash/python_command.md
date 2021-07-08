# 常用命令

- [一. 规则](#一-规则)
- [二. pip](#二-pip)
  - [2.1. pip --editable](#21-pip---editable)
  - [2.2. pip list or freeze](#22-pip-list-or-freeze)
  - [2.3. pip install](#23-pip-install)
    - [2.3.1. pip install -r requirements.txt](#231-pip-install--r-requirementstxt)
    - [2.3.2. pip install xxx](#232-pip-install-xxx)
- [三. flake8](#三-flake8)
- [四. tox](#四-tox)
  - [4.1. tox --version](#41-tox---version)
  - [4.2. tox --verbose](#42-tox---verbose)
  - [4.3. tox --help](#43-tox---help)
  - [4.4. tox --help-ini](#44-tox---help-ini)
  - [4.5. tox --showconfig](#45-tox---showconfig)
  - [4.6. tox --result-json](#46-tox---result-json)

> 平常工作和生活当中, 需要跨系统, 跨语言, 跨环境, 好多都需要笔录的方式记忆下来(已超出个体记忆能力), 好记性不如烂笔头, 故整理后续参考;

## 一. 规则

1. `./Temp/archives/record/*` 目录下的帮助文档统一格式命名为: `yyyy_MMdd_xyz.txt`;
2. `./Temp/*/*` 目录下的帮助文档统一格式命名为: `python[2|3]_xyz.txt`, 如若`定版`或`定稿`需求, 帮助文档统一格式命名为: `yyyy_python[2|3]_xyz.txt` 或 `yyyy_MMdd_python[2|3]_xyz.txt`;

此规则适用于如下`目录`:

- `./Temp/help/*`
- `./Temp/txt/*`

## 二. pip

### 2.1. pip --editable

```bash
pip2 install -e .
pip3 install -e .
```

### 2.2. pip list or freeze

```bash
# pip list
pip2 list > ./Temp/txt/python2_pip2_list.txt
pip3 list > ./Temp/txt/python3_pip3_list.txt

pip2 list > ./Temp/txt/2021_python2_pip2_list.txt
pip3 list > ./Temp/txt/2021_python3_pip3_list.txt

python2 -m pip list > ./Temp/txt/2021_python2_pip2_list.txt
python3 -m pip list > ./Temp/txt/2021_python3_pip3_list.txt
# pip freeze
pip2 freeze > ./Temp/txt/python2_pip2_freeze.txt
pip3 freeze > ./Temp/txt/python3_pip3_freeze.txt

pip2 freeze > ./Temp/txt/2021_python2_pip2_freeze.txt
pip3 freeze > ./Temp/txt/2021_python3_pip3_freeze.txt

python2 -m pip freeze > ./Temp/txt/2021_python2_pip2_freeze.txt
python3 -m pip freeze > ./Temp/txt/2021_python3_pip3_freeze.txt
```

### 2.3. pip install

#### 2.3.1. pip install -r requirements.txt

```bash
# the base component requirements
pip2 install -r ./requirements.txt
pip3 install -r ./requirements.txt

python2 -m pip install -r ./requirements.txt
python3 -m pip install -r ./requirements.txt

# the base chain component requirements
pip2 install -r ./Temp/archives/material/requirements.txt
pip3 install -r ./Temp/archives/material/requirements.txt

python2 -m pip install -r ./Temp/archives/material/requirements.txt
python3 -m pip install -r ./Temp/archives/material/requirements.txt
```

#### 2.3.2. pip install xxx

```bash
pip2 install xxx
pip3 install xxx
```

## 三. flake8

```bash

flake8 ./src/ > ./Temp/flake8/python2_flake8_recorder.txt
flake8 ./src/ > ./Temp/flake8/python3_flake8_recorder.txt

flake8 --exclude [*.pyc] ./src/
flake8 --exclude [*.pyc] ./src/ > ./Temp/flake8/python2_flake8_recorder.txt
flake8 --exclude [*.pyc] ./src/ > ./Temp/flake8/python3_flake8_recorder.txt

flake8 --help > ./Temp/help/python2_flake8_help.txt
flake8 --help > ./Temp/help/python3_flake8_help.txt
```

## 四. tox

### 4.1. tox --version

```bash
tox --version
```

### 4.2. tox --verbose

```bash
tox --verbose
tox --verbose --parallel all
tox --verbose --parallel auto
tox --verbose --parallel 4  // 4 cpu core
tox --verbose --parallel 8  // 8 cpu core

python2 -m tox --verbose > ./Temp/help/python2_tox_verbose.txt
python3 -m tox --verbose > ./Temp/help/python3_tox_verbose.txt
```

### 4.3. tox --help

```bash
tox --help

python2 -m tox --help > ./Temp/help/python2_tox_help.txt
python3 -m tox --help > ./Temp/help/python3_tox_help.txt
```

### 4.4. tox --help-ini

```bash
tox --help-ini

python2 -m tox --help-ini > ./Temp/help/python2_tox_help_ini.txt
python3 -m tox --help-ini > ./Temp/help/python3_tox_help_ini.txt
```

### 4.5. tox --showconfig

```bash
tox --showconfig

python2 -m tox --showconfig > ./Temp/help/python2_tox_show_config.txt
python3 -m tox --showconfig > ./Temp/help/python3_tox_show_config.txt
```

### 4.6. tox --result-json

```bash
tox --result-json

python2 -m tox --result-json ./Temp/help/python2_tox_result_json.txt
python3 -m tox --result-json ./Temp/help/python3_tox_result_json.txt
```
