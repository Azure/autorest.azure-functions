# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from abc import ABC, abstractmethod


class BindingsSerializer(object):
    def __init__(self, operation, env):
        self.operation = operation
        self.env = env


class OutputBinding(ABC):
    def __init__(self, operation, env):
        self.operation = operation
        self.env = env

    @abstractmethod
    def get_binding_type(self):
        """

        :return:
        """

    @abstractmethod
    def get_binding_name(self):
        """

        :return:
        """

    @abstractmethod
    def render_template(self):
        """

        :return:
        """

    @staticmethod
    def get_binding_direction():
        return "out"


class HTTPOutputBinding(OutputBinding):
    def get_binding_type(self):
        return "http"

    def get_binding_name(self):
        return "$return"

    def render_template(self):
        template = self.env.get_template("http-output-binding.jinja2")
        return template.render(binding_type=f'"{self.get_binding_type()}"',
                               binding_direction=f'"{self.get_binding_direction()}"',
                               return_variable_name=f'"{self.get_binding_name()}"')


class OutputBindingsSerializer(BindingsSerializer):
    def _get_output_binding(self):
        # ToDo - this has to become generic
        return HTTPOutputBinding(self.operation, self.env)

    def __str__(self):
        return self._get_output_binding().render_template()


class InputBindingsSerializer(BindingsSerializer):

    def __str__(self):
        return '"TO FILL"'
