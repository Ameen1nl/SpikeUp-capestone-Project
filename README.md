# data-engineering-capstone
# data-engineering-capstone-project
# Project Title: Customer Insights and Automation using PySpark, Airflow, and GCP

## Table of Contents

- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [CI/CD Pipeline](#cicd-pipeline)
- [Data Processing with PySpark](#data-processing-with-pyspark)
- [Orchestration with Airflow](#orchestration-with-airflow)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project focuses on developing a scalable and automated data processing pipeline using PySpark, Airflow, and Google Cloud Platform (GCP). The primary goal is to process large datasets to generate customer insights, such as segmentation, churn prediction, and retention analysis, and automate the orchestration of these tasks using Airflow on Google Cloud Composer.

## Repository Structure

The repository is organized as follows:

├── .github/ # Holds GitHub workflows for CI/CD
├── analysis/ # Contains data analysis scripts (Week 2)
├── dags/ # Holds Airflow DAGs for orchestration (Week 3 & 4)
└── README.md # Project documentation (this file)


## Prerequisites

Before you begin, ensure you have the following tools installed:

- [Git](https://git-scm.com/)
- [Miniconda](https://docs.anaconda.com/free/miniconda/)
- [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)

### Software Dependencies

- Python 3.9 (via Conda)
- PySpark
- Google Cloud SDK
- Apache Airflow

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-repository/project-name.git
cd project-name
```
### 2. Set Up Your Environment
Create and activate the Conda environment using the provided capstone.yml:
```bash
conda env create -f capstone.yml
conda activate project-env
```
### 3. Set Up Google Cloud Access
Authenticate and configure access to your GCP account via service accounts:

```bash
gcloud auth login
gcloud config set project your-gcp-project-id
```

## CI/CD Pipeline

This project utilizes GitHub Actions for continuous integration and deployment (CI/CD). The CI/CD pipeline is configured to:

1. **Lint and Test**: Automatically check code quality and run tests.
2. **Deploy**: Deploy code to GCP for data processing and Airflow DAG orchestration.

### Setting Up the CI/CD Pipeline

1. Create a new branch for your changes:

   ```bash
   git checkout -b feature-branch
   ```
2. Make your changes and push the branch:
```bash
git push origin feature-branch
   ```
3. Create a Pull Request (PR) and merge it to main after review.

4. GitHub Actions will automatically run the CI pipeline.
### Example Workflow: Hello World

An example GitHub Actions workflow is provided to print "Hello World":

```yaml
name: Hello World Workflow

on: [push]

jobs:
  hello-world:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v2
      - name: Run Hello World
        run: echo "Hello World"
```

This Markdown code includes the example GitHub Actions workflow for printing "Hello World."

