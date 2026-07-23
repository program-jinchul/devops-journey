terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "ap-northeast-2"
}

resource "aws_instance" "web_server" {
  ami           = "ami-062cf18d655c0b1e8"
  instance_type = var.instance_type
  subnet_id     = var.subnet_id

  tags = {
    Name = "jinchul-terraform-ec2"
  }
}