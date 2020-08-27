# project-stencil

Generates Azure Functions from Open API Spec.

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

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit [https://cla.microsoft.com](https://cla.microsoft.com).

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repositories using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
