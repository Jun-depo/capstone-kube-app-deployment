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
            steps { withCredentials([[$class: 'UsernamePasswordMultiBinding', 
            credentialsId: 'dockerhub', 
            usernameVariable: 'DOCKER_USERNAME', 
            passwordVariable: 'DOCKER_PASSWORD']]){
            
            sh '''
            #!/bin/bash
            
            COMMIT_TAG=$(git rev-parse HEAD | head -c8)
            echo Commit $COMMIT_TAG
            docker build -t jun222work/hypothyroid:$COMMIT_TAG .
            '''
            }
            }        
        }
        stage('Push image') {
            steps { withCredentials([[$class: 'UsernamePasswordMultiBinding', 
                credentialsId: 'dockerhub', 
                usernameVariable: 'DOCKER_USERNAME', 
                passwordVariable: 'DOCKER_PASSWORD']]) {
                sh '''
                #!/bin/bash
                
                COMMIT_TAG=$(git rev-parse HEAD | head -c8)
                echo Commit $COMMIT_TAG 

                dockerpath=jun222work/hypothyroid
                docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD
                docker image push $dockerpath:$COMMIT_TAG
                '''                           
                }
            }
        }
  
    }
}