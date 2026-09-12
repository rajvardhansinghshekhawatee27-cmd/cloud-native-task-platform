resource "aws_ecr_repository" "task_platform" {
  name                 = "cloud-native-task-platform"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = false
  }

  force_delete = false
}