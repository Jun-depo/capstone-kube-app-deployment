#!/usr/bin/env bash

# Docker image should be already uploaded to Docker Hub

# This is your Docker ID/path
# dockerpath=<>
dockerpath=jun222work/hypothyroid:latest

# Run the Docker Hub container with kubernetes
kubectl run hypothyroid \
    --generator=run-pod/v2\
    --image=$dockerpath\
    --port=80 --labels app=hypothyroid

# List kubernetes pods
kubectl get pods

# Forward the container port to a host
kubectl port-forward hypothyroid 8000:80
