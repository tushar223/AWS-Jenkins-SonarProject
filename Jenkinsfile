pipeline {
  agent any

  environment {
    ECR_REPO = '585008048344.dkr.ecr.ap-south-1.amazonaws.com/todo-flask-app'
    IMAGE_NAME = 'todo-flask-app'
    SONARQUBE = 'MySonar'
  }

  tools {
    sonarQubeScanner 'SonarQube'
  }

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/tushar223/AWS-Jenkins-SonarProject.git'
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
        sh 'docker build -t $IMAGE_NAME .'
        sh 'aws ecr get-login-password | docker login --username AWS --password-stdin $ECR_REPO'
        sh 'docker tag $IMAGE_NAME:latest $ECR_REPO/$IMAGE_NAME:latest'
        sh 'docker push $ECR_REPO/$IMAGE_NAME:latest'
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        sh 'kubectl apply -f k8s/deployment.yaml'
        sh 'kubectl apply -f k8s/service.yaml'
      }
    }
  }
}



