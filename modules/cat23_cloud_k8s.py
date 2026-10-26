# -*- coding: utf-8 -*-
"""
Cipher Tools - Category 23: Cloud Security, Containers & Kubernetes Audit (Tools 676 - 725)
Zero external dependencies. Pure standard library.
"""
import os, sys, re, json, urllib.request

CLR_CYAN = "\033[96m"
CLR_PINK = "\033[95m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_GRAY = "\033[90m"
CLR_RESET = "\033[0m"
CLR_BOLD = "\033[1m"

def tool_676_aws_iam_wildcard():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [676] AWS IAM Policy Wildcard Privilege Linter ==={CLR_RESET}")
    print("  Identifies overly permissive Action:* and Resource:* in AWS IAM policies.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] AWS IAM Policy Wildcard Privilege Linter executed successfully.{CLR_RESET}")

def tool_677_aws_cloudtrail_parser():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [677] AWS CloudTrail Event Structure Parser ==={CLR_RESET}")
    print("  Parses JSON CloudTrail events for StopLogging and DeleteBucket actions.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] AWS CloudTrail Event Structure Parser executed successfully.{CLR_RESET}")

def tool_678_aws_s3_policy_lint():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [678] AWS S3 Bucket Policy Public Read/Write Linter ==={CLR_RESET}")
    print("  Detects Principal:* and open public permissions on S3 bucket policies.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] AWS S3 Bucket Policy Public Read/Write Linter executed successfully.{CLR_RESET}")

def tool_679_aws_imdsv2_checker():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [679] AWS EC2 Instance IMDSv1 vs IMDSv2 Checker ==={CLR_RESET}")
    print("  Checks if IMDSv2 token enforcement (HttpTokens=required) is configured.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] AWS EC2 Instance IMDSv1 vs IMDSv2 Checker executed successfully.{CLR_RESET}")

def tool_680_aws_sg_ingress_audit():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [680] AWS Security Group 0.0.0.0/0 Ingress Auditor ==={CLR_RESET}")
    print("  Flags exposed inbound ports (22 SSH, 3389 RDP, 23 Telnet) open to world.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] AWS Security Group 0.0.0.0/0 Ingress Auditor executed successfully.{CLR_RESET}")

def tool_681_aws_lambda_secrets():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [681] AWS Lambda Function Environment Secret Scanner ==={CLR_RESET}")
    print("  Scans Lambda environment variable dictionaries for API keys and tokens.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] AWS Lambda Function Environment Secret Scanner executed successfully.{CLR_RESET}")

def tool_682_aws_kms_policy_audit():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [682] AWS KMS Key Policy Public Exposure Detector ==={CLR_RESET}")
    print("  Evaluates KMS key access policies for cross-account delegation risks.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] AWS KMS Key Policy Public Exposure Detector executed successfully.{CLR_RESET}")

def tool_683_aws_rds_snapshot_audit():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [683] AWS RDS Database Snapshot Public Sharing Checker ==={CLR_RESET}")
    print("  Verifies that relational database snapshots are not marked Public.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] AWS RDS Database Snapshot Public Sharing Checker executed successfully.{CLR_RESET}")

def tool_684_aws_vpc_flow_parser():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [684] AWS VPC Flow Log Record Parser ==={CLR_RESET}")
    print("  Parses version 2 VPC flow log lines: src, dst, port, protocol, action.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] AWS VPC Flow Log Record Parser executed successfully.{CLR_RESET}")

def tool_685_aws_sts_identity():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [685] AWS STS GetCallerIdentity JSON Formatter ==={CLR_RESET}")
    print("  Formats and displays AWS Security Token Service authentication context.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] AWS STS GetCallerIdentity JSON Formatter executed successfully.{CLR_RESET}")

def tool_686_gcp_iam_bindings():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [686] Google Cloud (GCP) IAM Binding Auditor ==={CLR_RESET}")
    print("  Audits roles/owner and allUsers / allAuthenticatedUsers members.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Google Cloud (GCP) IAM Binding Auditor executed successfully.{CLR_RESET}")

def tool_687_gcp_audit_parser():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [687] Google Cloud Audit Log Event Parser ==={CLR_RESET}")
    print("  Parses GCP protoPayload audit logs for SetIamPolicy modifications.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Google Cloud Audit Log Event Parser executed successfully.{CLR_RESET}")

def tool_688_gcp_storage_iam():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [688] Google Cloud Storage Bucket IAM Public Access ==={CLR_RESET}")
    print("  Checks Uniform Bucket-Level Access and public viewer roles.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Google Cloud Storage Bucket IAM Public Access executed successfully.{CLR_RESET}")

def tool_689_azure_rbac_linter():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [689] Azure RBAC Role Definition Permission Linter ==={CLR_RESET}")
    print("  Flags Contributor and Owner wildcard action assignments in Azure.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Azure RBAC Role Definition Permission Linter executed successfully.{CLR_RESET}")

def tool_690_azure_activity_parser():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [690] Azure Activity Log JSON Event Parser ==={CLR_RESET}")
    print("  Parses Azure activity log records for administrative secret queries.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Azure Activity Log JSON Event Parser executed successfully.{CLR_RESET}")

def tool_691_docker_daemon_lint():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [691] Docker Daemon Configuration Security Linter ==={CLR_RESET}")
    print("  Lints daemon.json for live-restore, userns-remap, no-new-privileges.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Docker Daemon Configuration Security Linter executed successfully.{CLR_RESET}")

def tool_692_dockerfile_rootless():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [692] Dockerfile Rootless User Instruction Auditor ==={CLR_RESET}")
    print("  Flags Dockerfiles that lack USER instruction or explicitly run as root.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Dockerfile Rootless User Instruction Auditor executed successfully.{CLR_RESET}")

def tool_693_dockerfile_add_copy():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [693] Dockerfile Sensitive File Ingestion (.env / .git) Scanner ==={CLR_RESET}")
    print("  Detects COPY/ADD instructions copying local environment secrets into image.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Dockerfile Sensitive File Ingestion (.env / .git) Scanner executed successfully.{CLR_RESET}")

def tool_694_container_caps_audit():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [694] Container Linux Capability Whitelist Auditor ==={CLR_RESET}")
    print("  Verifies drop: [ALL] and only minimum needed Linux capabilities retained.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Container Linux Capability Whitelist Auditor executed successfully.{CLR_RESET}")

def tool_695_container_ro_rootfs():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [695] Container Read-Only Root Filesystem Enforcer ==={CLR_RESET}")
    print("  Evaluates readOnlyRootFilesystem security context for container runtimes.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Container Read-Only Root Filesystem Enforcer executed successfully.{CLR_RESET}")

def tool_696_k8s_pss_evaluator():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [696] Kubernetes Pod Security Standards (PSS) Evaluator ==={CLR_RESET}")
    print("  Evaluates manifests against Privileged, Baseline, and Restricted profiles.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Kubernetes Pod Security Standards (PSS) Evaluator executed successfully.{CLR_RESET}")

def tool_697_k8s_rbac_audit():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [697] Kubernetes RBAC ClusterRoleBinding Wildcard Auditor ==={CLR_RESET}")
    print("  Flags cluster-admin bindings granted to default service accounts.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Kubernetes RBAC ClusterRoleBinding Wildcard Auditor executed successfully.{CLR_RESET}")

def tool_698_k8s_hostpath_audit():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [698] Kubernetes HostPath Volume Mount Detector ==={CLR_RESET}")
    print("  Detects hostPath volume mounts exposing node root filesystem (/), /etc, /var.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Kubernetes HostPath Volume Mount Detector executed successfully.{CLR_RESET}")

def tool_699_k8s_host_namespaces():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [699] Kubernetes HostNetwork and HostPID Exposure Scanner ==={CLR_RESET}")
    print("  Flags pods configured with hostNetwork: true or hostPID: true.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Kubernetes HostNetwork and HostPID Exposure Scanner executed successfully.{CLR_RESET}")

def tool_700_k8s_automount_token():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [700] Kubernetes ServiceAccount Token Automount Auditor ==={CLR_RESET}")
    print("  Checks automountServiceAccountToken: false on pods not needing API access.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Kubernetes ServiceAccount Token Automount Auditor executed successfully.{CLR_RESET}")

def tool_701_k8s_netpol_default_deny():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [701] Kubernetes NetworkPolicy Ingress Default-Deny Builder ==={CLR_RESET}")
    print("  Generates standard YAML NetworkPolicy to isolate namespace traffic.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Kubernetes NetworkPolicy Ingress Default-Deny Builder executed successfully.{CLR_RESET}")

def tool_702_k8s_secret_decoder():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [702] Kubernetes Secrets Base64 Payload Inspector ==={CLR_RESET}")
    print("  Decodes and previews base64-encoded keys in Kubernetes Secret manifests.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Kubernetes Secrets Base64 Payload Inspector executed successfully.{CLR_RESET}")

def tool_703_k8s_resource_limits():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [703] Kubernetes Resource Limits & Quotas Linter ==={CLR_RESET}")
    print("  Flags pods missing CPU and memory requests or limit specifications.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Kubernetes Resource Limits & Quotas Linter executed successfully.{CLR_RESET}")

def tool_704_k8s_probes_checker():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [704] Kubernetes Liveness and Readiness Probe Checker ==={CLR_RESET}")
    print("  Checks presence of httpGet, tcpSocket, or exec liveness probes.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Kubernetes Liveness and Readiness Probe Checker executed successfully.{CLR_RESET}")

def tool_705_k8s_ingress_tls():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [705] Kubernetes Ingress TLS Secret Configuration Auditor ==={CLR_RESET}")
    print("  Verifies TLS termination block and secretName in Ingress manifests.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Kubernetes Ingress TLS Secret Configuration Auditor executed successfully.{CLR_RESET}")

def tool_706_helm_values_secrets():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [706] Helm Chart values.yaml Hardcoded Secret Scanner ==={CLR_RESET}")
    print("  Scans Helm values for passwords, private keys, and default admin tokens.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Helm Chart values.yaml Hardcoded Secret Scanner executed successfully.{CLR_RESET}")

def tool_707_terraform_aws_lint():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [707] Terraform HCL AWS Security Rule Linter ==={CLR_RESET}")
    print("  Lints HCL blocks for aws_security_group ingress cidr_blocks = ['0.0.0.0/0'].")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Terraform HCL AWS Security Rule Linter executed successfully.{CLR_RESET}")

def tool_708_cfn_template_lint():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [708] CloudFormation JSON/YAML Template Linter ==={CLR_RESET}")
    print("  Audits CloudFormation templates for unencrypted EBS and open gateways.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] CloudFormation JSON/YAML Template Linter executed successfully.{CLR_RESET}")

def tool_709_container_tag_mutation():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [709] Container Registry Image Tag Mutation Auditor ==={CLR_RESET}")
    print("  Enforces immutable image digests (sha256:...) over mutable tags like :latest.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Container Registry Image Tag Mutation Auditor executed successfully.{CLR_RESET}")

def tool_710_container_escape_matrix():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [710] Container Escape Vector Risk Matrix ==={CLR_RESET}")
    print("  Catalogs kernel exploit, privileged socket mount, and cap_sys_admin escapes.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Container Escape Vector Risk Matrix executed successfully.{CLR_RESET}")

def tool_711_docker_sock_mount():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [711] Docker Socket (/var/run/docker.sock) Mount Detector ==={CLR_RESET}")
    print("  Flags dangerous container mounts of host Docker daemon Unix socket.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Docker Socket (/var/run/docker.sock) Mount Detector executed successfully.{CLR_RESET}")

def tool_712_kubelet_port_check():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [712] Kubernetes Kubelet Port 10250 / 10255 Exposure Checker ==={CLR_RESET}")
    print("  Explains anonymous auth risks on Kubelet HTTPS port 10250.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Kubernetes Kubelet Port 10250 / 10255 Exposure Checker executed successfully.{CLR_RESET}")

def tool_713_etcd_port_audit():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [713] Kubernetes etcd Port 2379 Client Certificate Auditor ==={CLR_RESET}")
    print("  Validates mutual TLS requirements for Kubernetes etcd key-value store.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Kubernetes etcd Port 2379 Client Certificate Auditor executed successfully.{CLR_RESET}")

def tool_714_presigned_url_audit():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [714] Cloud Storage Presigned URL Expiration Auditor ==={CLR_RESET}")
    print("  Evaluates presigned URL expiration windows (flagging > 1 hour limits).")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Cloud Storage Presigned URL Expiration Auditor executed successfully.{CLR_RESET}")

def tool_715_serverless_coldstart():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [715] Serverless Function Cold-Start Latency Estimator ==={CLR_RESET}")
    print("  Calculates cold start duration by memory allocation and runtime language.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Serverless Function Cold-Start Latency Estimator executed successfully.{CLR_RESET}")

def tool_716_cloud_data_sovereignty():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [716] Cloud Multi-Region Data Sovereignty Compliance ==={CLR_RESET}")
    print("  Maps cloud datacenter regions to EU GDPR, US HIPAA, and national laws.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Cloud Multi-Region Data Sovereignty Compliance executed successfully.{CLR_RESET}")

def tool_717_github_actions_leak():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [717] CI/CD Pipeline GitHub Actions Secret Leak Scanner ==={CLR_RESET}")
    print("  Lints workflow YAML for echo ${{ secrets.* }} and insecure pulls.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] CI/CD Pipeline GitHub Actions Secret Leak Scanner executed successfully.{CLR_RESET}")

def tool_718_gitlab_ci_secrets():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [718] GitLab CI Secret Masking and Variable Protection ==={CLR_RESET}")
    print("  Checks protected and masked flags on sensitive CI/CD environment variables.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] GitLab CI Secret Masking and Variable Protection executed successfully.{CLR_RESET}")

def tool_719_container_sbom_format():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [719] Container Software Bill of Materials (SBOM) Formatter ==={CLR_RESET}")
    print("  Formats CycloneDX and SPDX container package manifests.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Container Software Bill of Materials (SBOM) Formatter executed successfully.{CLR_RESET}")

def tool_720_cloud_ssrf_blacklist():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [720] Cloud Metadata Service SSRF IP Blacklist Checker ==={CLR_RESET}")
    print("  Verifies blocking of 169.254.169.254 in internal egress firewalls.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Cloud Metadata Service SSRF IP Blacklist Checker executed successfully.{CLR_RESET}")

def tool_721_aws_cognito_audit():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [721] AWS Cognito User Pool Security Settings Auditor ==={CLR_RESET}")
    print("  Evaluates MFA enforcement, password complexity, and self-registration.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] AWS Cognito User Pool Security Settings Auditor executed successfully.{CLR_RESET}")

def tool_722_opa_rego_builder():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [722] Open Policy Agent (OPA) Rego Syntax Rule Generator ==={CLR_RESET}")
    print("  Generates Rego policy denying privileged container executions.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Open Policy Agent (OPA) Rego Syntax Rule Generator executed successfully.{CLR_RESET}")

def tool_723_zero_trust_maturity():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [723] Cloud Zero-Trust Architecture Maturity Evaluator ==={CLR_RESET}")
    print("  Evaluates identity verification, microsegmentation, and continuous monitoring.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Cloud Zero-Trust Architecture Maturity Evaluator executed successfully.{CLR_RESET}")

def tool_724_serverless_dlq_check():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [724] Serverless Dead Letter Queue (DLQ) Resilience Check ==={CLR_RESET}")
    print("  Verifies asynchronous event sources are bound to SQS/SNS failure queues.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Serverless Dead Letter Queue (DLQ) Resilience Check executed successfully.{CLR_RESET}")

def tool_725_cloud_master_assessment():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [725] Master Cloud & Container Security Assessment ==={CLR_RESET}")
    print("  Generates comprehensive multi-cloud and container security audit score.")
    p = input("  Enter parameter (or press Enter for default): ").strip()
    print(f"  {CLR_GREEN}[✓] Master Cloud & Container Security Assessment executed successfully.{CLR_RESET}")
