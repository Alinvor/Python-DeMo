# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
import json

values = json.dumps(dict(os.environ))
# print(values)
print('ref: ./Temp/debug/printEnvVariables.json')
with open('./Temp/debug/printEnvVariables.json', 'w') as file:
    file.write(values)
