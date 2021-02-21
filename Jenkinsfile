pipeline {
    agent any
    stages{
        stage('Linting') {
            agent {
                docker { image 'python:3.8.7-buster'} 
            }   
            steps {                              
                sh 'make install' 
                sh './hadolint Dockerfile'
                sh 'pylint --disable=R,C,W1203 --load-plugins pylint_flask_sqlalchemy app.py'
                sh 'pylint --disable=R,C forms.py'
                sh 'pylint --disable=R,C hypothyroid.py'                
            }
        }
    }
}