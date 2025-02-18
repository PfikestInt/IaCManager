variable "subscription_id" {
  description = "The UUID identifying the Azure subscription."
  type        = string
}

variable "location" {
  description = "The Azure region used for deployment."
  type        = string
}

variable "environment" {
  description = "The environment code in the resource names."
  type        = string
}

variable "role" {
  description = "The role description in the resource names."
  type        = string
}

variable "counter" {
  description = "The unique identification counter in the resource names."
  type        = string
}

variable "product" {
  description = "Product name used in tags."
  type        = string
}

variable "deployed_by" {
  description = "GitHub user who ran the deployment--used in resource group tags."
  type        = string
}

variable "last_deployment_time" {
  description = "Last time the deployment was run--used in resource group tags."
  type        = string
}

variable "iac_version" {
  description = "The version tag of the deployment--used in resource group tags.."
  type        = string
}

variable "iac_repository" {
  description = "The GitHub repository the infrastructure was deployed from--used in resource group tags.."
  type        = string
}

variable "description" {
  description = "A description of the reason for existence--used in resource group tags.."
  type        = string
}

variable "repository_name" {
  description = "The organization/repo name to use for the federated credentials."
  type        = string
}
