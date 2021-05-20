
# Python-DeMo

Python DeMo

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
- [三. venvX activate](#三-venvx-activate)
  - [3.1 activate for mac](#31-activate-for-mac)
  - [3.2 activate for windows](#32-activate-for-windows)

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

## 三. venvX activate

### 3.1 activate for mac

在控制台中输入如下命令，使得Mac 环境下的 `virtualenv` 生效:

```bash
# python2
source ./venv2/bin/activate


# python3
source ./venv/bin/activate
```

### 3.2 activate for windows

在控制台中输入如下命令，使得Windows 环境下的 `virtualenv` 生效:

```bash
# python2
source ./venv2/Scripts/activate


# python3
source ./venv/Scripts/activate
```
