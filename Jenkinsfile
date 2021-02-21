pipeline {
    agent any
    stages{
        stage('Linting') {
            agent {
                docker { image 'cytopia/pylint'} 
            }   
            steps                               
                {
                    sh 'wget -O ./hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64 &&\
	                    chmod +x ./hadolint'
                    sh './hadolint Dockerfile'
                    sh 'pylint --disable=R,C forms.py'
                    sh 'pylint --disable=R,C hypothyroid.py'               
            }
        }
    }
}