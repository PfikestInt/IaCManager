locals {
  resource_group_tags = {
    product                  = var.product
    iac_deployed_by          = var.deployed_by
    iac_last_deployment_time = var.last_deployment_time
    iac_version              = var.iac_version
    iac_repository           = var.iac_repository
    description              = var.description
  }

  tags = {
    product     = var.product
    description = var.description
  }
}
