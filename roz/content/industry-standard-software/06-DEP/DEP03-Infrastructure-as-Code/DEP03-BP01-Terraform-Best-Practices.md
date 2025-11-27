# DEP03-BP01: Terraform Best Practices

Quản lý infrastructure với Terraform.

## Project Structure

```
terraform/
├── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── terraform.tfvars
│   ├── staging/
│   └── production/
├── modules/
│   ├── vpc/
│   ├── ecs/
│   └── rds/
└── README.md
```

## Module Structure

```
modules/vpc/
├── main.tf         # Resources
├── variables.tf    # Input variables
├── outputs.tf      # Output values
└── README.md       # Documentation
```

## Example Module

```hcl
# modules/vpc/variables.tf
variable "name" {
  description = "VPC name"
  type        = string
}

variable "cidr" {
  description = "VPC CIDR block"
  type        = string
  default     = "10.0.0.0/16"
}

variable "environment" {
  description = "Environment name"
  type        = string
}

# modules/vpc/main.tf
resource "aws_vpc" "main" {
  cidr_block           = var.cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name        = var.name
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_subnet" "public" {
  count             = 2
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(var.cidr, 8, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]

  tags = {
    Name = "${var.name}-public-${count.index + 1}"
  }
}

# modules/vpc/outputs.tf
output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main.id
}

output "public_subnet_ids" {
  description = "Public subnet IDs"
  value       = aws_subnet.public[*].id
}
```

## Using Modules

```hcl
# environments/production/main.tf
terraform {
  required_version = ">= 1.0"

  backend "s3" {
    bucket = "my-terraform-state"
    key    = "production/terraform.tfstate"
    region = "ap-southeast-1"
  }
}

module "vpc" {
  source = "../../modules/vpc"

  name        = "production-vpc"
  cidr        = "10.0.0.0/16"
  environment = "production"
}

module "ecs" {
  source = "../../modules/ecs"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.public_subnet_ids
}
```

## State Management

```hcl
# Remote state (recommended)
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "env/terraform.tfstate"
    region         = "ap-southeast-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}
```

## Variables & Secrets

```hcl
# variables.tf
variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true  # Won't show in logs
}

# terraform.tfvars (gitignored)
db_password = "secret123"

# Or use environment variables
# export TF_VAR_db_password="secret123"
```

## Naming Conventions

| Resource | Convention | Example |
|----------|------------|---------|
| Resources | snake_case | `aws_instance.web_server` |
| Variables | snake_case | `var.instance_type` |
| Outputs | snake_case | `output.vpc_id` |
| Modules | kebab-case | `module "my-vpc"` |

## Workflow

```bash
# Initialize
terraform init

# Format code
terraform fmt -recursive

# Validate
terraform validate

# Plan (preview changes)
terraform plan -out=tfplan

# Apply
terraform apply tfplan

# Destroy (careful!)
terraform destroy
```

## Checklist

- [ ] Remote state configured
- [ ] State locking enabled
- [ ] Modules for reusable components
- [ ] Variables documented
- [ ] Sensitive values marked
- [ ] Resources tagged
- [ ] terraform fmt in CI
