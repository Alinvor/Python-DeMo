# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import json
import os
import sys

obj = {}
obj["base_project_prefix"] = os.getenv('base_project_prefix')
obj["versionInfo"] = tuple(sys.version_info)
obj["sysModules"] = {}
for (k, v) in sys.modules.items():
    (obj["sysModules"])[str(k)] = str(v)
obj["sysPrefix"] = sys.prefix
obj["sysVersion"] = sys.version
obj["sysPath"] = sys.path
obj["sysPlatform"] = sys.platform
obj["is64Bit"] = sys.maxsize > 2**32
obj["PWD"] = os.environ.get('PWD')
obj["VIRTUAL_ENV"] = os.environ.get('VIRTUAL_ENV')

values = json.dumps(obj, indent=4)
# print(values)
print('ref: ./Temp/debug/env/interpreterInfo.json')
with open('./Temp/debug/env/interpreterInfo.json', 'w') as file:
    file.write(values)
