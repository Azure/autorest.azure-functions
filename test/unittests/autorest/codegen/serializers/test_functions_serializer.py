# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import os
import unittest
from abc import ABCMeta
from typing import Any, Dict

import yaml
from jinja2 import Environment, PackageLoader

from autorest.codegen import CodeGenerator
from autorest.codegen.serializers.azure_functions.python import \
    AzureFunctionsPythonAppSerializer


class TestAzureFunctionsPythonAppSerializer(unittest.TestCase,
                                            metaclass=ABCMeta):
    @staticmethod
    def load_code_model():
        options: Dict[str, Any] = {
            "language": "python"
        }

        test_yaml_file = os.path.join("test", "data", "test-code-generated.yml")
        # Parse the received YAML
        yaml_data = yaml.safe_load(test_yaml_file)
        return CodeGenerator._create_code_model(yaml_data=yaml_data,
                                                options=options)

    @classmethod
    def setUpClass(cls):
        cls.jinja_templates_env = Environment(loader=PackageLoader(
                "autorest.codegen.azure_functions_templates", "python"),
                keep_trailing_newline=True,
                line_statement_prefix="##", line_comment_prefix="###",
                trim_blocks=True, lstrip_blocks=True)
        cls.azfunc_python_app_serializer = AzureFunctionsPythonAppSerializer(
                cls.jinja_templates_env, False)


class TestHttpFunctionsSerializer(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
