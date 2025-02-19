data "azurerm_subscription" "current" {
}

resource "azurerm_user_assigned_identity" "managed_identity" {
  location            = var.location
  name                = var.location == "eastus" ? "id-${var.environment}-github-001" : "id-${var.environment}-github-${var.location}-001"
  resource_group_name = var.location == "eastus" ? "rg-${var.environment}-${var.role}-${var.counter}" : "rg-${var.environment}-${var.role}-${var.location}-${var.counter}"
  tags                = local.tags
}
yo test
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

resource "azurerm_resource_group_policy_assignment" "azure_cis_policy" {
  resource_group_id    = module.resource_group.resource_id
  policy_definition_id = "/providers/Microsoft.Authorization/policySetDefinitions/fe7782e4-6ff3-4e39-8d8a-64b6f7b82c85"
  name                 = "CIS Azure Foundations v2.1.0"

  # 2025-02-18: Accommodate a bug in the definition
  parameters = <<-EOT
  {
    "operationName-c5447c04-a4d7-4ba8-a263-c9ee321a6858": { 
      "value": "Microsoft.Authorization/policyAssignments/write" 
    },
    "operationName-b954148f-4c11-4c38-8221-be76711e194a": {
      "value": "Microsoft.Sql/servers/firewallRules/write"
    }
  }
  EOT
}
