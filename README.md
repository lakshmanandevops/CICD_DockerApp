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
- Route53 used for DNS (mytwocents.click for Jenkins/Sonar and ramsawswork.click for Application in EKS)
- Cross Account Access using IAM Role
- Amazon Certificate Manager (ACM) is used to Secure the Application deployed in EKS
- Zero-Downtime Deployment with EKS
- Readiness/Liveness probes and Pod CPU/Memory Requests and Limits set.
- Ingress enabled in EKS so multiple applications can be hosted and routed seamlessly in EKS

Screen Captures

Jenkins

![CI_CD PipelineBO](https://user-images.githubusercontent.com/66190700/162048674-efd27be1-b746-4817-b399-88bcf2c6ab39.PNG)

SonarQube

![SonarQube Results](https://user-images.githubusercontent.com/66190700/162048792-d9f6fb6a-8a16-4804-b3ce-e312f024a6ce.PNG)

ECR Repo

![ECR Repo](https://user-images.githubusercontent.com/66190700/162049118-0542b182-f72a-4b82-9b54-5b0a7d32820c.PNG)

EKS Cluster

![EKS](https://user-images.githubusercontent.com/66190700/162049373-781004bb-ac70-4f51-acb0-c30d4b28b209.png)

Application Exposed Via Ingress

HomePage

![Homepage](https://user-images.githubusercontent.com/66190700/162049519-9a0da4ef-e336-4780-a14e-76b7100574e4.png)

HealthCheck Page

![Health Check Page](https://user-images.githubusercontent.com/66190700/162049582-344f7f14-8e1c-4e7b-86f5-e28e5bbee16c.png)




