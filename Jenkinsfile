pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'suatbayir'
        IMAGE_NAME = 'backend'
        IMAGE_TAG = 'latest'
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
                    sh '''
                        apt-get update && apt-get install -y git python3-pip python3-venv &&
                        python3 -m venv venv &&
                        . venv/bin/activate &&
                        git config --global --add safe.directory /app &&
                        git config --unset-all core.hooksPath &&
                        pip install --upgrade pip &&
                        pip install pre-commit &&
                        venv/bin/pre-commit install &&
                        venv/bin/pre-commit run --all-files
                    '''
                }
            }
        }


        stage('Build') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG} ."
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
            when {
                branch 'main'
            }

            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'DOCKER_CREDENTIALS_ID', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                        sh "docker push ${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}"
                    }
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }

            steps {
                script {
                    echo "Deploying application..."
                    sh """
                        docker compose down
                        docker compose pull
                        docker compose up --build -d
                    """
                }
            }
        }
    }
}
