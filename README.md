# CICD Pipeline for Dockerized Applications
CI/CD Pipeline for Dockerized Applications Using AWS/Jenkins/Kubernetes
# Pipeline Architecture

![image](https://user-images.githubusercontent.com/66190700/162047506-401b105e-55d9-445b-9d38-f7bf32b30bce.png)

1. GitHub Repo with Simple Application Code / Jenkinsfile / Docker File / Helm Chart etc.
2. GitHub WebHooks triggers the Jenkins Job on Commit to the Repo.
3. Unit Testcases are Run and Static application Security Testing (SAST) is carried out with and SonarQube.
4. Docker Image is Built/Tagged (Using commit hash) and Pushed to ECR.
5. Jenkins CI server Assumes Cross Account Role to connect to EKS account .
6. Helm Lint is performed and Helm packaging is done. 
7. Application deployed in EKS Cluster with Rolling Update Deployment Strategy 
8. Email and Slack Notification is sent upon Successful/Failure of Jenkins Pipeline
