pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/swethasweth19/intract.git'
            }
        }

        stage('Install Requirements') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // If you have test cases, run them
                sh 'python -m unittest discover tests'
            }
        }

        stage('Run App') {
            steps {
                sh 'nohup python app.py &'
            }
        }
    }
}
