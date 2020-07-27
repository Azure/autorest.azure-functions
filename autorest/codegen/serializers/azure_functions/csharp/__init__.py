# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import logging
from pathlib import Path

from jinja2 import ChoiceLoader, Environment, PackageLoader

from autorest import AutorestAPI
from autorest.codegen import CodeModel
from autorest.codegen.serializers.azure_functions import \
    AzureFunctionsSerializer
from autorest.codegen.serializers.azure_functions.common import prettify_json
# from autorest.codegen.serializers.azure_functions.python.functions_serializer \
#    import \
#    HttpFunctionsSerializer
# from autorest.codegen.serializers.azure_functions.python \
#    .model_generic_serializer import \
#    ModelGenericSerializer
# from autorest.codegen.serializers.azure_functions.python \
#    .model_init_serializer import \
#    ModelInitSerializer
# from autorest.codegen.serializers.azure_functions.python \
#    .model_python3_serializer import \
#    ModelPython3Serializer
# from autorest.codegen.serializers.enum_serializer import EnumSerializer

_LOGGER = logging.getLogger(__name__)

__all__ = [
    "AzureFunctionsCSharpSerializer",
    "AzureFunctionsCSharpAppSerializer"
]

_VSCODE_FOLDER_NAME = ".vscode"


class AzureFunctionsCSharpSerializer(AzureFunctionsSerializer):
    def __init__(self, autorest_api: AutorestAPI, code_model: CodeModel,
                 function_app_path: Path, async_mode: bool):
        super().__init__(autorest_api, code_model, function_app_path,
                         async_mode)
        self.azure_functions_templates_env: Environment = Environment(
            loader=ChoiceLoader([PackageLoader(
                "autorest.codegen.azure_functions_templates", "csharp"),
                PackageLoader(
                "autorest.codegen.azure_functions_templates.csharp",
                "templates")]), keep_trailing_newline=True,
            line_statement_prefix="##",
            line_comment_prefix="###", trim_blocks=True, lstrip_blocks=True)

    def serialize(self):
        _LOGGER.debug("Generating Functions")
        #self._serialize_and_write_functions(code_model=self.code_model, env=self.azure_functions_templates_env, function_app_path=self.function_app_path)

        _LOGGER.debug("Generating Function App contents")
        self._serialize_and_write_function_app_contents(
            env=self.azure_functions_templates_env, code_model=self.code_model, function_app_path=self.function_app_path)

        # Writes the model folder
        _LOGGER.debug("Generating python model folders")
        # if self.code_model.schemas or self.code_model.enums:
        #self._serialize_and_write_models_folder(code_model=self.code_model, env=self.azure_functions_templates_env, function_app_path=self.function_app_path)

    def _serialize_and_write_models_folder(self, code_model: CodeModel,
                                           env: Environment,
                                           function_app_path: Path) -> None:
        """
        :param code_model:
        :param env:
        :param function_app_path:
        :return:
        """
        models_path = function_app_path / Path("models")
        # if code_model.schemas:
        #self.autorest_api.write_file(models_path / Path("_models.py"), ModelGenericSerializer(code_model=code_model, env=env).serialize())
        #self.autorest_api.write_file(models_path / Path("_models_py3.py"), ModelPython3Serializer(code_model=code_model, env=env).serialize())
        # if code_model.enums:
        #self.autorest_api.write_file(models_path / Path(f"_{code_model.module_name}_enums.py"), EnumSerializer(code_model=code_model, env=env).serialize())
        #self.autorest_api.write_file(models_path / Path("__init__.py"), ModelInitSerializer(code_model=code_model, env=env).serialize())

    def _serialize_and_write_function_app_contents(
            self, env: Environment, code_model: CodeModel, function_app_path: Path) -> None:
        """Create the top level function all files.

        This generates the following files -
        - host.json
        - local.settings.json
        - .gitignore
        - app.csproj
        - .vscode files
        # - README.md

        :param code_model:
        :param env:
        :param function_app_path:
        :return:
        """

        azure_functions_serializer = AzureFunctionsCSharpAppSerializer(
            env=env, async_mode=False)

        # Write the host.json file in the Azure Functions App folder
        self.autorest_api.write_file(
            function_app_path / Path("host.json"),
            azure_functions_serializer.serialize_host_json_file()
        )

        # Write the local.settings.json file in the Azure Functions App folder
        self.autorest_api.write_file(function_app_path / Path("local.settings.json"),
                                     azure_functions_serializer.serialize_local_settings_json_file())

        # Write the .gitignore file in the Azure Functions App folder
        self.autorest_api.write_file(
            function_app_path / Path(".gitignore"), azure_functions_serializer.serialize_gitignore_file())

        # Write the csproj file in the Azure Functions App folder
        self.autorest_api.write_file(
            function_app_path / Path(code_model.namespace + ".csproj"), azure_functions_serializer.serialize_csproj_file())

        # Write the .funcignore file in the Azure Functions App folder
        # self.autorest_api.write_file(
        #        function_app_path /
        #        Path(".funcignore"),
        #        azure_functions_serializer.serialize_funcignore_file()
        # )

        # Write the proxies file in the Azure Functions App folder
        # self.autorest_api.write_file(
        #        function_app_path /
        #        Path("proxies.json"),
        #        azure_functions_serializer.serialize_proxies_json_file()
        # )

        # Write the README.md file in the Azure Functions App folder
        # self.autorest_api.write_file(
        #        function_app_path / Path("README.md"),
        #        azure_functions_serializer.serialize_readme_md_file(
        #                function_app_path)
        # )

        self._serialize_and_write_function_app_vscode_contents(
            env, function_app_path)

    def _serialize_and_write_function_app_vscode_contents(
            self, env: Environment, function_app_path: Path) -> None:

        azure_functions_serializer = AzureFunctionsCSharpAppSerializer(
            env=env, async_mode=False)

        self.autorest_api.write_file(function_app_path / Path(_VSCODE_FOLDER_NAME) / Path(
            "extensions.json"), azure_functions_serializer.serialize_extensions_json_file())

    def _serialize_and_write_functions(
            self, code_model: CodeModel, env: Environment,
            function_app_path: Path
    ) -> None:
        """Creating functions based on the spec

        Each function contains at least two files -
                         __init__.py and function.json file.
        - __init__.py - The actual function code
        - function.json - The function.json file is the one used to specify the
        triggers and bindings for the functions host to understand the function
        and setup for action.

        :param code_model:
        :param env:
        :param function_app_path:
        :return:
        """

        # for operation_group in code_model.operation_groups:
        # Todo: Current default serializer is Http. Extend this to change
        #  based on different openAPI extensions,
        # trigger types and bindings

        # http_functions_serializer = HttpFunctionsSerializer(
        #        code_model=code_model, env=env,
        #        operation_group=operation_group,
        #        async_mode=False)

        # for operation in code_model.operation_groups[0].operations:
        # self.autorest_api.write_file(
        #        function_app_path /
        #        Path(f"{operation.name}") / Path("__init__.py"),
        #        http_functions_serializer.serialize_functions_init_file(
        #                operation)
        # )

        # self.autorest_api.write_file(
        #        function_app_path /
        #        Path(f"{operation.name}") / Path("function.json"),
        #        http_functions_serializer.serialize_functions_json_file(
        #                operation)
        # )


