pipeline {
    agent none  
 
    stages {
        stage('Build') {
            agent{
                label 'docker-agent-python'
            }
            steps {
                git branch: 'source', url:'https://github.com/Sanegv/jenkins-test'
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
 