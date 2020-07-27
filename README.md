# project-stencil

See [here](https://github.com/Azure/autorest.python/wiki/Generating-with-autorest-for-python-v5.0.0)


### Autorest plugin configuration
- Please don't edit this section unless you're re-configuring how the powershell extension plugs in to AutoRest
AutoRest needs the below config to pick this up as a plug-in - see https://github.com/Azure/autorest/blob/master/docs/developer/architecture/AutoRest-extension.md

#### Azure Functions Python code generation configuration

```yaml $(language) == "python"
require: $(this-folder)/config/python/readme.md
```

#### Azure Functions C# code generation configuration

```yaml $(language) == "csharp"
require: $(this-folder)/config/csharp/readme.md
```

#### Azure Functions Java code generation configuration

```yaml $(language) == "java"
require: $(this-folder)/config/java/readme.md
```

#### Azure Functions JavaScript code generation configuration

```yaml $(language) == "javascript"
require: $(this-folder)/config/javascript/readme.md
```

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
