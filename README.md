# TaskFlow

TaskFlow is a cloud-native task management application built with FastAPI.

## Features
- Create tasks
- View tasks
- Update tasks
- Delete tasks
- Store user input in backend database

## Tech Stack
- FastAPI
- SQLite
- Docker
- Google Cloud Run

## Deployment
The application is deployed on Google Cloud Run.

Live URL:
https://taskflow-service-513471288086.asia-south1.run.app

## API Endpoints
- GET /
- POST /submit
- GET /tasks
- POST /tasks
- PUT /tasks/{task_id}
- DELETE /tasks/{task_id}