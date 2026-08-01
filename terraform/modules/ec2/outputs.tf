output "instance_id" {
    description = "생성된 Instance ID"
    value       = aws_instance.main_aws_instance.id
}