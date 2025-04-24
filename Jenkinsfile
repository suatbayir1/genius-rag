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

        stage("Build") {
            steps {
                script {
                    sh "docker build -t ${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG} ."
                }
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
