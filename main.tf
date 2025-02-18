resource "azurerm_user_assigned_identity" "managed_identity" {
  location            = var.location
  name                = var.location == "eastus" ? "id-${var.environment}-github-001" : "id-${var.environment}-github-${var.location}-001"
  resource_group_name = var.location == "eastus" ? "rg-${var.environment}-${var.role}-${var.counter}" : "rg-${var.environment}-${var.role}-${var.location}-${var.counter}"
  tags                = local.tags
}

resource "azurerm_federated_identity_credential" "credentials" {
  name                = "github-main"
  resource_group_name = module.resource_group.name
  audience            = ["api://AzureADTokenExchange"]
  issuer              = "https://token.actions.githubusercontent.com"
  parent_id           = azurerm_user_assigned_identity.managed_identity.id
  subject             = "repo:${var.repository_name}:ref:refs/heads/main"
}

module "resource_group" {
  source   = "Azure/avm-res-resources-resourcegroup/azurerm"
  version  = "0.2.1"
  location = var.location
  name     = var.location == "eastus" ? "rg-${var.environment}-${var.role}-${var.counter}" : "rg-${var.environment}-${var.role}-${var.location}-${var.counter}"
  tags     = local.resource_group_tags
  role_assignments = {
    "roleassignment1" = {
      principal_id               = azurerm_user_assigned_identity.managed_identity.principal_id
      role_definition_id_or_name = "Contributor"
    },
    "roleassignment2" = {
      principal_id               = azurerm_user_assigned_identity.managed_identity.principal_id
      role_definition_id_or_name = "User Access Administrator"
    },
    "roleassignment3" = {
      principal_id               = azurerm_user_assigned_identity.managed_identity.principal_id
      role_definition_id_or_name = "Resource Policy Contributor"
    }
    "roleassignment3" = {
      principal_id               = azurerm_user_assigned_identity.managed_identity.principal_id
      role_definition_id_or_name = "Managed Identity Contributor"
    }
  }
}
