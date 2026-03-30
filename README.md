# aceetest-devops
Setup test for Docker, Jenkins and Github Actions
This project implements a Flask-based fitness management system integrated with a complete DevOps pipeline. It demonstrates modern DevOps practices including version control, automated testing, containerization, and CI/CD using GitHub Actions and Jenkins.


## Tech Stack
Backend: Python (Flask)
Database: SQLite
Testing: Pytest
Containerization: Docker
CI/CD: GitHub Actions
Build Automation: Jenkins

## Project Structure
```
aceest-devops/
│
├── app.py
├── database.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
│
├── templates/
│
├── tests/
│   └── test_app.py
│
├── .github/workflows/
│   └── main.yml
│
└── README.md
```
## Local Setup & Execution
1. Clone Repository:
   git clone https://github.com/<username>/aceetest-devops.git
   cd aceetest-devops

2. Create Virtual Environment

```
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
```

3. Install Dependencies
`pip install -r requirements.txt`


4. Run Application
`python app.py`

5. Open in browser:

http://localhost:8000


### Running Tests
Run all tests using:
`pytest`

Expected output:
`1 passed`

## Docker Setup
1. Build Docker Image
   
`docker build -t aceest-app .`

2. Run Container

`docker run -p 8000:5000 aceest-app`

3. Access:

http://localhost:8000


## GitHub Actions CI/CD Pipeline
The pipeline is triggered on every push and pull request.
Pipeline Stages:
- Install dependencies
- Run Pytest
- Build Docker Image
- Run container smoke test

## Jenkins BUILD Pipeline:
Jenkins acts as a secondary validation layer.

### Running Jenkins Locally with Docker
1. To run Jenkins locally using Docker:
```
docker run -d \
  --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts
```
2. After starting the container, Open Jenkins in your browser:
http://localhost:8080

3. Get the initial admin password:
`docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword`

4. Complete setup:
- Install suggested plugins
- Create an admin user
- Create a new Pipeline job:
- Select Pipeline
- Connect your GitHub repository
- Use the existing Jenkinsfile
- Jenkins Workflow:
- - Pull latest code from GitHub
- - Set up Python environment
- - Install dependencies
- - Run Pytest
5. Trigger Mechanism:
- - Configured using Poll SCM
- - Jenkins checks for changes on main branch and triggers builds automatically
