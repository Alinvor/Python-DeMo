# -*- coding:utf-8 -*-
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import json
import os
import sys

obj = {}
obj["is64Bit"] = sys.maxsize > 2**32
obj["PWD"] = os.environ.get('PWD')
obj["PYTHON_PROJECT_PREFIX"] = os.getenv('PYTHON_PROJECT_PREFIX', None)
obj["PYTHON_PROJECT_NAME"] = os.getenv('PYTHON_PROJECT_NAME', None)
obj["PYTHON_PROJECT_PATH"] = os.getenv('PYTHON_PROJECT_PATH', None)
if obj["PYTHON_PROJECT_PATH"] is None:
    raise KeyError('the please configure PYTHON_PROJECT_PATH environment variable, otherwise it cannot run')
obj["PYTHONPATH"] = os.environ.get('PYTHONPATH')
obj["PYTHONTRACEMALLOC"] = os.getenv('PYTHONTRACEMALLOC', None)
obj["PYTHONUTF8"] = os.getenv('PYTHONUTF8', None)
obj["sysModules"] = {}
for (k, v) in sys.modules.items():
    (obj["sysModules"])[str(k)] = str(v)
obj["sysPath"] = sys.path
obj["sysPlatform"] = sys.platform
obj["sysPrefix"] = sys.prefix
obj["sysVersion"] = sys.version
obj["versionInfo"] = tuple(sys.version_info)
obj["VIRTUAL_ENV"] = os.environ.get('VIRTUAL_ENV')

values = json.dumps(obj, indent=4)
# print(values)
print('ref: ./Temp/debug/env/interpreterInfo.json')
with open('./Temp/debug/env/interpreterInfo.json', 'w') as file:
    file.write(values)
