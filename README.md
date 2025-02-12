#Target-Sales-Pipeline (PART-1)

AWS Lambda Handler for S3 to DynamoDB Data Pipeline

📌 Overview

This project automates the creation of DynamoDB tables from CSV schemas in S3 and inserts the extracted data. It is optimized for AWS Lambda, but can also run on EC2 or Docker. The pipeline can be extended with AWS Step Functions to orchestrate multiple Lambda functions, each handling a different table.

🔧 Features

Auto-creates DynamoDB tables if they don't exist.
Dynamically infers schema from CSV files stored in S3.
Efficient batch insertion into DynamoDB.
Designed for AWS Lambda, but can be deployed on EC2 or Docker.
Supports AWS Step Functions for multi-step workflows with different Lambda functions handling specific tables.

📁 Project Structure

.
├── main.py               # Lambda handler (entry point)
├── s3_handler.py         # Handles S3 operations (reads CSV)
├── dynamodb_handler.py   # Handles DynamoDB operations (table creation, inserts)
├── utils.py              # Utility functions (data type inference, key mappings)
└── requirements.txt      # Dependencies (for local execution)


![image](https://github.com/user-attachments/assets/2d2c50a7-8360-431f-bc27-2a07bbca025e)


🚀 Deployment

1️⃣ Deploy to AWS Lambda

Zip the project files:

zip -r lambda-handler.zip .

Upload lambda-handler.zip to AWS Lambda.

Set the Lambda handler:

main.main

Attach an S3 trigger to process CSV files automatically when uploaded.

2️⃣ Running Locally (EC2, Docker)

This project can be adapted to EC2 or Docker for long-running or customized data processing.

Running on EC2

Install dependencies:

pip install boto3

Set up AWS credentials (aws configure).

Run the script:

python main.py

Running with Docker

Create a Dockerfile:

FROM python:3.12
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]

Build and run:

docker build -t lambda-handler .
docker run lambda-handler

🔀 Using AWS Step Functions for Automation

Instead of handling all tables in a single Lambda function, Step Functions can orchestrate multiple Lambda functions, each processing a different DynamoDB table.

How It Works

Each table gets a dedicated Lambda function (e.g., CustomersLambda, OrdersLambda).

Step Functions orchestrate the workflow, triggering specific Lambdas based on file uploads.

State transitions handle failures and retries, ensuring smooth execution.

Example Step Function Flow

(S3 Upload) → (Step Function) → (Lambda for Customers) → (Lambda for Orders) → (Lambda for Products) → (Data stored in DynamoDB)

Benefits of Using Step Functions

Modular Processing: Different Lambda functions for different tables.

Improved Reliability: Retries and error handling with AWS Step Functions.

Scalability: Each Lambda function runs independently, avoiding bottlenecks.

🛠️ Requirements

Python 3.12

AWS Boto3 SDK

IAM Role Permissions:

{
  "Effect": "Allow",
  "Action": [
    "s3:GetObject",
    "dynamodb:CreateTable",
    "dynamodb:PutItem",
    "logs:CreateLogStream",
    "logs:PutLogEvents",
    "states:StartExecution"
  ],
  "Resource": "*"
}

📈 Future Enhancements

AWS Glue Integration for ETL processing.

Amazon Redshift support for analytics.

EventBridge Triggers to automate workflows.

📬 Contact

For questions or issues, open a GitHub issue or contact the maintainer.
