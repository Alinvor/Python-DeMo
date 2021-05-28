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
- [五. 构建与分发](#五-构建与分发)
  - [5.1 安装](#51-安装)
  - [5.2 配置](#52-配置)
    - [5.2.1 pyproject.toml](#521-pyprojecttoml)
    - [5.2.2 MANIFEST.in](#522-manifestin)
    - [5.2.3 tox.ini](#523-toxini)
    - [5.2.4 setup.cfg](#524-setupcfg)
    - [5.2.5 README.md](#525-readmemd)
  - [5.3 构建](#53-构建)
    - [5.3.1 tox 脚本测试](#531-tox-脚本测试)
    - [5.3.2 build](#532-build)
  - [5.3 发布](#53-发布)
    - [5.3.1 注册账号](#531-注册账号)
    - [5.3.2 检查软件包](#532-检查软件包)
    - [5.3.3 上传软件包](#533-上传软件包)
- [六. 参考](#六-参考)

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

## 五. 构建与分发

Python 软件包开发工程结构，如下所示:

```Django
# soft package tree

--- project root
    |
    | --- .tox
    | --- .vscode
    | --- build
    | --- dist
    | --- doc
        --- ...
            --- README.md
    | --- src
        --- com
            --- dvsnier
                --- ...
    | --- test
        --- com
            --- dvsnier
                --- ...
    | --- venv
    | --- venv2
    | --- .editorconfig
    | --- .gitignore
    | --- LICENSE.txt
    | --- MANIFEST.in
    | --- pyproject.toml
    | --- README.md
    | --- setup.cfg
    | --- tox.ini
```

### 5.1 安装

首先检查是否安装如下依赖:

1. pip
2. flake8 (可选)
3. virtualenv
4. setuptools
5. wheel
6. discover
7. tox
8. toml (可选)
9. tox-travis (可选)
10. build
11. twine

如若没有，请使用`pip` 命令安装如下软件包:

```bash
# python2 pip version
python2 -m pip --version

python2 -m pip install flake8
python2 -m pip install virtualenv
python2 -m pip install setuptools
python2 -m pip install wheel
python2 -m pip install discover
python2 -m pip install tox
python2 -m pip install toml
python2 -m pip install tox-travis
python2 -m pip install build
python2 -m pip install twine

# python3 pip version
python3 -m pip --version

python3 -m pip install flake8
python3 -m pip install virtualenv
python3 -m pip install setuptools
python3 -m pip install wheel
python3 -m pip install discover
python3 -m pip install tox
python3 -m pip install toml
python3 -m pip install tox-travis
python3 -m pip install build
python3 -m pip install twine
```

其实一般安装有 `pip` 软件包的，一般都会有`setuptools` 和`wheel` 软件包附带安装;

### 5.2 配置

#### 5.2.1 pyproject.toml

首先配置 `pyproject.toml` ，模板固定, 一般不需大范围改动;

```bash
[build-system]
# https://setuptools.readthedocs.io/en/latest/build_meta.html
# These are the assumed default build requirements from pip:
# https://pip.pypa.io/en/stable/cli/pip/#pep-517-and-518-support
#
# As of version 10.0, pip supports projects declaring dependencies that are
# required at install time using a pyproject.toml file, in the form described
# in PEP 518. When building a project, pip will install the required
# dependencies locally, and make them available to the build process.
# Furthermore, from version 19.0 onwards, pip supports projects specifying the
# build backend they use in pyproject.toml, in the form described in PEP 517.
#
requires = [
    "setuptools>=40.8.0",
    "wheel"
]
build-backend = "setuptools.build_meta"
```

#### 5.2.2 MANIFEST.in

然后配置 `MANIFEST.in` 软件包应当包含哪些信息,哪些排除配置信息, 如下所示:

```bash
# https://packaging.python.org/guides/using-manifest-in/

include pyproject.toml

# Include the README
include *.md

# Include the license file
include LICENSE.txt
```

同上，模板一般都是固定结构，无需太范围改动;

#### 5.2.3 tox.ini

再然后配置 `tox` 脚本自动化测试, 指定Python 虚拟环境版本, 配置信息如下:

```bash
# tox (https://tox.readthedocs.io/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox" from this directory.
# For information see https://tox.readthedocs.io/en/latest/examples.html

[tox]
envlist = py27, py39

minversion = 3.23.1

# Activate isolated build environment. tox will use a virtual environment
# to build a source distribution from the source tree. For build tools and
# arguments use the pyproject.toml file as specified in PEP-517 and PEP-518.
isolated_build = true

# install testing framework
# ... or install anything else you might need here
[testenv]
platform = linux: linux
           macos: darwin
           windows: win32
; alwayscopy = True
allowlist_externals =
    /bin/bash
changedir =
    tests
deps =
    build
    discover
    twine
commands =
    discover
    ; python -m unittest discover
```

#### 5.2.4 setup.cfg

最后配置 `setup.cfg` 构建脚本, 指定软件包所要构建的软件细节部分, 举例配置信息如下:

```bash
[metadata]
# 1. https://setuptools.readthedocs.io/en/latest/
# 2. https://setuptools.readthedocs.io/en/latest/userguide/declarative_config.html
# 3. https://setuptools.readthedocs.io/en/latest/references/keywords.html
name = com.dvsnier.directory
version = 0.0.1.dev1
author = dvsnier
author_email = dovsnier@qq.com
description = this is dvsnier directory.
long_description = file: ./doc/description/directory/README.md
long_description_content_type = text/markdown
keywords = dir, development
url = https://github.com/Alinvor/Python-DeMo
project_urls =
    Documentation = https://packaging.python.org/tutorials/distributing-packages/
    Funding = https://donate.pypi.org
    Wiki = https://github.com/Alinvor/Python-DeMo/wiki
    Bug_Tracker = https://github.com/Alinvor/Python-DeMo/issues
    Source = https://github.com/Alinvor/Python-DeM
platforms = any
# classifiers
# Development Status :: 3 - Alpha
# Development Status :: 4 - Beta
# Development Status :: 5 - Production/Stable
classifiers =
    Development Status :: 3 - Alpha
    Programming Language :: Python :: 2.7
    Programming Language :: Python :: 3.8
    Programming Language :: Python :: 3.9
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

python_requires =
    >=2.7
    <4

# This includes the license file(s) in the wheel.
# https://wheel.readthedocs.io/en/stable/user_guide.html#including-license-files-in-the-generated-wheel-file
# https://choosealicense.com/
license = MIT License
license_files =
    LICENSE.txt

[options]
package_dir =
    = src

packages = find:

[options.packages.find]
where = src
#
# https://packaging.python.org/guides/distributing-packages-using-setuptools/#wheels
#
[bdist_wheel]
universal = 1
```

> 软件包`名称`和软件包`版本`信息, 一定要明确具体发布规则;

实际项目中, 可依据如上配置信息稍加修改和增添;

#### 5.2.5 README.md

更新`README.md` 版本和摘要信息;

### 5.3 构建

#### 5.3.1 tox 脚本测试

首次运行`tox` 命令，可使用`tox-quickstart` 命令, 依据简短提示信息进行配置:

```bash
tox-quickstart
```

后续运行`tox` 命令，可执行自动化脚本测试:

```bash
tox
```

#### 5.3.2 build

可使用如下命令, 进行`xxx.tar.gz` 源码包和`xxx.whl` 二进制包构建, 命令如下:

```bash
# python build tar.gz and whl
python2 -m build

# python build tar.gz
python2 -m build --sdist
# python build whl
python2 -m build --wheel


# python build tar.gz and whl
python3 -m build

# python build tar.gz
python3 -m build --sdist
# python build whl
python3 -m build --wheel
```

### 5.3 发布

#### 5.3.1 注册账号

1. 账户注册地址: https://pypi.org/account/register/
2. 创建一个[PyPI API令牌](https://pypi.org/help/#apitoken), 以便能够安全地上传您的项目;
3. 为了避免每次上载时都必须复制和粘贴令牌，可以创建一个`$HOME/.pypirc` 文件, 参考如下:

```bash
[pypi]
username = __token__
password = <the token value, including the `pypi-` prefix>
```

#### 5.3.2 检查软件包

检查软件包, 命令:

```bash
twine check dist/*
```

#### 5.3.3 上传软件包

上传软件包, 命令:

```bash
twine upload dist/*
```

## 六. 参考

1. https://packaging.python.org/tutorials/packaging-projects/
2. https://packaging.python.org/guides/distributing-packages-using-setuptools/
3. https://pypi.org/pypi?%3Aaction=list_classifiers
4. https://docs.python.org/2/distutils/setupscript.html#additional-meta-data
