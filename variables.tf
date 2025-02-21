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

variable "repository_name" {
  description = "The organization/repo name to use for the federated credentials."
  type        = string
}
