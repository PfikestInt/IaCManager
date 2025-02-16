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
  Pipeline->>Azure: create federated credential for develop branch
  Azure->>Pipeline: credential created
  Pipeline->>GitHub: add client id secret to target repo
  GitHub->>Pipeline: secret added
  Pipeline->>GitHub: add subscription id secret to target repo
  GitHub->>Pipeline: secret added
  Pipeline->>GitHub: add tenant id secret to target repo
  GitHub->>Pipeline: secret added 
  Pipeline->>Python: add resource group to history
  Python->>Pipeline: history updated
  Pipeline->>git: commit history change
  git->>Pipeline: history committed
  Pipeline->>Documentation: rebuild documentation
```
