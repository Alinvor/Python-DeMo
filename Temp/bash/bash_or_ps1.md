# bash or ps1 命令

- [一. 删除缓存](#一-删除缓存)
  - [1.1. pyc and pycache](#11-pyc-and-pycache)
  - [1.2. 扩展目录](#12-扩展目录)
    - [1.2.1. build](#121-build)
    - [1.2.2. com.dvsnier.*.egg-info](#122-comdvsnieregg-info)
    - [1.2.3. dist](#123-dist)
    - [1.2.4. log](#124-log)

## 一. 删除缓存

### 1.1. pyc and pycache

```bash
## THE DELETE FILES
find . -name '*.pyc' -delete
## THE DELETE DIRECTORY
find . -type d -name __pycache__ -exec rm -r {} +
```

### 1.2. 扩展目录

推荐删除扩展目录:

- `build`
- `com.dvsnier.*.egg-info`
- `dist`
- `log`

#### 1.2.1. build

```bash
# ./build/*
find ./build -path "*" ! -name "build" -delete
```

#### 1.2.2. com.dvsnier.*.egg-info

```bash
# ./src/com.dvsnier.*.egg-info
find ./src -path "*com.dvsnier*" -delete
# find ./src -path "*com.dvsnier.*" -type d -exec rm -r {} +
# find ./src -path "*com.dvsnier.*" -type f -delete
```

#### 1.2.3. dist

```bash
# ./dist/*
find ./dist -path "*" ! -name "dist" -delete
```

#### 1.2.4. log

```bash
# ./out/log/*
find ./out/log -path "*" ! -name "log" -delete
```
