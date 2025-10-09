pipeline {
    agent any

    stages {
        stage('Devolopment') {
            steps {
                echo 'i am in devolopment'
                sh 'git --version'
            }
        }
        stage('Testing') {
            steps {
                echo 'i am in testing'
                sh 'Docker --version'
            }
        }
        stage('Production') {
            steps {
                echo 'i am in production'
                sh 'python3 --version'
            }
        }
    }
}
