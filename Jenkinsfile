pipeline {
    agent any
    stages{  
        stage('Linting') { 
            agent { docker { image 'python:3.8.8-alpine3.13' } }
            steps  {     
                    sh 'python3.8 -m venv venv'
                    sh '. venv/bin/activate'
                    sh 'pip install pylint'
                    sh 'wget -O ./hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64 &&\
	                    chmod +x ./hadolint'
                    sh './hadolint Dockerfile'
                    sh 'pylint --disable=R,C forms.py'
                    sh 'pylint --disable=R,C hypothyroid.py'              
            }
        }
    }
}