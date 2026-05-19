provider "google" {
  project = "eco-emissary-496007-c7"
  region  = "asia-south1"
}

resource "google_cloud_run_service" "taskflow" {
  name     = "taskflow-service"
  location = "asia-south1"

  template {
    spec {
      containers {
        image = "asia-south1-docker.pkg.dev/eco-emissary-496007-c7/task-repo/taskflow-app:v1"
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}