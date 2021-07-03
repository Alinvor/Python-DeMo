# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
import json

values = json.dumps(dict(os.environ), indent=4)
# print(values)
print('ref: ./Temp/debug/env/printEnvVariables.json')
with open('./Temp/debug/env/printEnvVariables.json', 'w') as file:
    file.write(values)
