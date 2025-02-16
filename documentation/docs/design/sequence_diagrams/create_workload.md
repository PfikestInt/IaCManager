# Create Workload
The sequence diagram for the happy-path life cycle of a create workload repository job is presented below:

``` mermaid
sequenceDiagram
  autonumber
  Person->>Variable: set repo parameters
  Variable->>Person: parameters set
  Person->>Pipeline: execute
  Pipeline->>GitHub: create repo from template
  GitHub->>Pipeline: repo created
  Pipeline->>Repository: create config file
  Repository->>Pipeline: config file created
  Pipeline->>Python: add repo to history
  Python->>Pipeline: history updated
  Pipeline->>git: commit history change
  git->>Pipeline: history committed
  Pipeline->>Documentation: rebuild documentation
```
