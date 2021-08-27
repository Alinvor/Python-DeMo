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
    - [4.2.2 pip cache](#422-pip-cache)
    - [4.2.3 setuptools](#423-setuptools)
      - [4.2.3.1 setup.cfg](#4231-setupcfg)
      - [4.2.3.2 setup.py](#4232-setuppy)
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
    - [5.2.5 setup.py](#525-setuppy)
    - [5.2.6 README.md](#526-readmemd)
  - [5.3 构建](#53-构建)
    - [5.3.1 tox 脚本测试](#531-tox-脚本测试)
    - [5.3.2 build](#532-build)
  - [5.3 发布](#53-发布)
    - [5.3.1 注册账号](#531-注册账号)
    - [5.3.2 检查软件包](#532-检查软件包)
    - [5.3.3 上传软件包](#533-上传软件包)
- [六. WiKi](#六-wiki)
  - [6.1 规约与守则](#61-规约与守则)
  - [6.2 文档与源码](#62-文档与源码)
  - [6.3 配置与模板](#63-配置与模板)
  - [6.4 调试与构建](#64-调试与构建)
  - [6.5 日志与清理](#65-日志与清理)
- [七. 参考](#七-参考)

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

在控制台中输入如下命令，使得 Mac 环境下的 `virtualenv` 生效:

```bash
# python2
source ./venv2/bin/activate


# python3
source ./venv/bin/activate
```

#### 3.1.2 activate for windows

在控制台中输入如下命令，使得 Windows 环境下的 `virtualenv` 生效:

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
python3 --version
# python help
python2 --help > ./Temp/help/python2_help.txt
python3 --help > ./Temp/help/python3_help.txt
```

### 4.2 pip setuptools wheel version

```bash
# pip
python2 -m pip --version
python3 -m pip --version

# pip setuptools wheel help
python2 -m pip --help > ./Temp/help/python2_pip_help.txt
python3 -m pip --help > ./Temp/help/python3_pip_help.txt
## python2 -m setuptools --help > ./Temp/help/python2_setuptools_help.txt
## python3 -m setuptools --help > ./Temp/help/python3_setuptools_help.txt
python2 -m setup.py --help-commands > ./Temp/help/python2_setuptools_help.txt
python3 -m setup.py --help-commands > ./Temp/help/python3_setuptools_help.txt
python2 -m wheel --help > ./Temp/help/python2_wheel_help.txt
python3 -m wheel --help > ./Temp/help/python3_wheel_help.txt
```

#### 4.2.1 pip freeze list

```bash
# pip freeze
python2 -m pip freeze > ./Temp/python2_pip_freeze.txt
python3 -m pip freeze > ./Temp/python3_pip_freeze.txt
python2 -m pip list > ./Temp/python2_pip_list.txt
python3 -m pip list > ./Temp/python3_pip_list.txt
```

#### 4.2.2 pip cache

```bash
# pip cache list
python2 -m pip cache list > ./out/dist/python2_pip2_cache_list.txt
python3 -m pip cache list > ./out/dist/python3_pip3_cache_list.txt
# pip no cache install
python2 -m pip --no-cache-dir install com.dvsnier.*
python3 -m pip --no-cache-dir install com.dvsnier.*
# pip remove cache package with whl
python2 -m pip cache remove com.dvsnier.*
python3 -m pip cache remove com.dvsnier.*
```

#### 4.2.3 setuptools

##### 4.2.3.1 setup.cfg

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

##### 4.2.3.2 setup.py

```bash
# setup sdist
python2 setup.py sdist > ./out/dist/setup2_sdist.txt
python3 setup.py sdist > ./out/dist/setup3_sdist.txt

python2 setup.py bdist_wheel --universal
python3 setup.py bdist_wheel --universal

python2 setup.py bdist_wheel
python3 setup.py bdist_wheel
```

### 4.3 virtualenv version

```bash
# virtualenv
python2 -m virtualenv --version
python3 -m virtualenv --version
# virtualenv help
python2 -m virtualenv --help > ./Temp/help/python2_virtualenv_help.txt
python3 -m virtualenv --help > ./Temp/help/python3_virtualenv_help.txt
```

### 4.4 tox tox-travis version

```bash
# tox
python2 -m tox --version
# python2 -m tox-travis --version
python3 -m tox --version
# python3 -m tox-travis --version
# tox tox-travis help
python2 -m tox --help > ./Temp/help/python2_tox_help.txt
# python2 -m tox-travis --help > ./Temp/help/python2_tox_travis_help.txt
python3 -m tox --help > ./Temp/help/python3_tox_help.txt
# python3 -m tox-travis --help > ./Temp/help/python3_tox_travis_help.txt
```

如若快捷生成脚本,参考如下命令:

```bash
tox-quickstart
```

默认运行命令，如下:

```bash
tox

# the recommend
tox --result-json ./Temp/tox/python2_tox_result.json
tox --result-json ./Temp/tox/python3_tox_result.json
```

### 4.5 twine version

```bash
# twine
python2 -m twine --version
python3 -m twine --version
# twine help
python2 -m twine --help > ./Temp/help/python2_twine_help.txt
python3 -m twine --help > ./Temp/help/python3_twine_help.txt

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
    | --- out
    | --- src
        --- com
            --- dvsnier
                --- ...
    | --- Temp
    | --- template
    | --- tests
        --- com
            --- dvsnier
                --- ...
    | --- venv
    | --- venv2
    | --- .editorconfig
    | --- .env
    | --- .gitignore
    | --- .rmcache.sh
    | --- .rmcache.ps1
    | --- LICENSE.txt
    | --- MANIFEST.in
    | --- pyproject.toml
    | --- README.md
    | --- requirements.txt
    | --- setup.cfg
    | --- tox.ini
```

### 5.1 安装

首先检查是否安装如下依赖:

1. build
2. discover
3. flake8 (可选)
4. pip
5. setuptools
6. tox
7. toml (可选)
8. tox-travis (可选)
9. twine
10. unittest2
11. virtualenv
12. wheel

如若没有，请使用`pip` 命令安装如下软件包:

```bash
# python2 pip version
python2 -m pip --version

python2 -m pip install build
python2 -m pip install discover
python2 -m pip install flake8
python2 -m pip install pip
python2 -m pip install setuptools
python2 -m pip install tox
python2 -m pip install toml
python2 -m pip install tox-travis
python2 -m pip install twine
python2 -m pip install unittest2
python2 -m pip install virtualenv
python2 -m pip install wheel

# python3 pip version
python3 -m pip --version

python3 -m pip install build
python3 -m pip install discover
python3 -m pip install flake8
python3 -m pip install pip
python3 -m pip install setuptools
python3 -m pip install tox
python3 -m pip install toml
python3 -m pip install tox-travis
python3 -m pip install twine
python3 -m pip install unittest2
python3 -m pip install virtualenv
python3 -m pip install wheel
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

# # Include the requirements file
include requirements.txt
```

同上，模板一般都是固定结构，无需太范围改动;

#### 5.2.3 tox.ini

再然后配置 `tox` 脚本自动化测试, 指定 Python 虚拟环境版本, 配置信息如下:

```bash
# tox (https://tox.readthedocs.io/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox" from this directory.
# For information see https://tox.readthedocs.io/en/latest/examples.html

[tox]
envlist = py27, py38

minversion = 3.23.1

# Activate isolated build environment. tox will use a virtual environment
# to build a source distribution from the source tree. For build tools and
# arguments use the pyproject.toml file as specified in PEP-517 and PEP-518.
isolated_build = true

# install testing framework
# ... or install anything else you might need here
[testenv]
passenv =
    PYTHONPATH
platform = linux: linux
           macos: darwin
           windows: win32
; alwayscopy = True
allowlist_externals =
    /bin/bash
; changedir =
;     tests
#
# https://tox.readthedocs.io/en/latest/config.html#conf-deps
# https://tox.readthedocs.io/en/latest/example/basic.html#a-simple-tox-ini-default-environments
#
deps =
    -rrequirements.txt
    unittest2
    flake8
    virtualenv
    setuptools
    wheel
    discover
    tox
    toml
    tox-travis
    build
    twine
commands =
    ; windows: python --version
    ; macos,linux: python --version
    discover -s ./tests -t .
    ; unit2 discover []
    ; python -m unittest discover
```

#### 5.2.4 setup.cfg

最后配置 `setup.cfg` 构建脚本, 指定软件包所要构建的软件细节部分, 举例配置信息如下:

```bash
[metadata]
# 1. https://setuptools.readthedocs.io/en/latest/
# 2. https://setuptools.readthedocs.io/en/latest/userguide/declarative_config.html
# 3. https://setuptools.readthedocs.io/en/latest/references/keywords.html
name = com.dvsnier.xxx
version = 0.0.1.dev1
author = dvsnier
author_email = dovsnier@qq.com
description = this is dvsnier xxx.
long_description = file: ./doc/description/xxx/README.md
long_description_content_type = text/markdown
keywords = xxx, development
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
    Topic :: Software Development :: Libraries
    License :: OSI Approved :: MIT License
    Programming Language :: Python :: 2.7
    Programming Language :: Python :: 3.8
    Programming Language :: Python :: 3.9

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

#### 5.2.5 setup.py

最后配置 `setup.py` 构建脚本, 指定软件包所要构建的软件细节部分, 举例配置信息如下:

```bash
# -*- coding:utf-8 -*-
"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/Alinvor/Python-DeMo
"""

# Always prefer setuptools over distutils
# from setuptools import setup, find_packages, find_namespace_packages
from setuptools import setup, find_packages
import os
import sys


def read_text(file_name):
    ''' the read describe readme files content. '''
    content = ''
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if sys.version_info.major > 2:
                content += str(line)
            else:
                content += str(line).encode('utf-8')
    # print(content)
    return content


project = os.getenv('PYTHON_PROJECT_PATH')
if project is None:
    raise KeyError('the please configure PYTHON_PROJECT_PATH environment variable, otherwise it cannot run')
print(project)
PROJECT_DIRECTORY = 'xxx'  # project directory
PROJECT_README_FILE = 'README.md'  # project readme file
README_ROOT_DIRECTORY = os.path.join(project, 'doc/description')
README_PROJECT_DIRECTORY = os.path.join(README_ROOT_DIRECTORY, PROJECT_DIRECTORY)
PROJECT_DESCRIPTION = os.path.join(README_PROJECT_DIRECTORY, PROJECT_README_FILE)
#
# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.
#
# |  序列  |                 字段                  |   数据类型   |  选项  |  描述                 | 备注 |
# | :---: | :-----------------------------------: | :---------: | :---: | -------------------- | ---- |
# |   1   |             DVSNIER_NAME              |   string    |   Y   | 包名称                |      |
# |   2   |            DVSNIER_VERSION            |   string    |   Y   | 包版本                |      |
# |   3   |          DVSNIER_DESCRIPTOIN          |   string    |       | 包简单描述             |      |
# |   4   |       DVSNIER_LONG_DESCRIPTOIN        |    file     |       | 较长文档描述           |      |
# |   5   | DVSNIER_LONG_DESCRIPTION_CONTENT_TYPE |   string    |       | 长文本类型描述          |      |
# |   6   |              DVSNIER_URL              |    http     |       | 项目主页               |      |
# |   7   |            DVSNIER_AUTHOR             |   string    |       | 项目作者               |      |
# |   8   |         DVSNIER_AUTHOR_EMAIL          |    email    |       | 项目作者邮箱           |      |
# |   9   |         DVSNIER_LICENSE               |    许可证    |       | 许可证                |      |
# |  10   |          DVSNIER_CLASSIFIERS          | classifiers |       | 项目分类器             |      |
# |  11   |           DVSNIER_KEYWORDS            |  keywords   |       | 项目关键字             |      |
# |  12   |          DVSNIER_PACKAGE_DIR          |   string    |       | 包目录                |      |
# |  13   |          DVSNIER_PY_MODULES           |   string    |   Y   | 模块名称               |      |
# |  14   |           DVSNIER_PACKAGES            |   string    |   Y   | 包名称                 |      |
# |  15   |        DVSNIER_PYTHON_REQUIRES        |   string    |   Y   | 版本匹配分类器描述符     |      |
# |  16   |       DVSNIER_INSTALL_REQUIRES        |    list     |       | 依赖库                 |      |
# |  17   |        DVSNIER_EXTRAS_REQUIRE         |    dict     |       | 附加/扩展依赖           |      |
# |  18   |         DVSNIER_PACKAGE_DATA          |    dict     |       | 包数据文件              |      |
# |  19   |          DVSNIER_DATA_FILES           |    list     |       | 包外数据文件            |      |
# |  20   |         DVSNIER_ENTRY_POINTS          |    dict     |       | 入口点                 |      |
# |  21   |         DVSNIER_PROJECT_URLS          |    dict     |       | 项目 URL               |      |
# |  22   |                                       |             |       |                       |      |
DVSNIER_NAME = 'com.dvsnier.xxx'  # Required
DVSNIER_VERSION = '0.0.1.dev0'  # Required
DVSNIER_DESCRIPTOIN = 'this is dvsnier xxx.'  # Optional
# Get the long description from the README file
DVSNIER_LONG_DESCRIPTOIN = read_text(str(PROJECT_DESCRIPTION))  # Optional
DVSNIER_LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'  # Optional
DVSNIER_URL = 'https://github.com/Alinvor/Python-DeMo'  # Optional
DVSNIER_AUTHOR = 'dvsnier'  # Optional
DVSNIER_AUTHOR_EMAIL = 'dovsnier@qq.com'  # Optional
DVSNIER_LICENSE = 'MIT'  # Optional
DVSNIER_CLASSIFIERS = [  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    # 'Intended Audience :: Developers',
    # 'Topic :: Software Development :: Build Tools',
    'Topic :: Software Development :: Libraries',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate you support Python 3. These classifiers are *not*
    # checked by 'pip install'. See instead 'python_requires' below.
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    # 'Programming Language :: Python :: 3 :: Only',
    # 'Operating System :: OS Independent'
]
DVSNIER_KEYWORDS = 'xxx, development'  # Optional
DVSNIER_PACKAGE_DIR = {'': 'src'}  # Optional
# DVSNIER_PY_MODULES = ["xxx"]  # Required
# DVSNIER_PACKAGES = find_packages(include=['xxx', 'xxx.*'])  # Required
DVSNIER_PACKAGES = find_packages(where='src')  # Required
# DVSNIER_NAMESPACE_PACKAGES = find_namespace_packages(include=['com.*'])  # Required
# DVSNIER_PYTHON_REQUIRES = '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*'
DVSNIER_PYTHON_REQUIRES = '>=2.7, <4'
DVSNIER_INSTALL_REQUIRES = [  # Optional

]
DVSNIER_EXTRAS_REQUIRE = {  # Optional
    'dev': ['check-manifest'],
    'test': ['coverage']
}
DVSNIER_PACKAGE_DATA = {  # Optional
    # 'sample': ['package_data.dat'],
}
DVSNIER_DATA_FILES = [  # Optional
    # ('my_data', ['data/data_file'])
]
DVSNIER_ENTRY_POINTS = {  # Optional
    # 'console_scripts': [
    #     'dvs-dir=dvs:main',
    # ],
}
DVSNIER_PROJECT_URLS = {  # Optional
    'Bug_Tracker': 'https://github.com/Alinvor/Python-DeMo/issues',
    'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
    'Funding': 'https://donate.pypi.org',
    'Wiki': 'https://github.com/Alinvor/Python-DeMo/wiki',
    'Source': 'https://github.com/Alinvor/Python-DeMo'
}

setup(
    # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install com.dvsnier.xxx
    #
    # And where it will live on PyPI: https://pypi.org/project/com.dvsnier.xxx/
    #
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    name=DVSNIER_NAME,  # Required

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    # https://semver.org/lang/zh-CN/
    #
    # 1.2.0.dev1   Development release
    # 1.2.0a1      Alpha Release
    # 1.2.0b1      Beta Release
    # 1.2.0rc1     Release Candidate
    # 1.2.0        Final Release
    # 1.2.0.post1  Post Release
    # 15.10        Date based release
    # 23           Serial release
    #
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=DVSNIER_VERSION,  # Required

    # This is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    description=DVSNIER_DESCRIPTOIN,  # Optional

    # This is an optional longer description of your project that represents
    # the body of text which users will see when they visit PyPI.
    #
    # Often, this is the same as your README, so you can just read it in from
    # that file directly (as we have already done above)
    #
    # This field corresponds to the "Description" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=DVSNIER_LONG_DESCRIPTOIN,  # Optional

    # Denotes that our long_description is in Markdown; valid values are
    # text/plain, text/x-rst, and text/markdown
    #
    # Optional if long_description is written in reStructuredText (rst) but
    # required for plain-text or Markdown; if unspecified, "applications should
    # attempt to render [the long_description] as text/x-rst; charset=UTF-8 and
    # fall back to text/plain if it is not valid rst" (see link below)
    #
    # This field corresponds to the "Description-Content-Type" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type=DVSNIER_LONG_DESCRIPTION_CONTENT_TYPE,  # Optional (see note above)

    # This should be a valid link to your project's main homepage.
    #
    # This field corresponds to the "Home-Page" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#home-page-optional
    url=DVSNIER_URL,  # Optional

    # This should be your name or the name of the organization which owns the project.
    author=DVSNIER_AUTHOR,  # Optional

    # This should be a valid email address corresponding to the author listed above.
    author_email=DVSNIER_AUTHOR_EMAIL,  # Optional

    # The license argument doesn’t have to indicate the license under which your package is being released,
    # although you may optionally do so if you want. If you’re using a standard, well-known license, then
    # your main indication can and should be via the classifiers argument. Classifiers exist for all major
    #  open-source licenses.
    license=DVSNIER_LICENSE,  # Optional

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=DVSNIER_CLASSIFIERS,  # Optional

    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a list of additional keywords, separated
    # by commas, to be used to assist searching for the distribution in a
    # larger catalog.
    keywords=DVSNIER_KEYWORDS,  # Optional

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    package_dir=DVSNIER_PACKAGE_DIR,  # Optional

    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=DVSNIER_PACKAGES,  # Required

    #
    # Only for Python 3.x and above
    #
    # namespace_packages=DVSNIER_NAMESPACE_PACKAGES, # Optional

    # If your project contains any single-file Python modules that aren’t part of
    # a package, set py_modules to a list of the names of the modules (minus the .py
    # extension) in order to make setuptools aware of them.
    # py_modules=DVSNIER_PY_MODULES,  # Required

    # Specify which Python versions you support. In contrast to the
    # 'Programming Language' classifiers above, 'pip install' will check this
    # and refuse to install the project if the version does not match. See
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    python_requires=DVSNIER_PYTHON_REQUIRES,

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # https://packaging.python.org/discussions/install-requires-vs-requirements/
    install_requires=DVSNIER_INSTALL_REQUIRES,  # Optional

    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing projects.
    extras_require=DVSNIER_EXTRAS_REQUIRE,  # Optional

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    # https://setuptools.readthedocs.io/en/latest/userguide/datafiles.html
    package_data=DVSNIER_PACKAGE_DATA,  # Optional

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/distutils/setupscript.html#installing-additional-files
    # http://docs.python.org/3/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=DVSNIER_DATA_FILES,  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `dvsnier` which
    # executes the function `main` from this package when invoked:
    entry_points=DVSNIER_ENTRY_POINTS,  # Optional

    #
    # 1. https://www.python.org/dev/peps/pep-0328/
    # 2. https://setuptools.readthedocs.io/en/latest/userguide/package_discovery.html
    # 3. https://packaging.python.org/guides/packaging-namespace-packages/
    # 4. https://github.com/pypa/sample-namespace-packages/tree/master/pkgutil
    #
    zip_safe=False,

    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    project_urls=DVSNIER_PROJECT_URLS,  # Optional
)
```

> 软件包`名称`和软件包`版本`信息, 一定要明确具体发布规则;

实际项目中, 可依据如上配置信息稍加修改和增添;

#### 5.2.6 README.md

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

tox --verbose
tox --verbose --parallel all
tox --verbose --parallel auto
tox --verbose --parallel 4  // 4 cpu core
tox --verbose --parallel 8  // 8 cpu core

python2 -m tox --result-json ./Temp/help/python2_tox_result_json.txt
python3 -m tox --result-json ./Temp/help/python3_tox_result_json.txt

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
2. 创建一个[PyPI API 令牌](https://pypi.org/help/#apitoken), 以便能够安全地上传您的项目;
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

## 六. WiKi

### 6.1 规约与守则

1. [【Contract: 规约守则】](./doc/project_help/the_global_rules.md)

### 6.2 文档与源码

1. [【Document: Python 环境查看函数】](./doc/README.md)
2. [【Source: Recommended Source Websites】](./doc/SOURCE.md)

### 6.3 配置与模板

1. [【Config: The `LICENSE` File】](./LICENSE.txt)
2. [【Config: The `MANIFEST` File】](./MANIFEST.in)
3. [【Config: The `pyproject` File】](./pyproject.toml)
4. [【Config: The `requirements` File】](./requirements.txt)
5. [【Config: The `setup` File】](./setup.cfg)
6. [【Config: The `tox` File】](./tox.ini)
7. [【Template: The `__init__` File】](./template/__init__.py)
8. [【Template: The `__init__with_pkgutil` File】](./template/__init__with_pkgutil.py)
9. [【Template: The `template` File】](./template/template.py)
10. [【Template: The `template_class` File】](./template/template_class.py)
11. [【Template: The `test_template` File】](./template/test_template.py)

### 6.4 调试与构建

1. [【Debug: Bash_or_Ps1】](./Temp/bash/bash_or_ps1.md)
2. [【Debug: Python Command】](./Temp/bash/python_command.md)
3. [【Debug: Environment Variable Information(The Necessities)】](./Temp/debug/env/interpreterInfo.py)
4. [【Debug: Environment Variable Information(An Generals)】](./Temp/debug/env/interpreterInfo.py)
5. [【Build: The `Requirements` Text】](./Temp/archives/material/requirements.txt)
6. [【Build: The `Setup` Script】](./Temp/archives/material/setup.py)

### 6.5 日志与清理

1. [【Clean: darwin】](./.rmcache.sh)
2. [【Clean: win】](./.rmcache.ps1)

## 七. 参考

1. https://packaging.python.org/tutorials/packaging-projects/
2. https://packaging.python.org/guides/distributing-packages-using-setuptools/
3. https://pypi.org/pypi?%3Aaction=list_classifiers
4. https://docs.python.org/2/distutils/setupscript.html#additional-meta-data
