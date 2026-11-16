variable "instance_type" {
  description = "EC2 인스턴스 타입"
  default     = "t3.micro"
}

variable "subnet_id" {
  description = "서브넷 ID"
  default     = "subnet-026db834a477f714c"
}
variable "my_ip_cidr" {
  description = "SSH 접속을 허용할 내 IP (CIDR, 예: 1.2.3.4/32)"
  type        = string
}
