FROM python:3.8.7-buster

# Create a working directory
WORKDIR /app

# Copy source code to working directory.
# .dockerignore lists file and directories that are copied into docker
COPY . .

## Step 3:
# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

## Step 4:
# Expose port 80
EXPOSE 80

## Step 5:
# Run app.py at container launch
CMD ["python", "app.py"]
