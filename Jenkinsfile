pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Python & Dependencies') {
            steps {
                sh '''
                apt-get update
                apt-get install -y python3 python3-pip
                pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
    }
}