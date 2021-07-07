# 规则

- [一. 说明](#一-说明)
- [二. 文档](#二-文档)
  - [2.1. 规则文档](#21-规则文档)
  - [2.2. 命令文档](#22-命令文档)
- [三. 源码](#三-源码)
- [四. 调试](#四-调试)
  - [4.1. System 环境变量](#41-system-环境变量)
  - [4.2. VSCode PYTHONPATH](#42-vscode-pythonpath)
  - [4.3. inline import](#43-inline-import)
- [五. 测试](#五-测试)

## 一. 说明

本文档适用于全局性规则要义;

## 二. 文档

### 2.1. 规则文档

pass

### 2.2. 命令文档

1. [【Command】bash or ps1](../../Temp/bash/bash_or_ps1.md)
2. [【Command】python script](../../Temp/bash/python_command.md)

## 三. 源码

1. 统一采用`com.dvsnier` 命名空间;
2. 包结构，统一定义: `com.dvsnier.xxx`, 且`xxx` 包名称一定要和目录层次一一对应, 可以避免潜在无关紧要问题;

## 四. 调试

### 4.1. System 环境变量

目前我们规定如下可选全局变量:

- `PYTHONPATH`: 【可选项】, Python 环境变量;
- `BASE_PROJECT_PREFIX`: 【必选项】, 当前工作区目录前缀;

> 1. `工作区`: 当前程序被系统`调用并执行`的区间点;
> 2. `运行区`: 当前程序被系统`执行`的区间点;
>
> > - `工作目录`: 当前进程的`静态执行` 符号载体;
> > - `运行目录`: 当前进程的`动态执行` 驻留载体;

```bash
# darwin Python
# export PYTHONPATH=.
export BASE_PROJECT_PREFIX="/Users/.../Python-DeMo"

# win Python
# PYTHONPATH=.
BASE_PROJECT_PREFIX="D:\\...\\Python-DeMo"
```

### 4.2. VSCode PYTHONPATH

VSCode 环境变量指定的默认配置选项为:

```json
{
    "python.envFile": "${workspaceFolder}/.env"
}
```

**注意**:

1. 在`${workspaceFolder}/.env` 文件中所指定 `PYTHONPATH` 请使用`绝对路径`, 因为使用相对路径目前的版本不受支持;
2. 目前无需在 VSCode 中使用`.` 操作符指定当前目录, 从而被重复加入到VSCode `PYTHONPATH` 中, VSCode 默认具有当前功能(隐含默认将当前执行目录加入`PYTHONPATH` 环境变量);
3. 加载环境变量顺序需要注意, VSCode 默认加载位置为: `["VSCode DEFAULT RULES(stdlib)", "VSCode DEFAULT INLINE RULUES WITH PYTHON PATH . AND SRC", "VSCode PYTHONPATH WITH ENV", "SYSTEM DEFAULT PYTHON PATH LIST", "virtual environment list"]`
4. `.` 操作符在VSCode `PYTHONPATH` 中单独使用是起作用的, 联合使用不起作用, 是 VSCode 的一个 Bug, 同时不支持 `${workspaceFolder}` 变量替换;

具体 `PYTHONPATH` 添加规则如下:

```bash
"VSCode STD LIBRARY" ↔ "VSCode DEFAULT RULES(stdlib)"
        ↓                               ↓
"VSCode CURRENT RULES" ↔ "VSCode DEFAULT INLINE RULES WITH PYTHON PATH . AND SRC"
        ↓                     ↓
"VSCode ENV" ↔ "VSCode PYTHONPATH WITH ENV"
        ↓                   ↓
"SYSTEM" ↔ "SYSTEM DEFAULT PYTHON PATH LIST"
        ↓                           ↓
"VIRTUAL ENVIRONMENT" ↔ "virtual environment list"
```

举例如下:

```bash
# darwin
PYTHONPATH=/Users/.../Python-DeMo:/Users/.../Python-DeMo/tests:${PYTHONPATH}

# win32
PYTHONPATH=D:\\WorkSpace\\...\\Python-DeMo;D:\\WorkSpace\\...\\Python-DeMo\\tests;%PYTHONPATH%
```

### 4.3. inline import

**内联导入**:

在 VSCode 中, 如果需要在 `tests` 写测试用例, 调用 `src` 中代码, 由于 Python 或 VSCode 机制的原因, 实际上不指明 `PYTHONPATH` 的情况下, 是无法进行调用的; 因此我们采用如下方式:

1. `PYTHONPATH` 指定绝对路径方式【不推荐】;
2. 将 `src` 调试安装到当前虚拟环境下(需要 `setup.py` 文件参与)**【推荐】**;

举例如下:

```bash
pip2 install -e .
pip3 install -e .
```

## 五. 测试

1. 统一采用和源码空间统一的目录结构和命名空间形式;
