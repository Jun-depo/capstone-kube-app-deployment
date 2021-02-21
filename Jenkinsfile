pipeline {
    agent any
    stages{  
        stage('Linting') { 
            steps  { 
                agent { docker { image 'python:3.8.7-buster' } }                 
                {   
                    sh 'python --version'
                    sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
                    sh 'python get-pip.py'
                    sh 'make install'
                    sh './hadolint Dockerfile'
                    sh 'pylint --disable=R,C,W1203 --load-plugins pylint_flask_sqlalchemy --load-plugins pylint_flask app.py'
                    sh 'pylint --disable=R,C forms.py'
                    sh 'pylint --disable=R,C hypothyroid.py'
                }               
            }
        }
    }
}