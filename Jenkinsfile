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
                sh "cp .env.example .env"
            }
        }

        stage('Pre-commit Check') {
            steps {
                script {
                    sh """
                        docker run --rm -v "\$(pwd):/app" -w /app python:3.12 bash -c '
                            apt-get update && apt-get install -y git &&
                            git config --global --add safe.directory /app &&
                            git config --unset-all core.hooksPath &&
                            pip install pre-commit &&
                            pre-commit install &&
                            pre-commit run --all-files
                        '
                    """
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh "docker build --no-cache -t ${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh "docker run --rm --env-file .env ${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG} pytest tests"
                }
            }
        }

        stage('Push to Dockerhub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'DOCKER_CREDENTIALS_ID', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                        sh "docker push ${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}"
                    }
                }
            }
        }
    }
}
