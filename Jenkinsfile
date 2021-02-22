pipeline {
    agent any
    stages{  
        stage('Linting') { 
            agent { docker { image 'python:3.8.7-buster' } }
            steps  {     
                    sh 'python3.8 -m venv venv'
                    sh '''
                        . venv/bin/activate
                        pip install --upgrade pip && pip install -r requirements.txt 
                        pylint --disable=R,C,W1203 --load-plugins pylint_flask_sqlalchemy --load-plugins pylint_flask app.py
                        pylint --disable=R,C forms.py
                        pylint --disable=R,C hypothyroid.py
                        '''
                    sh 'wget -O ./hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64 &&\
	                    chmod +x ./hadolint'
                    sh './hadolint Dockerfile'             
            }
        }
        
        stage('Build docker image') {
            agent { label "6-core-agent" }
            steps { withCredentials([[$class: 'UsernamePasswordMultiBinding', 
            credentialsId: 'dockerhub', 
            usernameVariable: 'DOCKER_USERNAME', 
            passwordVariable: 'DOCKER_PASSWORD']]){
            
            sh '''
            docker build -t jun222work/hypothyroid:$BUILD_ID .
            '''
            }
            }        
        }
  
    }
}