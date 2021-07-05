# 命令

- [一. 删除缓存](#一-删除缓存)
  - [1.1. pyc and pycache](#11-pyc-and-pycache)
  - [1.2. 扩展目录](#12-扩展目录)
- [二. pip](#二-pip)
  - [2.1 pip list or freeze](#21-pip-list-or-freeze)

## 一. 删除缓存

### 1.1. pyc and pycache

```bash
# the delete files
find . -name '*.pyc' -delete
# the delete directory
find . -type d -name __pycache__ -exec rm -r {} +
```

### 1.2. 扩展目录

推荐删除扩展目录:

```bash
find . -type d -name build -exec rm -r {} +
find . -type d -name dist -exec rm -r {} +
find . -type d -name .tox -exec rm -r {} +
```

## 二. pip

### 2.1 pip list or freeze

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
