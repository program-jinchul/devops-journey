resource "aws_instance" "main_aws_instance" {
  ami                    = "ami-062cf18d655c0b1e8"
  instance_type          = var.instance_type
  subnet_id              = var.subnet_id
  vpc_security_group_ids = [aws_security_group.main.id]

  tags = {
    Name = "jinchul-instance-tf"
  }
}

resource "aws_security_group" "main" {
    vpc_id = var.vpc_id

    ingress {
    protocol   = "tcp"
    from_port  = 22
    to_port    = 22
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    protocol   = "tcp"
    from_port  = 80
    to_port    = 80
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    protocol   = "-1"
    from_port  = 0
    to_port    = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "jinchul-security-group-tf"
  }
}