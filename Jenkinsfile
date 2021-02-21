pipeline {
    agent any
    stages{
        stage('Linting') {
            steps { withPythonEnv('/usr/bin/python3.8')                              
                {
                    sh 'sudo apt-get install python3-venv'
                    sh 'python3.8 -m venv venv'
                    sh '. venv/bin/activate'
                    sh 'make install' 
                    sh './hadolint Dockerfile'
                    sh 'pylint --disable=R,C,W1203 --load-plugins pylint_flask_sqlalchemy app.py'
                    sh 'pylint --disable=R,C forms.py'
                    sh 'pylint --disable=R,C hypothyroid.py'
                }               
            }
        }
    }
}