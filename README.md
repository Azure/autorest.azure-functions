# Azure Functions code generator for Open API Specs

f.k.a: Project Stencil: Generate Azure Functions from Open API Spec across multiple languages.

## Supported Languages

To see the language specific implementations, go to their respective repositories.

|Language|Repo|
| :-----| :----|
|C#|<https://github.com/Azure/autorest.azure-functions-csharp>|
|Java|<https://github.com/Azure/autorest.azure-functions-java>|
|Python|<https://github.com/Azure/autorest.azure-functions-python>|
|TypeScript|<https://github.com/Azure/autorest.azure-functions-typescript>|

## Inspiration

Do you build HTTP APIs or have customers who do? Have you heard from them that the process of building apps that make use of well-designed, reusable (and thus, marketable) APIs is painful? We've heard from numerous premier customers that they wished their APIs could have been designed better before they were built, but that the tools and frameworks favored code over design and thus, mitigated broad API comprehension and thus, consumption.

Project Stencil fills a gap between API designers and API developers and aims to enable citizen developers who feel unempowered to impact the API design process. By taking advantage of excellence in other products like AutoRest, Functions, API Management, and Visual Studio Code, Stencil enables design-first API development using OpenAPI Specification-driven serverless API stub generation. Customers can get started on implementation the moment they're in agreement on API design with their business partners, using any language supported by Azure Functions to satisfy their implementation goals.

The best part? Developers can work with their business analyst or citizen dev colleagues to design an empty API using Azure API management, then use the API Management extension for Visual Studio Code to generate their serverless stubs. With Project Stencil, teams can design in the Azure portal, scaffold in Visual Studio Code, and implement using Azure Functions, with confidence and visibility that the design drives the development.

## Prerequisites

To run Stencil on your box today, you need to have NodeJS and NPM installed. We rely on autorest (Microsoft's OpenAPI specification generator) and you need to install it on your box.

```bash
npm install -g autorest
```

## Usage

CLI: 

Autorest works on all the platforms and the following CLI example is from Windows. Also, the `--input-file` parameter can take in a URL as well.

#### TypeScript

```bash
autorest --azure-functions-typescript --input-file:C:\\path\\to\\spec.json --output-folder:./generated-azfunctions --version:3.0.6314 --no-namespace-folders:true
```

#### Python

```bash
autorest --azure-functions-python --input-file:C:\\path\\to\\spec.json  --output-folder:./generated-azfunctions --version:3.0.6314 --no-namespace-folders:true
```

#### Java

```bash
autorest --azure-functions-java --input-file:C:\\path\\to\\spec.json --output-folder:./generated-azfunctions --version:3.0.6314 --namespace:CovidScreeningNamespace
```

#### C#

```bash
autorest --azure-functions-csharp --input-file:C:\\path\\to\\spec.json --output-folder:./generated-azfunctions --version:3.0.6314 --namespace:CovidScreeningNamespace
```

Once you create the function app folders, you can open the function app in VSCode. Once opened, Azure Function Extension for VSCode would detect the app as a Functions App. If it fails to detect it as a functions app automatically, you can use the extension to detect it.

Note:
- Please install Java and python if you are going to create Python and Java functions as the plugins need them to run itself.
- Make sure you have Azure-Functions-Core-Tools installed on the box to use the generated functions.
- There is a bug in C# generator if you set the output-folder as a simple string. Please add `./` to make sure that the output folder is of URL format.

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit [https://cla.microsoft.com](https://cla.microsoft.com).

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repositories using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
