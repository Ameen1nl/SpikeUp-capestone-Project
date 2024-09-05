# data-engineering-capstone
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

## Project Overview

This project aims to develop an automated daily insights system for an e-commerce website, focusing on analyzing user behavior to enhance the customer experience, reduce churn, and increase lead conversion. The insights generated will help the sales and marketing teams target the right customers with personalized incentives, leading to improved customer retention, higher conversion rates, and increased sales and revenue.

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
- Java

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Devops1964/data-engineering-capstone.git
cd data-engineering-capstone
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
gcloud config set data-eng-capstone-434311
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

on:
  push:
    branches:
      - main  # Run only on pushes to the 'main' branch
      
jobs:
  say-hello:
    runs-on: ubuntu-latest
    steps:
    - name: Print Hello World
      run: echo "Hello, World!"
```

## Data Processing with PySpark

In Week 2, we focused on processing and analyzing customer data using PySpark. The steps included:

- **Data Ingestion**: Reading data from Google Cloud Storage.
- **Data Transformation**: Performing customer segmentation and churn analysis.
- **Data Storage**: Writing results back to a separate GCS bucket.

you can check the processing script in this [data-analysis.ipynb file](https://github.com/Devops1964/data-engineering-capstone/blob/d5b24fe2ff71a3908f0c33a45b4cb5d3e7fbd146/data-analysis.ipynb)

## Orchestration with Airflow

In Weeks 3 & 4, we implemented task orchestration using Apache Airflow on Google Cloud Composer. The pipeline is scheduled to run daily at 10:00 AM and automates the data processing tasks developed in Week 2.

you can check the Orchestration with Airflow in this [ecommerce_insights_dag.py file](https://github.com/Devops1964/data-engineering-capstone/blob/d5b24fe2ff71a3908f0c33a45b4cb5d3e7fbd146/dags/ecommerce_insights_dag.py)

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Push the branch (`git push origin feature-branch`).
5. Open a Pull Request.

