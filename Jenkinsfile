pipeline {
    agent any
    stages{
        stage('Linting') {
            steps                               
                {   
                    sh 'wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh'
                    sh 'bash Miniconda3-latest-Linux-x86_64.sh -b -p .'
                    sh '. /miniconda3/bin/activate'
                    sh 'conda create --yes -n venv'
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