pipeline {
    agent any
    stages{
        stage('Linting') {
            steps { withPythonEnv('/usr/bin/python3.8')                              
                {
                    sh 'pip install pylint'
                    sh 'pylint-flask-sqlalchemy'        
                    sh 'wget -O ./hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64 &&\
	                chmod +x ./hadolint' 
                    sh './hadolint Dockerfile'
                    sh 'pylint --disable=R,C,W1203 --load-plugins pylint_flask_sqlalchemy app.py'
                    sh 'pylint --disable=R,C forms.py'
                    sh 'pylint --disable=R,C hypothyroid.py'
                }               
            }
        }
    }
}