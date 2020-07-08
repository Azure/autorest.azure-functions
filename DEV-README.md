# project-stencil

### Prerequisites

1. Installing Python - Python 3.6+ is required to run this new autorest. 
   - You can install it using apt-get/yum on Linux
   - Homebrew on mac
   - Windows Store or Python.org on Windows
2. Install autorest v3 - Follow the documenation from Autorest team on [Installing Autorest](https://github.com/Azure/autorest/blob/master/docs/installing-autorest.md)

### Generate

Make sure to do an "autorest --reset" if you don't have a core v3 >= 3.0.6258. You can find the latest release [here](https://github.com/Azure/autorest.python/releases).

You must pass `--use` to the tgz file. current one at time of this article is:

Example:
```bash
# git clone <git:path-to-project-stencil> autorest.azurefuncions
$ cd autorest.azurefuncions
$ autorest \
--input-file:<path-to-swagger.json> \
--use:. \
--output-folder:<path-to-output-folder-for-azure-function-app> \
--verbose \
--no-async \
--language:python
```

#### AutoRest.AzureFunctions Command Line Interface Documentation
This section described the Autorest.AzureFunctions-specific command line interface. For Autorest's CLI documentation, please refer to [AutoRest Command Line Interface Documentation
](https://github.com/Azure/autorest/blob/master/docs/user/command-line-interface.md#autorest-command-line-interface-documentation).

|Option  | Description |
|------------------|-------------|
|`--language`| Choose the language to generate the Azure Functions stub. |


### Running tests


##### Running vanilla tests