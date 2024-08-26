# Flask Web Application

This project is a simple Flask web application that allows users to submit their name and email, and view a list of all submissions. The application is containerized using Docker and managed with Docker Compose.

## Features

- Home page with a form for submitting name and email.
- View page displaying all submissions.
- Containerized with Docker for easy deployment.
- Orchestrated with Docker Compose for managing services.
- Automated deployment script included.

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git.bskyb.com/)


## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Deploy Flask Application

- To run the flask application using python commands.
- Create a virtual environment.
- Activate the virtual environment.

```
python3 -m venv myenv
source myenv/bin/activate

```
- Run the application using python command.

```
python3 app.py

```
- Ensure flask is installed in your system

```
pip install Flask

```

- The application will be running in localhost at port 5000.


### 3. Containerize application using Dockerfile

- Navigate to the project directory and build a dokcer image.

```
docker build -t task .

```
- Start the container by giving run command.

```
docker run task

```

### 4.  Build and Run the application using Docker Compose

- Ensure Docker and Docker Compose are installed and running on your system.
- To deploy the application using docker compose file, use the following command.

```
docker compose up -d --build

```
This command will:

- Build the Docker image based on the Dockerfile.
- Start the Flask application inside a Docker container.
- Map port 5000 of the container to port 5000 of your host machine.

### 5. Access the Application
- Open your web browser and go to http://localhost:5000. You should see the homepage with a form to submit your information.

### 6. View Submissions
- After submitting the form, you can view all submissions by navigating to http://localhost:5000/submissions

### 7. Stopping the Application

- To stop the application, run:

```bash
docker compose down
```

## Automated Deployment

- On the server, run the following command to deploy the application

```
./deploy.sh

```

## Orchestration using Kubernetes

- Make sure you have Kuberenetes installed in your system.

- On the server, run the following command to manage the containerized application using Kuberenetes

```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

```

## Version Control

- Create a new git repository(mentortask2).

##### 1. Clone the repository

- Clone the mentortask2 repository using https.

```
git remote add origin https://git.bskyb.com/lmn549/mentortask2.git

```

##### 2. Create a new branch

- Create a new branch named task_files

```
git checkout -b task_files

```

##### 3. Copy and Add the files

- Copy all the files to the git repository.

```
cp /path/to/your/files/ .

```
- Add the files using following command.

```
git add file_name

```

##### 4. Commit the changes

- Commit the changes

```
git commit -m "Message for Commit"

```

##### 5. Push the Changes

- push the changes to the remote repository

```
git push origin task_files

```
