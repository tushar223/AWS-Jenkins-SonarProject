# Flask To-Do App with Jenkins CI/CD, Docker, SonarQube and Kubernetes on AWS
A simple to-do app that stores, delete update job by creating app and building image thorugh docker and pushing into ECR then thorugh kubernetes (used kind not used EKS as it takes little time and cost in AWS) and then build that project in jenkins where integartion of sonarqube was done to check the quality of code which was a success.
## Project Overview

This project demonstrates a complete DevOps pipeline for deploying a simple Python Flask To-Do application using:

- Docker for containerization
- Jenkins for CI/CD
- SonarQube for static code analysis
- MySQL on AWS RDS as the backend database
- Kubernetes (Kind) for orchestration
- Amazon ECR for container image storage
- AWS EC2 for infrastructure

---

## Completed Steps

### 1. AWS RDS Setup
- Launched MySQL database on AWS RDS
- Created a database and configured the security group to allow EC2 access
- ![image](https://github.com/user-attachments/assets/36159b10-79c9-4def-9887-28a6f814a479)
![Screenshot 2025-05-12 183442](https://github.com/user-attachments/assets/cddd82f9-7707-4e20-8d18-3beeef2486fc)

### 2. Flask Application
- Developed a Python Flask application with basic to-do functionality
- Connected it to RDS MySQL
- Created HTML templates for frontend

### 3. Dockerization
- Wrote a Dockerfile to containerize the application
- Installed required packages using requirements.txt
- Verified Docker build locally

### 4. Amazon ECR
- Created a private repository in AWS ECR
- Built and pushed Docker image using Jenkins
- ![Screenshot 2025-05-16 171545](https://github.com/user-attachments/assets/be8ce332-625a-4a54-b7e7-c61b13d39a16)


### 5. Jenkins Setup
- Installed Jenkins inside a Docker container on EC2
- Configured plugins: Docker, Git, SonarQube Scanner
- Built Jenkins pipeline for CI/CD

### 6. Kubernetes (Kind)
- Installed Kind inside the Jenkins container
- Configured kubectl to point to the Kind cluster
- Applied Kubernetes manifests for deployment and service

### 7. SonarQube Integration
- Installed SonarQube using Docker on EC2
- Configured Jenkins to connect to SonarQube via token
- Added sonar-project.properties file for analysis
![Screenshot 2025-05-15 173822](https://github.com/user-attachments/assets/a2e801a6-0765-42a8-b341-868b8b8b1097)

---
