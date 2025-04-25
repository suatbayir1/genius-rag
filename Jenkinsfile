pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'suatbayir'
        IMAGE_NAME = 'backend'
        IMAGE_TAG = 'latest'
        SSH_CREDENTIALS_ID = 'remote-server-ssh-id'
        REMOTE_HOST = 'your.remote.server.ip'
        REMOTE_USER = 'remoteuser'
        REMOTE_PATH = 'path'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Docker build test') {
            steps {
                sh 'docker version'
                sh 'docker run hello-world'
            }
        }

        stage('Build') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }
    }
}
