# 命令

- [一. 删除缓存](#一-删除缓存)
  - [1.1. pyc and pycache](#11-pyc-and-pycache)
  - [1.2. 扩展目录](#12-扩展目录)

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
