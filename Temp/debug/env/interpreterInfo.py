# -*- coding:utf-8 -*-
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import json
import os
import sys

obj = {}
obj["BASE_PROJECT_PREFIX"] = os.getenv('BASE_PROJECT_PREFIX', None)
if obj["BASE_PROJECT_PREFIX"] is None:
    raise KeyError('the please configure BASE_PROJECT_PREFIX environment variable, otherwise it cannot run')
obj["is64Bit"] = sys.maxsize > 2**32
obj["PWD"] = os.environ.get('PWD')
obj["PYTHONPATH"] = os.environ.get('PYTHONPATH')
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
