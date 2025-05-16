pipeline { 
    agent any

    environment {
        ECR_REPO = '585008048344.dkr.ecr.ap-south-1.amazonaws.com/todo-flask-app'
        IMAGE_NAME = 'todo-flask-app'
        SONARQUBE = 'MySonar'  // Must match name in Jenkins > SonarQube servers
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/tushar223/AWS-Jenkins-SonarProject.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'sonar-scanner'  // This must match the name from your screenshot
                    withSonarQubeEnv("${SONARQUBE}") {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
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
                    kubectl apply -f k8s/db-secret.yaml
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml
                '''
            }
        }
    }
}
