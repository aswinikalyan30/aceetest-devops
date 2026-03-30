pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aceest-app .'
            }
        }

        stage('Run Container Test') {
            steps {
                sh '''
                docker run -d -p 9000:5000 --name test-container aceest-app
                sleep 5
                curl http://localhost:9000
                docker stop test-container
                docker rm test-container
                '''
            }
        }
    }
}
