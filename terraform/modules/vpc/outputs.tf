output "vpc_id" {
    description = "생성된 VPC의 ID"
    value       = aws_vpc.main.id
}

output "subnet_id" {
    description = "생성된 Subnet의 ID"
    value       = aws_subnet.main_subnet.id
}