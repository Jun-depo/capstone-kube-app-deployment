pipeline {
    agent any
    environment {
        New_VERSION = "V1"
    }
    parameters {
        booleanParam(name: "DockerBuild", defaultValue: True)        
        booleanParam(name: "RollingUpdate", defaultValue: false)
    }
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
            when { expression { params.DockerBuild } }
            
            steps { withCredentials([[$class: 'UsernamePasswordMultiBinding', 
            credentialsId: 'dockerhub', 
            usernameVariable: 'DOCKER_USERNAME', 
            passwordVariable: 'DOCKER_PASSWORD']])
            {            
                sh '''#!/bin/bash
                echo Docker image version: $New_VERSION
                docker build -t jun222work/hypothyroid:$New_VERSION .
                '''
            }
            }        
        }
        stage('Push image') {

            when { expression { params.DockerBuild } }
            steps { withCredentials([[$class: 'UsernamePasswordMultiBinding', 
                credentialsId: 'dockerhub', 
                usernameVariable: 'DOCKER_USERNAME', 
                passwordVariable: 'DOCKER_PASSWORD']]) 
                {
                    sh '''
                    docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD
                    docker image push jun222work/hypothyroid:$New_VERSION
                    '''                           
                }
            }
        }

        stage('create the kubeconfig file') {
            steps {
                withAWS(region:'us-east-1', credentials:'aws_credentials')
                {
                    sh 'aws eks --region us-east-1 update-kubeconfig --name capstonecluster'
                }                        
            }            
        }
        stage('Deploy Docker image Version 1') {
            steps {
                withAWS(region:'us-east-1', credentials:'aws_credentials')
                {
                    sh 'kubectl apply -f k8s/deployment_service.yaml' 
                }
            }
        }
        stage('Rolling update docker image to Version-2') {
            when { expression { params.RollingUpdate } }
            steps {
                    sh "kubectl set image deployment/hypothyroid-deployment hypothyroid \
                    hypothyroid=jun222work/hypothyroid:$New_VERSION"
                    }
        }
  
    }
}