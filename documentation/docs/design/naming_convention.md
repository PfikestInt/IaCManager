# Naming Convention

The naming convention follows the following pattern:

[ _Resource Type_ ]-[ _Environment_ ]-[ _Role_ ]-[ _Region_ ]-[ _Unique Identifier_ ]

- _Resource Type_: a standard Microsoft abbreviation for the resource
- _Environment_: **d** for dev, **t** for test, **s** for stage, **p** for prod
- _Role_: a descriptive purpose identifier
- _Region_: the Azure region
- _Unique Identifier_: a three digit integer

The names will be built dynamically using Terraform variables.

- _Resource Type_: will be hard coded into the module definition
- _Environment_: will be provided per environment branch
- _Role_: will be provided per resource definition
- _Region_: will be provided per resource definition
- _Unique Identifier_: will be provided per resource definition
