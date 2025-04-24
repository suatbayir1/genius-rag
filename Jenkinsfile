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

        stage('Install Dependencies') {
            steps {
                sh '''
                    apt-get update && apt-get install -y python3-pip git
                    pip3 install --upgrade pip
                    pip3 install pre-commit
                '''
            }
        }

        stage('Pre-commit Checks') {
            steps {
                sh 'pre-commit run --all-files'
            }
        }

        stage("Build") {
            steps {
                echo "building the application..."
            }
        }

        stage("test") {
            steps {
                echo "testing the application..."
            }
        }

        stage("deploy") {
            steps {
                echo "deploying the application"
            }
        }
    }
}
