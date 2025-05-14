pipeline {
  agent any

  environment {
    ECR_REPO = '272258873932.dkr.ecr.ap-south-1.amazonaws.com/todoapp'  // ✅ Your actual ECR repo URL
    IMAGE_NAME = 'todoapp'
    SONARQUBE = 'MySonar'  // ✅ This must match name from Jenkins > Manage Jenkins > Configure System > SonarQube servers
  }

  tools {
    // ✅ This must match the name from Global Tool Configuration
    // If you're using latest plugin, use 'SonarQube Scanner for MSBuild' if required, or 'sonar-scanner'
    // We'll assume it's 'sonar-scanner' here:
    // Note: If you're using Declarative Pipeline and latest plugin, this might not even be needed
  }

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/tushar223/AWS-Jenkins-SonarProject.git'
      }
    }

    stage('SonarQube Analysis') {
      steps {
        withSonarQubeEnv("${SONARQUBE}") {
          sh 'sonar-scanner'
        }
      }
    }

    stage('Docker Build & Push') {
      steps {
        sh '''
          docker build -t $IMAGE_NAME .
          aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin $ECR_REPO
          docker tag $IMAGE_NAME:latest $ECR_REPO:latest
          docker push $ECR_REPO:latest
        '''
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        sh '''
          kubectl apply -f k8s/deployment.yaml
          kubectl apply -f k8s/service.yaml
        '''
      }
    }
  }
}
