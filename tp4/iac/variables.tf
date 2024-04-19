variable "location" {
  description = "Emplacement Azure pour les ressources"
  type        = string
  default     = "france central"
}

variable "rgroup" {
  description = "ressource groupe name"
  type        = string
  default     = "ADDA84-CTP"
}


variable "vnetwork" {
  description = "ressource groupe name"
  type        = string
  default     = "network-tp4"
}
