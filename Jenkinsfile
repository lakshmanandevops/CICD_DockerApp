def COMMIT

pipeline
{
 agent any

 environment
 {
     AWS_CI_ACCOUNT_ID="<<CI_ACCOUNT>>"
     AWS_EKS_ACCOUNT_ID="<<EKS_ACCOUNT>>"
     AWS_DEFAULT_REGION="us-east-1" 
     ECR_REPO_NAME="<<ECR_REPO_NAME>>"
     ECR_REPOSITORY_URI = "${AWS_CI_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${ECR_REPO_NAME}"
     scannerHome = tool 'SonarScanner'
    
 }

 options 
 {
  buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', daysToKeepStr: '', numToKeepStr: '5')
  timestamps()
 }

 stages
 {
     stage('Code Checkout')
     {
         steps
         {
             script
             {
                 checkout([$class: 'GitSCM', branches: [[name: '*/feature']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/lakshmanandevops/PythonDockerApp.git']]])
                 COMMIT = sh (script: "git rev-parse --short=10 HEAD", returnStdout: true).trim()                             

             }
             
         }
     }

     stage('UnitTest')
     {
        steps
         {
            sh '''
            pip3 install virtualenv
            python3 -m virtualenv dockerapp
            source dockerapp/bin/activate
            pip3 install -r requirements.txt
            nosetests -v ./ --with-coverage --cover-package=app --cover-xml --cover-html --with-xunit
            '''
         }
     }

     stage('SonarQube Analysis')
     {
         steps
         {
                withSonarQubeEnv('SonarServer') 
                {
                    sh "${scannerHome}/bin/sonar-scanner"
                }
         }
      }

     stage('SonarQube QualityCheck')
     {
         steps     
         {
            timeout(10) 
                {
                    waitForQualityGate abortPipeline: true, credentialsId: 'SonarSecret'
                } 
         }
     }

     stage('Docker Build')
     {
        steps   
        {
            sh "docker build . -t ${ECR_REPOSITORY_URI}:pythonflaskapp-${COMMIT}"
        }
     }

     stage('Docker Push')
     {
        steps   
        {
            sh " aws ecr get-login-password --region ${AWS_DEFAULT_REGION}| docker login --username AWS --password-stdin ${AWS_CI_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"
            sh " docker push ${ECR_REPOSITORY_URI}:pythonflaskapp-${COMMIT} "
        }
     }

     stage('Helm Lint & Package')
     {
        steps  
            {
                sh """
                #!/bin/bash
                sed -i 's/version/$COMMIT/g' ${WORKSPACE}/helm/values.yaml
                helm lint helm
                helm package helm
                mv helm-0.1.0.tgz PythonFlaskApp.tgz
                """
            }
     }

     stage('EKS Deploy') 
     { 
        steps  
            {
            sh '''
            export $(printf "AWS_ACCESS_KEY_ID=%s AWS_SECRET_ACCESS_KEY=%s AWS_SESSION_TOKEN=%s" \
            $(aws sts assume-role \
            --role-arn arn:aws:iam::<<EKS_ACCOUNT>>:role/JenkinsCIRole \
            --role-session-name JenkinsCISession \
            --query "Credentials.[AccessKeyId,SecretAccessKey,SessionToken]" \
            --output text))
            aws eks update-kubeconfig --name eks-master --region us-east-1
            helm upgrade --dry-run --install pythonflaskapp PythonFlaskApp.tgz --debug
            helm upgrade --install pythonflaskapp PythonFlaskApp.tgz --debug --wait --timeout 1200s 
            helm status pythonflaskapp  '''
            }
    }
          
} 
 
 
 
 post
 {     
     success
     {
       slackSend channel: 'ci-cd', tokenCredentialId: 'Slack',color: 'good', message: "started  JOB : ${env.JOB_NAME}  with BUILD NUMBER : ${env.BUILD_NUMBER}  BUILD_STATUS: - ${currentBuild.currentResult} To view the dashboard (<${env.BUILD_URL}|Open>)"
     
       emailext attachLog: true, body: '''BUILD IS SUCCESSFULL - $PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS: 
       Check at $BUILD_URL to view the results. 
        
       Regards, 
       Lakshmanan''', compressLog: true, replyTo: '<<EmailID>>', 
       subject: '$PROJECT_NAME - $BUILD_NUMBER - $BUILD_STATUS', to: '<<EmailID>>'
         
     }
     
    failure
    {
     
       slackSend channel: 'ci-cd', tokenCredentialId: 'Slack',color: 'danger', message: "started  JOB : ${env.JOB_NAME}  with BUILD NUMBER : ${env.BUILD_NUMBER}  BUILD_STATUS: - ${currentBuild.currentResult} To view the dashboard (<${env.BUILD_URL}|Open>)"
     
       emailext attachLog: true, body: '''BUILD FAILED- $PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS: 
       Check at $BUILD_URL to view the results. 
        
        Regards, 
       Lakshmanan''', compressLog: true, replyTo: '<<EmailID>>', 
       subject: '$PROJECT_NAME - $BUILD_NUMBER - $BUILD_STATUS', to: '<<EmailID>>'
     
     
     }
     
 }


 
 }
