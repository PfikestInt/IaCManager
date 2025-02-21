locals {
  tags = {
    product        = var.product
    description    = var.description
    deploymentType = "IaC v1"
  }
}
