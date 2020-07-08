
### Azure Functions Python code generation configuration
- Please don't edit this section unless you're re-configuring how the Azure Functions generator plugs in to AutoRest
AutoRest needs the below config to pick this up as a plug-in - 
see [AutoRest-extension.md](https://github.com/Azure/autorest/blob/master/docs/developer/architecture/AutoRest-extension.md) 
for more information.

```yaml
pass-thru:
  - model-deduplicator
  - subset-reducer
# version: 3.0.6258
use-extension:
  "@autorest/modelerfour": "4.15.375"

modelerfour:
  group-parameters: true
  flatten-models: true
  flatten-payloads: true
  resolve-schema-name-collisons: true
  always-create-content-type-parameter: true
  multiple-request-parameter-flattening: false
  naming:
    parameter: snakecase
    property: snakecase
    operation: snakecase
    operationGroup:  pascalcase
    choice:  pascalcase
    choiceValue:  snakecase
    constant:  snakecase
    constantParameter:  snakecase
    type:  pascalcase
    local: _ + snakecase
    global: snakecase
    preserve-uppercase-max-length: 6
    override:
      $host: $host
      base64: base64
      IncludeAPIs: include_apis


pipeline:
  python:
    # doesn't process anything, just makes it so that the 'python:' config section loads early.
    pass-thru: true
    input: openapi-document/multi-api/identity

  modelerfour:
    # in order that the modelerfour/flattener/grouper/etc picks up
    # configuration nested under python: in the user's config,
    # we have to make modeler four pull from the 'python' task.
    input: python

  python/m2r:
    input: modelerfour/identity

  python/namer:
    input: python/m2r

  python/codegen:
    input: python/namer
    output-artifact: python-files

  python/codegen/emitter:
    input: codegen
    scope: scope-codegen/emitter

scope-codegen/emitter:
    input-artifact: python-files
    output-uri-expr: $key

output-artifact: python-files
```