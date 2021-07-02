# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import json
import os
import sys

obj = {}
obj["versionInfo"] = tuple(sys.version_info)
obj["sysPrefix"] = sys.prefix
obj["sysVersion"] = sys.version
obj["is64Bit"] = sys.maxsize > 2 ** 32
obj["PWD"] = os.environ.get('PWD')
obj["VIRTUAL_ENV"] = os.environ.get('VIRTUAL_ENV')

values = json.dumps(obj)
# print(values)
print('ref: ./Temp/debug/env/interpreterInfo.json')
with open('./Temp/debug/env/interpreterInfo.json', 'w') as file:
    file.write(values)
