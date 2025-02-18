output "client_id" {
  value = azurerm_user_assigned_identity.managed_identity.principal_id
}
