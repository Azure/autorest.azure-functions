import os
import subprocess
import tempfile
import unittest
from abc import ABCMeta


class CodeGeneratorTestCase(unittest.TestCase, metaclass=ABCMeta):
    _AUTOREST_COMMAND = 'autorest'
    _AUTOREST_INPUT_FILE_PARAMETER = '--input-file'
    _AUTOREST_OUTPUT_FILE_PARAMETER = '--input-file'
    _AUTOREST_USE_PARAMETER = '--use'
    _AUTOREST_NO_ASYNC_PARAMETER = '--no-async'
    _AUTOREST_LANGUAGE_PARAMETER = '--language'

    def test_codegen(self):
        """

        :return:
        """


class MyTestCase(CodeGeneratorTestCase):

    def setUp(self) -> None:
        CodeGeneratorTestCase.setUp(self)
        self.dummy_azure_function_folder = tempfile.mkdtemp()

    def test_codegen(self):
        """
        autorest --input-file:/Users/varadmeru/work/microsoft/azfunc-learning-docs/work-investigations/petstore-swagger.json
        --use:. --output-folder:/Users/varadmeru/work/microsoft/azfunc-learning-docs/work-investigations/python-autogen-test
        --no-async --language:python

        :return:
        """
        input_file_args = os.path.join()

        autorest_args = [self._AUTOREST_COMMAND]
        subprocess.Popen(
            hostexe_args,
            cwd=script_root,
            env={
                **os.environ,
                **extra_env,
            },
            stdout=stdout,
            stderr=stderr)

if __name__ == '__main__':
    unittest.main()
