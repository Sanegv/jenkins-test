pipeline {
    agent none  
 
    stages {
        stage('Build') {
            agent{
                label 'docker-agent-python'
            }
            steps {
                git branch: 'source', url:'https://github.com/Sanegv/jenkins-test'
                sh 'pip install -r back/requirements.txt'
            }
        }
        stage('Test') {
            agent{
                label 'docker-agent-python-test'
            }
            steps {
                git branch: 'source', url:'https://github.com/Sanegv/jenkins-test'
                sh 'pip install -r back/requirements.txt'
                sh 'py back/app_test.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
 