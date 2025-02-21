# Create Resource Group

The prerequisites are:

1. IaC repository template exists.

The sequence diagram for the happy-path life cycle of a create resource group job is presented below:

``` mermaid
sequenceDiagram
  autonumber
  Person->>Parameters: set repo parameters
  Parameters->>Person: parameters set
  Person->>Pipeline: execute
  Pipeline->>Azure: create resource group
  Azure->>Pipeline: resource group created
  Pipeline->>Azure: create managed identity
  Azure->>Pipeline: managed identity created
  Pipeline->>Azure: create federated credential for main branch
  Azure->>Pipeline: credential created
  Pipeline->>Azure: create federated credential for terraform-apply environment
  Azure->>Pipeline: credential created
```
