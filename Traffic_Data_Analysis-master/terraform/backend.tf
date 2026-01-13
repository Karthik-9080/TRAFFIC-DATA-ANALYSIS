terraform {
  backend "s3" {
    bucket         = "traffic-accident-tfstate-aswin"
    key            = "traffic-ec2/terraform.tfstate"
    region         = "ap-south-1"
    encrypt        = true
  }
}
