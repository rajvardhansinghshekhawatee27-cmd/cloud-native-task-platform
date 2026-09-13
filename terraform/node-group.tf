resource "aws_eks_node_group" "main" {
  cluster_name    = aws_eks_cluster.main.name
  node_group_name = "task-platform-nodes"
  node_role_arn   = aws_iam_role.eks_node.arn

  subnet_ids = aws_subnet.public[*].id

  instance_types = ["t3.small"]

  scaling_config {
    desired_size = 1
    min_size     = 1
    max_size     = 2
  }

  capacity_type = "ON_DEMAND"

  disk_size = 20

  depends_on = [
    aws_iam_role_policy_attachment.eks_node_worker_policy,
    aws_iam_role_policy_attachment.eks_node_ecr_policy,
    aws_iam_role_policy_attachment.eks_node_cni_policy
  ]

  tags = {
    Name = "task-platform-node"
  }
}
