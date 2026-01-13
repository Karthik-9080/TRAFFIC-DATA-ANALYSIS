# Traffic Data Analysis & Severity Prediction

This project analyzes traffic accident data, visualizes key patterns, and predicts accident severity using a machine learning model.  
The application is containerized using Docker, deployed on AWS EC2 using Terraform, and automatically deployed via a CI/CD pipeline using GitHub Actions.

---

## Live Demo

The application is deployed on an AWS EC2 instance and can be accessed here:

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://tinyurl.com/trafficanalysisapp)

---

## Features

- Exploratory Data Analysis (EDA) with visualizations
- Accident severity prediction using Machine Learning
- Interactive web interface built with Streamlit
- Dockerized application with Docker Compose
- Infrastructure provisioned using Terraform
- Terraform remote state using S3
- Fully automated CI/CD pipeline (zero manual SSH)
- Deterministic deployments using Git hard reset

---

## Machine Learning Overview

- **Problem Type:** Multi-class classification  
- **Target Variable:** Accident Severity (1–4)  
- **Model Used:** Decision Tree Classifier  
- **Evaluation Metric:** Accuracy  

> Moderate accuracy is expected due to limited dataset size and partial feature availability.  
> The model performs better than a random baseline.

---

## Data Analysis & Visualization

The application visualizes:
- Accident severity distribution
- Accidents by hour of day
- Accidents by weather condition
- Weekday vs weekend accident patterns

These insights help understand temporal and environmental factors influencing accidents.

---

## Tech Stack

### Application & ML
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Streamlit

### DevOps & Cloud
- Docker
- Docker Compose
- Terraform
- AWS EC2
- AWS S3 (Terraform remote state)
- GitHub Actions (CI/CD)

---

## Project Structure

```
Traffic_Data_Analysis/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
│
├── data/
│   └── india_traffic_accidents.csv
│
├── src/
│   ├── data_cleaning.py
│   └── model.py
│
├── terraform/
│   ├── Main.tf
    ├── Provider.tf
│   ├── Variables.tf
│   ├── Outputs.tf
│   └── backend.tf
│
└── .github/
    └── workflows/
        └── deploy.yml
```

---

## Run Locally (Without Docker)

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Run with Docker Compose

```bash
docker-compose build
docker-compose up
```

App will be available at:
```
http://localhost:8501
```

---

## Infrastructure Provisioning (Terraform)

- EC2 instance is provisioned using Terraform
- AMI is dynamically fetched using a data source
- Terraform state is stored remotely in S3

```bash
terraform init
terraform apply
```

---

## CI/CD Pipeline

On every push to the `main` branch:

1. GitHub Actions triggers the pipeline
2. SSH connection to EC2 is established automatically
3. Repository is force-synced using:
   ```
   git reset --hard origin/main
   git clean -fd
   ```
4. Docker images are rebuilt
5. Containers are restarted using Docker Compose

This ensures:
- No merge conflicts
- No configuration drift
- Production always matches `master`

---

## Security & Best Practices

- No secrets committed to Git all are on GitHub secrets
- Terraform state files are ignored and are on remote backend(s3)
- SSH keys and sensitive files are excluded via `.gitignore`

---

## Key Learnings

- End-to-end ML project lifecycle
- Containerization and orchestration
- Infrastructure as Code (IaC)
- Remote Terraform state management
- CI/CD automation and deployment strategies
- Real-world DevOps troubleshooting

---

## Future Improvements

- Push Docker images to Amazon ECR
- Add Nginx reverse proxy and HTTPS
- Implement health checks and rollback strategy
- Add monitoring and logging
- Extend ML model with more features

---

## Author

**Karthikeyan - S**  
DevOps & Cloud Enthusiast  
Machine Learning Practitioner  

---

## Final Note

This project demonstrates a complete production-style workflow combining **Machine Learning + DevOps + Cloud**, built with simplicity, automation, and best practices in mind.
