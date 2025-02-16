# Environment Management

The sequence diagram for the happy-path life cycle of a deployment is presented below:

``` mermaid
sequenceDiagram
  autonumber
  Person->>GitHub: feature branch from environment branch
  GitHub->>Person: feature branch created
  Person->>IDE: implement IaC
  IDE->>Person: commit features
  Person->>GitHub: pull request to merge to environment branch
  GitHub->>Pipeline: pull TerraformHub modules
  Pipeline->>Terraform: build plan
  Terraform->>Pipeline: plan built
  Pipeline->>Pull Request: append plan as comment
  Pull Request->>Person: review plan
  Person->>Pipeline: approve deployment
  Pipeline->>Terraform: deploy
  Terraform->>Azure: deploy
```
