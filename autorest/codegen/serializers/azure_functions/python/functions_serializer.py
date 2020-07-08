# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------


from jinja2 import Environment

from autorest.codegen import CodeModel, OperationGroup
from autorest.codegen.serializers.azure_functions.common import prettify_json
from autorest.codegen.serializers.azure_functions.python.import_serializer import FileImportSerializer
from autorest.codegen.serializers.azure_functions.python.trigger_serializer import InputTriggerSerializer
from autorest.codegen.serializers.azure_functions.python.bindings_serializer import OutputBindingsSerializer


class HttpFunctionsSerializer(object):
    default_script_filename = '"__init__.py"'

    def __init__(self, code_model: CodeModel, env: Environment, operation_group: OperationGroup,
                 async_mode: bool) -> None:
        self.code_model = code_model
        self.env = env
        self.operation_group = operation_group
        self.async_mode = async_mode

    def serialize_functions(self):
        pass

    def serialize_functions_init_file(self, operation):
        template = self.env.get_template("functions-init.py.jinja2")

        return template.render(
            code_model=self.code_model,
            request_type="HttpRequest",
            return_type="HttpResponse",
            function_name=operation.name,
            operations_description="Doing operation here",
            request_comment_description="Passing the request",
            return_comment_description="Request",
            magic_comment="### Do Magic Here! ###",
            imports=FileImportSerializer(
                self.operation_group.imports(self.async_mode, bool(self.code_model.schemas)),
                is_python_3_file=self.async_mode
            ),
            success_status_code="200",
            failure_status_code="405"
        )

    def serialize_functions_json_file(self, operation):
        template = self.env.get_template("functions.json.jinja2")

        return prettify_json(template.render(script_filename=self.default_script_filename,
                                             input_trigger=InputTriggerSerializer(operation, self.env),
                                             output_bindings=[OutputBindingsSerializer(operation, self.env)],
                                             is_disabled=False))
