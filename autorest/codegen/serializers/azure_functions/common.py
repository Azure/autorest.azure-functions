# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import json


def prettify_json(to_prettify):
    return json.dumps(json.loads(to_prettify), indent=2)
