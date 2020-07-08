# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import unittest
from abc import ABCMeta, abstractmethod

from jinja2 import Environment, PackageLoader

from autorest.codegen.serializers.azure_functions.common import prettify_json
from autorest.codegen.serializers.azure_functions.python import \
    AzureFunctionsPythonAppSerializer


class TemplateTests(unittest.TestCase, metaclass=ABCMeta):
    @classmethod
    def setUpClass(cls):
        cls.env = Environment(loader=PackageLoader(
                "autorest.codegen.azure_functions_templates", "python"),
                keep_trailing_newline=True,
                line_statement_prefix="##", line_comment_prefix="###",
                trim_blocks=True, lstrip_blocks=True)
        cls.azfunc_python_app_serializer = AzureFunctionsPythonAppSerializer(
            cls.env, False)

    @abstractmethod
    def test_template(self):
        """test the template

        :return:
        """


class TestExtensionBundleHost(TemplateTests):
    def test_template(self):
        expected_template = '''"extensionBundle": {
    "id": "Microsoft.Azure.Functions.ExtensionBundle",
    "version": "[1.*, 2.0.0)"
}
'''
        template = self.env.get_template("extension-bundle-host.json.jinja2")
        self.assertEqual(template.render(), expected_template)


class TestFuncignore(TemplateTests):
    def test_template(self):
        expected_template = '''.git*
.vscode
local.settings.json
test
.venv
'''
        template = self.env.get_template("funcignore.jinja2")
        self.assertEqual(template.render(), expected_template)


class TestFunctionsInit(TemplateTests):
    def test_template(self):
        expected_template = '''
'''
        template = self.env.get_template("extension-bundle-host.json.jinja2")
        self.assertEqual(template.render(), expected_template)


class TestFunctions(TemplateTests):
    def test_template(self):
        expected_template = '''
'''
        template = self.env.get_template("extension-bundle-host.json.jinja2")
        self.assertEqual(template.render(), expected_template)


class TestHost(TemplateTests):
    def test_template(self):
        expected_template = '''
{
  "version": {{ version }} {{"," if extension_bundle}}
  {{ extension_bundle }}
}
'''
        template = self.env.get_template("host.json.jinja2")
        return prettify_json(template.render(version='"2.0"',
                                             extension_bundle=self._get_extension_bundle()))


class TestHttpOutputBinding(TemplateTests):
    def test_template(self):
        expected_template = '''
'''
        template = self.env.get_template("extension-bundle-host.json.jinja2")
        self.assertEqual(template.render(), expected_template)


class TestHttpTrigger(TemplateTests):
    def test_template(self):
        expected_template = '''
'''
        template = self.env.get_template("extension-bundle-host.json.jinja2")
        self.assertEqual(template.render(), expected_template)


class TestSettings(TemplateTests):
    def test_template(self):
        expected_template = '''
'''
        template = self.env.get_template("extension-bundle-host.json.jinja2")
        self.assertEqual(template.render(), expected_template)


class TestProxies(TemplateTests):
    def test_template(self):
        expected_template = '''
'''
        template = self.env.get_template("extension-bundle-host.json.jinja2")
        self.assertEqual(template.render(), expected_template)


class TestReadmeMd(TemplateTests):
    def test_template(self):
        expected_template = '''
'''
        template = self.env.get_template("extension-bundle-host.json.jinja2")
        self.assertEqual(template.render(), expected_template)


class TestRequirements(TemplateTests):
    def test_template(self):
        expected_template = '''
'''
        template = self.env.get_template("extension-bundle-host.json.jinja2")
        self.assertEqual(template.render(), expected_template)


class TestVscodeExtensions(TemplateTests):
    def test_template(self):
        expected_template = '''
'''
        template = self.env.get_template("extension-bundle-host.json.jinja2")
        self.assertEqual(template.render(), expected_template)


class TestVscodeLaunch(TemplateTests):
    def test_template(self):
        expected_template = '''
'''
        template = self.env.get_template("extension-bundle-host.json.jinja2")
        self.assertEqual(template.render(), expected_template)


class TestVscodeSettings(TemplateTests):
    def test_template(self):
        expected_template = '''
'''
        template = self.env.get_template("extension-bundle-host.json.jinja2")
        self.assertEqual(template.render(), expected_template)


class TestVscodeTasks(TemplateTests):
    def test_template(self):
        expected_template = '''
'''
        template = self.env.get_template("extension-bundle-host.json.jinja2")
        self.assertEqual(template.render(), expected_template)


if __name__ == '__main__':
    unittest.main()
