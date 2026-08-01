variable "subnet_id" {
    description = "EC2를 배치할 서브넷 ID"
}

variable "security_group_id" {
    description = "EC2에 적용할 Security Group ID"
}

variable "instance_type" {
    description = "EC2 인스턴스 타입"
    default     = "t3.micro"
}

variable "vpc_id" {
    description = "EC2를 배치할 VPC ID"
}