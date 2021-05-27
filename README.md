# Python-DeMo

![Python Logo](https://www.python.org/static/community_logos/python-logo.png "Python DeMo")

- [一. 构建`venv`环境](#一-构建venv环境)
  - [1.1 venv2](#11-venv2)
    - [1.1.1 venv2 for mac](#111-venv2-for-mac)
      - [1.1.1.1 venv2 16.7.5](#1111-venv2-1675)
      - [1.1.1.2 venv2 20.4.6](#1112-venv2-2046)
    - [1.1.2 venv2 for windows](#112-venv2-for-windows)
  - [1.2 venv3](#12-venv3)
    - [1.2.1 venv3 for mac](#121-venv3-for-mac)
      - [1.2.1.1 venv3 16.7.5](#1211-venv3-1675)
      - [1.2.1.2 venv3 20.4.6](#1212-venv3-2046)
    - [1.2.2 venv3 for windows](#122-venv3-for-windows)
- [二. 多模块配置](#二-多模块配置)
- [三. venvX activate and deactivate](#三-venvx-activate-and-deactivate)
  - [3.1 venvX activate](#31-venvx-activate)
    - [3.1.1 activate for mac](#311-activate-for-mac)
    - [3.1.2 activate for windows](#312-activate-for-windows)
- [四. 脚本](#四-脚本)
  - [4.1 python version](#41-python-version)
  - [4.2 pip setuptools wheel version](#42-pip-setuptools-wheel-version)
    - [4.2.1 pip freeze list](#421-pip-freeze-list)
    - [4.2.2 setuptools](#422-setuptools)
      - [4.2.2.1 setup.cfg](#4221-setupcfg)
      - [4.2.2.2 setup.py](#4222-setuppy)
  - [4.3 virtualenv version](#43-virtualenv-version)
  - [4.4 tox tox-travis version](#44-tox-tox-travis-version)
  - [4.5 twine version](#45-twine-version)
- [五. 参考](#五-参考)

## 一. 构建`venv`环境

首先检查是否安装如下软件包:

```bash
# python2
python2 -m pip --version
python2 -m setuptools --version
python2 -m wheel --version
python2 -m virtualenv --version


# python3
python3 -m pip --version
python3 -m setuptools --version
python3 -m wheel --version
python3 -m virtualenv --version
```

如果没有，请安装如下软件包:

```bash
# python2
python2 -m pip install setuptools wheel virtualenv
或
python2 -m pip install virtualenv

# python3
python3 -m pip install setuptools wheel virtualenv
或
python3 -m pip install virtualenv
```

### 1.1 venv2

#### 1.1.1 venv2 for mac

##### 1.1.1.1 venv2 16.7.5

```bash
python2 -m virtualenv -p /usr/local/bin/python2 --no-site-packages venv2
```

##### 1.1.1.2 venv2 20.4.6

```bash
python2 -m virtualenv -p /usr/local/bin/python2 venv2
```

#### 1.1.2 venv2 for windows

```bash
python2 -m virtualenv -p C:\Python\Python27\python2.exe venv2

或

python2 -m virtualenv -p C:\Python\Python27\python2.exe venv2 > venv2.log
```

### 1.2 venv3

#### 1.2.1 venv3 for mac

##### 1.2.1.1 venv3 16.7.5

```bash
python3 -m virtualenv -p /usr/local/bin/python3 --no-site-packages venv
```

##### 1.2.1.2 venv3 20.4.6

```bash
python3 -m virtualenv -p /usr/local/bin/python3 venv
```

#### 1.2.2 venv3 for windows

```bash
python3 -m virtualenv -p C:\Python\Python38\python3.exe venv

或

python3 -m virtualenv -p C:\Python\Python38\python3.exe venv > venv.log
```

## 二. 多模块配置

具体步骤:

1. 在`venv2`和`venv` 下新建一个`python.pth`文件，具体目录为`venv2/lib/python2.x/site-packages/python.pth`和`venv/lib/python3.x/site-packages/python.pth`;
2. 在上述`python.pth`文件中写入多模块的`绝对路径`(自己设备上实际目录);

```python
# venv2 环境
# /Users/.../Python-DeMo/venv2/lib/python2.x/site-packages/python.pth
#
# venv 环境
# /Users/.../Python-DeMo/venv/lib/python3.x/site-packages/python.pth

/Users/.../Python-DeMo/src
/Users/.../Python-DeMo/test
/Users/.../Python-DeMo/mock
/Users/.../Python-DeMo/case
```

## 三. venvX activate and deactivate

### 3.1 venvX activate

#### 3.1.1 activate for mac

在控制台中输入如下命令，使得Mac 环境下的 `virtualenv` 生效:

```bash
# python2
source ./venv2/bin/activate


# python3
source ./venv/bin/activate
```

#### 3.1.2 activate for windows

在控制台中输入如下命令，使得Windows 环境下的 `virtualenv` 生效:

```bash
# python2
./venv2/Scripts/activate


# python3
./venv/Scripts/activate
```

## 四. 脚本

### 4.1 python version

```bash
# python
python2 --version
# python help
python2 --help > ./Temp/help/python_help.txt
```

### 4.2 pip setuptools wheel version

```bash
# pip
python2 -m pip --version

# pip setuptools wheel help
python2 -m pip --help > ./Temp/help/python_pip_help.txt
## python2 -m setuptools --help > ./Temp/help/python_setuptools_help.txt
python2 -m setup.py --help-commands > ./Temp/help/python_setuptools_help.txt
python2 -m wheel --help > ./Temp/help/python_wheel_help.txt
```

#### 4.2.1 pip freeze list

```bash
# pip freeze
python2 -m pip freeze > ./Temp/python_pip_freeze.txt
python2 -m pip list > ./Temp/python_pip_list.txt
```

#### 4.2.2 setuptools

##### 4.2.2.1 setup.cfg

```bash
# python2 build
python2 -m pip install build
python2 -m pip install --upgrade build
python2 -m build
python2 -m build > ./out/dist/build.txt

# python3 build
python3 -m pip install build
python3 -m pip install --upgrade build
python3 -m build
python3 -m build > ./out/dist/build.txt
```

##### 4.2.2.2 setup.py

```bash
# setup sdist
python2 setup.py sdist > ./out/dist/setup_sdist.txt
python3 setup.py sdist > ./out/dist/setup_sdist.txt

python2 setup.py bdist_wheel --universal
python3 setup.py bdist_wheel --universal

python2 setup.py bdist_wheel
python3 setup.py bdist_wheel
```

### 4.3 virtualenv version

```bash
# virtualenv
python2 -m virtualenv --version
# virtualenv help
python2 -m virtualenv --help > ./Temp/help/python_virtualenv_help.txt
```

### 4.4 tox tox-travis version

```bash
# tox
python2 -m tox --version
# python2 -m tox-travis --version
# tox tox-travis help
python2 -m tox --help > ./Temp/help/python_tox_help.txt
# python2 -m tox-travis --help > ./Temp/help/python_tox_travis_help.txt
```

如若快捷生成脚本,参考如下命令:

```bash
tox-quickstart
```

默认运行命令，如下:

```bash
tox
```

### 4.5 twine version

```bash
# twine
python2 -m twine --version
# twine help
python2 -m twine --help > ./Temp/help/python_twine_help.txt

# check python check and upload dist format
twine check dist/*
twine upload dist/*
```

## 五. 参考

1. https://packaging.python.org/tutorials/packaging-projects/
2. https://packaging.python.org/guides/distributing-packages-using-setuptools/
3. https://pypi.org/pypi?%3Aaction=list_classifiers
4. https://docs.python.org/2/distutils/setupscript.html#additional-meta-data
