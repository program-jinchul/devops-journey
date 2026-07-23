output "instance_id" {
  description = "EC2 인스턴스 ID"
  value       = aws_instance.web_server.id
}

output "public_ip" {
  description = "EC2 퍼블릭 IP"
  value       = aws_instance.web_server.public_ip
}