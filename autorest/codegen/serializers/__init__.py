# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import logging
from pathlib import Path

from .azure_functions import Languages
from .azure_functions.python import AzureFunctionsPythonSerializer
from ..models import CodeModel
from ...jsonrpc import AutorestAPI

__all__ = [
    "JinjaSerializer",
    "_LOGGER"
]

_LOGGER = logging.getLogger(__name__)


class JinjaSerializer:
    def __init__(self, autorestapi: AutorestAPI) -> None:
        self._autorestapi = autorestapi
        # of the serializer to pick up

    def serialize(self, code_model: CodeModel) -> None:
        """

        :param code_model:
        :return:
        """
        function_app_path = (
            Path(".") if code_model.options["no_namespace_folders"]
            else Path(*(code_model.namespace.split("."))))

        if code_model.options['language'] == Languages.PYTHON.value:
            _LOGGER.debug("AzureFunctionsPythonSerializer serializing now")
            serializer = AzureFunctionsPythonSerializer(
                    autorest_api=self._autorestapi,
                    code_model=code_model,
                    function_app_path=function_app_path,
                    async_mode=False)
            serializer.serialize()
        else:
            language = code_model.options['language']
            supported_languages = Languages.supported_list()
            raise NotImplementedError(f"The language {language} has not been "
                                      f"implemented yet. Current Supported "
                                      f"list: {supported_languages}")
