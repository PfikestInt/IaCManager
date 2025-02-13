# Create Repository

The prerequisites are:

1. IaC repository template exists.
2. Key Vault with Service Principal credentials has been populated.

The sequence diagram for the happy-path life cycle of a create repository job is presented below:

``` mermaid
sequenceDiagram
  autonumber
  Person->>Variable: set repo name
  Variable->>Person: repo name
  Person->>Pipeline: execute
  Pipeline->>GitHub: create repo from template
  GitHub->>Pipeline: repo created
  Pipeline->>Key Vault: fetch develop credentials
  Key Vault->>Pipeline: develop credentials
  Pipeline->>GitHub: setup develop environment secrets
  GitHub->>Pipeline: secrets populated
  Pipeline->>Key Vault: fetch test credentials
  Key Vault->>Pipeline: test credentials
  Pipeline->>GitHub: setup test environment secrets
  GitHub->>Pipeline: secrets populated
  Pipeline->>Key Vault: fetch stage credentials
  Key Vault->>Pipeline: stage credentials
  Pipeline->>GitHub: setup stage environment secrets
  GitHub->>Pipeline: secrets populated
  Pipeline->>Key Vault: fetch prod credentials
  Key Vault->>Pipeline: prod credentials
  Pipeline->>GitHub: setup prod environment secrets
  GitHub->>Pipeline: secrets populated
```
