import configparser

config = configparser.ConfigParser()
config.read('azure-functions-serialization-configuration.ini')


def get_serializer_configured():
    if 'CONFIGURATION' in config:
        return config['CONFIGURATION']['SERIALIZER'] if 'SERIALIZER' in config[
            'CONFIGURATION'] else get_default_serializer()

    return get_default_serializer()


def get_default_serializer():
    return config['DEFAULT']['SERIALIZER']


class AzureFunctionsConfigurations:
    @staticmethod
    def get_default_trigger_type():
        return config['DEFAULT']['TRIGGER_TYPE']
