pipeline {
    agent any
    stages{  
        stage('Linting') { 
            agent { docker { image 'python:3.8.8-alpine3.13' } }
            steps  {     
                    sh 'python --version'
                    sh 'make install'
                    sh './hadolint Dockerfile'
                    sh 'pylint --disable=R,C,W1203 --load-plugins pylint_flask_sqlalchemy --load-plugins pylint_flask app.py'
                    sh 'pylint --disable=R,C forms.py'
                    sh 'pylint --disable=R,C hypothyroid.py'              
            }
        }
    }
}