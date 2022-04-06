# CICD Pipeline for Dockerized Applications

CI/CD Pipeline for Dockerized Applications Using AWS/Jenkins/Kubernetes. Please replace the Placeholders << >> with your Account Specific details.


# Pipeline Architecture

![CI_CD Pipeline](https://user-images.githubusercontent.com/66190700/162048132-e232e877-0fcc-45f8-81a2-23b5941f98fd.PNG)

1. GitHub Repo with Simple Application Code / Jenkinsfile / Docker File / Helm Chart etc.
2. GitHub WebHooks triggers the Jenkins Job on Commit to the Repo.
3. Unit Testcases are Run and Static application Security Testing (SAST) is carried out with and SonarQube.
4. Docker Image is Built/Tagged (Using commit hash) and Pushed to ECR.
5. Jenkins CI server Assumes Cross Account Role to connect to EKS account .
6. Helm Lint is performed and Helm packaging is done. 
7. Application deployed in EKS Cluster with Rolling Update Deployment Strategy 
8. Email and Slack Notification is sent upon Successful/Failure of Jenkins Pipeline


# Features

- AWS EC2 Spot instances for Compute (Jenkins/Sonar)
- Route53 used for DNS (mytwocents.click for Jenkins/Sonar and ramsawswork.click for Application in EKS for)
- Cross Account Access using IAM Role
- Amazon Certificate Manager (ACM) is used to Secure the Application deployed in EKS
- Zero-Downtime Deployment with EKS
- Readiness/Liveness probes and Pod CPU/Memory Requests and Limits set.
- Ingress enabled in EKS so multiple applications can be hosted and routed seamlessly

