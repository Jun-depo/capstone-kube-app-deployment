pipeline {
    agent any
    stages{
        stage('Linting') {
            steps                               
                {   
                    sh 'conda create --yes -n venv python=3.8'
                    sh 'conda activate venv'
                    sh 'make install'
                    sh './hadolint Dockerfile'
                    sh 'pylint --disable=R,C,W1203 --load-plugins pylint_flask_sqlalchemy --load-plugins pylint_flask app.py'
                    sh 'pylint --disable=R,C forms.py'
                    sh 'pylint --disable=R,C hypothyroid.py'               
            }
        }
    }
}