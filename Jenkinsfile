pipeline {
    agent any
    stages{
        stage('Install dependencies'){ 
            agent {
                docker { image 'python:3.8.7-buster'} 
            }           
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]){
                    sh 'python3.8 -m venv venv'
                    sh '. venv/bin/activate'
                    sh 'make install'
                    sh 'ls -al'
                }
            }
        }
        stage('Linting') {
            steps {
                withPythonEnv('/usr/bin/python3.8') {
                sh './hadolint Dockerfile'
                sh 'pylint --disable=R,C,W1203 --load-plugins pylint_flask_sqlalchemy app.py'
                sh 'pylint --disable=R,C forms.py'
                sh 'pylint --disable=R,C hypothyroid.py'
                }
            }
        }
    }
}