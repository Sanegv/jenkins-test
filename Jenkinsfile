pipeline {
    agent none  
 
    stages {
        stage('Checkout code'){
            agent any
            steps {
                git branch 'source', url:'https://github.com/Sanegv/jenkins-test'
            }
        }
        stage('Build') {
            agent{
                label 'docker-agent-python'
            }
            steps {
                sh 'pip install -r requirements'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
 