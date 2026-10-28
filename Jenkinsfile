pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Test') {
            steps {
                bat 'python -m unittest test_app.py'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t student-management-app:latest .'
            }
        }

        stage('Push Image') {
            steps {
                echo 'Docker image will be pushed to Docker Hub'
            }
        }

        stage('Deploy to Minikube') {
            steps {
                echo 'Application will be deployed to Minikube'
            }
        }

        stage('Verify') {
            steps {
                echo 'Deployment will be verified'
            }
        }
    }
}