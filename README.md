# CICD Pipeline for Dockerized Applications
CI/CD Pipeline for Dockerized Applications Using AWS/Jenkins/Kubernetes
# Pipeline Architecture

GitHub Repo with Simple Application Code / Jenkinsfile / Docker File / Helm Chart etc.
GitHub WebHooks triggers the Jenkins Job on Commit to the Repo.
Unit Testcases are Run and Static application Security Testing (SAST) is carried out with and SonarQube.
Docker Image is Built/Tagged (Using commit hash) and Pushed to ECR.
Jenkins CI server Assumes Cross Account Role to connect to EKS account .
Helm Lint is performed and Helm packaging is done. 
Application deployed in EKS Cluster with Rolling Update Deployment Strategy 
Email and Slack Notification is sent upon Successful/Failure of Jenkins Pipeline
