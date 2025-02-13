# Signature IaC

## Repository Layout

There will be two prebuilt repositories:

- TerraformHub: A set of prebuilt Terraform modules for creating commonly used resources.
- WorkloadTemplate: A standardized repository structure from which workload IaC repositories will be derived.

``` mermaid
stateDiagram-v2
    state Prebuilt {
        WorkloadTemplate --> Code
        TerraformHub --> Pipeline
    }

    state WorkloadRepository {
        Code --> Pipeline
        Pipeline --> ResourceGroup
    }

    state Azure {
        ResourceGroup
    }
```

## Environment Branches

The environments within a workload IaC repository are managed using a branching scheme where definitions common to all environments are stored in Main and inherited by the individual environment branches where environment specific definitions can be implemented.

``` mermaid
stateDiagram-v2
    Main --> Develop
    Main --> Test
    Main --> Stage
    Main --> Prod
    Main --> Feature/Main
    Develop --> Feature/Develop
    Test --> Feature/Test
    Stage --> Feature/Stage
    Prod --> Feature/Prod
    
    Feature/Main --> Main
    Feature/Develop --> Develop
    Feature/Test --> Test
    Feature/Stage --> Stage
    Feature/Prod --> Prod
```

## Pipelines

### Create Workload Pipeline

The Create Workload pipeline is used to create a standardized repository in which an IaC implementation can be defined and managed. This pipeline is also responsible for populating the environmental secrets that provide the credentials for each of the environment branches.

### Deployment Pipeline

The Deployment pipeline is triggered upon approval of a pull request merging changes into a branch.  It creates a deployment plan and places the plan in the pull request as a comment for review. Following the review, the deployment stage of the pipeline can either be executed of canceled.

