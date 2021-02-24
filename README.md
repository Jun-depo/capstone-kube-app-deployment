## Use Jenkins for Continuous Integration, Continuous Deployment or Continuous Delivery (CI/CD) to Deploy a Hypothyroid Machine learning Application (Udacity AWS DevOps Nano degree Castone Project)

### Propose and Scope the Project

This Project use Jenkins as the CI/CD tool to build the Docker image for a machine learning application, then use AWS kubenetes Service to deploy the application using the docker image.

The outline of the steps for this project

1. Build an Machine Learning flask app.  

I have built hyothyroid classification app previously with flask.  The app is slightly modified for this project.

2. Build docker image version 1 for this app and deposit at docker hub.  

* Dockerfile contains the info to build docker image.

3. Deploy kubenetes service with version 1 of the docker image (tagged V1). 

4. Modify the flask app to build and deposit version 2 of the docker version (tagged V2). 

5. Use kubenetes services to perform rolling update with new docker image. 

All the steps above were scripted in Jenkinsfile which perform the tasks in stages.  



