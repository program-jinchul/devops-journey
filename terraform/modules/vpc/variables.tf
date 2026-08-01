variable "vpc_cidr" {
    description = "VPC CIDR 블록"
    default     = "10.0.0.0/16"
}

variable "subnet_cidr" {
    description = "Subnet CIDR 블록"
    default     = "10.0.1.0/24"
}

variable "availability_zone" {
    description = "가용영역"
    default     = "ap-northeast-2a"
}