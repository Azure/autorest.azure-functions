# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from abc import ABC, abstractmethod


class TriggerSerializer(object):
    def __init__(self, operation, env):
        self.operation = operation
        self.env = env


class InputTriggerSerializer(TriggerSerializer):
    def _get_input_trigger(self):
        # ToDo - this has to become generic
        return HTTPInputTrigger(self.operation, self.env)

    def __str__(self) -> str:
        trigger = self._get_input_trigger()
        return trigger.render_template()


class Trigger(ABC):
    def __init__(self, operation, env):
        self.operation = operation
        self.env = env

    @abstractmethod
    def get_trigger_type(self):
        """

        :return:
        """

    @abstractmethod
    def get_trigger_name(self):
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
        return "in"


class HTTPInputTrigger(Trigger):
    def get_trigger_type(self):
        return "httpTrigger"

    def get_trigger_name(self):
        return "req"

    def _get_http_method(self):
        return str(self.operation.method).lower()

    @staticmethod
    def _get_http_authentication():
        # ToDo - needs to be extended
        return 'anonymous'

    def _get_http_name(self):
        return self.operation.name

    def _get_http_description(self):
        return self.operation.description

    def _get_http_parameters(self):
        return self.operation.parameters

    def _get_http_responses(self):
        return self.operation.responses

    def _get_route(self):
        return str(self.operation.url).strip('/')

    def render_template(self):
        template = self.env.get_template("http-trigger.jinja2")

        return template.render(authentication_level=f'"{self._get_http_authentication()}"',
                               trigger_direction=f'"{self.get_binding_direction()}"',
                               trigger_type=f'"{self.get_trigger_type()}"',
                               request_variable_name=f'"{self.get_trigger_name()}"',
                               methods=f'"{self._get_http_method()}"',
                               route=f'"{self._get_route()}"')
