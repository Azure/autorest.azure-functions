# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from abc import ABC, abstractmethod
from enum import Enum
from pathlib import Path

from autorest import AutorestAPI
from autorest.codegen import CodeModel

__all__ = [
    "AzureFunctionsSerializer",
    "Languages"
]


class AzureFunctionsSerializer(ABC):
    """Abstract class for different Azure Functions language
    """

    def __init__(self, autorest_api: AutorestAPI, code_model: CodeModel,
                 function_app_path: Path, async_mode: bool):
        """Initialize the Functions serializer

        :param autorest_api:
        :param code_model:
        :param function_app_path:
        :param async_mode:
        """
        self.autorest_api = autorest_api
        self.code_model = code_model
        self.async_mode = async_mode
        self.function_app_path = function_app_path

    @abstractmethod
    def serialize(self):
        """Serialize the code model to specific language
        """


class Languages(Enum):
    """Current languages supported for code generation.
    """
    PYTHON = "python"
    JAVA = "java"
    CSHARP = "csharp"
    JAVASCRIPT = "javascript"
    TYPESCRIPT = "typescript"

    @classmethod
    def supported_list(cls):
        return ', '.join([item.value for item in cls])