class AzureFunctionsCSharpAppSerializer(object):
    def __init__(self, env: Environment, async_mode: bool) -> None:
        self.env = env
        self.async_mode = async_mode

    # def serialize_funcignore_file(self):
    #    template = self.env.get_template("funcignore.jinja2")
    #    return template.render()

    def serialize_gitignore_file(self):
        template = self.env.get_template("gitignore.jinja2")
        return template.render()

    def serialize_host_json_file(self):
        template = self.env.get_template("host.json.jinja2")
        return prettify_json(template.render())
        # return prettify_json(template.render(version='"2.0"', extension_bundle=self._get_extension_bundle()))

    def serialize_local_settings_json_file(self):
        template = self.env.get_template("local.settings.json.jinja2")
        return prettify_json(template.render())
        # return prettify_json(template.render(is_encrypted="false", azure_web_jobs_storage_secret='""', language_worker_runtime='"python"'))

    def serialize_csproj_file(self):
        template = self.env.get_template("app.csproj.jinja2")
        return template.render()

    # def serialize_proxies_json_file(self):
    #    template = self.env.get_template("proxies.json.jinja2")
    #    return template.render()

    # def serialize_readme_md_file(self, function_app_path):
    #    template = self.env.get_template("readme.md.jinja2")
    #    return template.render(function_app_name=function_app_path)

    def serialize_extensions_json_file(self):
        template = self.env.get_template("vscode/extensions.json.jinja2")
        return prettify_json(template.render())

    # def serialize_launch_json_file(self):
    #    template = self.env.get_template("vscode-launch.json.jinja2")
    #    return template.render()

    # def serialize_settings_json_file(self):
    #    template = self.env.get_template("vscode-settings.json.jinja2")
    #    return template.render()

    # def serialize_tasks_json_file(self):
    #    template = self.env.get_template("vscode-tasks.json.jinja2")
    #    return template.render()

    # def _get_extension_bundle(self):
    #    template = self.env.get_template("extension-bundle-host.json.jinja2")
    #    return template.render()
