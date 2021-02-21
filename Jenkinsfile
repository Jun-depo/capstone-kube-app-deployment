pipeline {
    agent any
    stages{
        stage('Install dependencies'){ 
            agent {
                docker { image 'python:3.8.8-alpine3.13' } 
            }           
            steps {
            sh 'pip install --upgrade pip && pip install -r requirements.txt'
            sh 'wget -O ./hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64 &&\
	        chmod +x ./hadolint'
            }
        }
        stage('Linting') {
            steps {
        sh './hadolint Dockerfile'
        sh 'pylint --disable=R,C,W1203 --load-plugins pylint_flask_sqlalchemy app.py'
        sh 'pylint --disable=R,C forms.py'
        sh 'pylint --disable=R,C hypothyroid.py'
            }

    }
    }
}