# GitHub Issues for Platform Engineer Roadmap

These issues should be created in your GitHub repository to track progress.

---

## Phase 1: Python Fundamentals (Weeks 1-4)

### Issue 1: Week 1 - Python Setup & Syntax
**Title:** Week 1: Python Setup & Basic Syntax  
**Labels:** python, phase-1, week-1  
**Assignee:** Self  
**Description:**

Setup Python environment and master basic syntax.

- [ ] Install Python 3.x from python.org
- [ ] Install VSCode and Python extension
- [ ] Create project folder: `pbc-platform-engineer`
- [ ] Set up virtual environment: `python -m venv venv`
- [ ] Create first program: hello.py
- [ ] Complete Week 1 syntax exercises
- [ ] Solve 5 HackerRank problems (basic)
- [ ] Commit code to GitHub

**Resources:**
- [Python Installation Guide](https://www.python.org/downloads/)
- [VSCode Setup](https://code.visualstudio.com/)
- [Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

---

### Issue 2: Week 2 - Control Flow (if/else, loops)
**Title:** Week 2: Control Flow - if/else, for, while  
**Labels:** python, phase-1, week-2  
**Depends on:** Issue 1  
**Description:**

Master control flow structures.

- [ ] Understand if/elif/else statements
- [ ] Learn for loops (range, lists)
- [ ] Learn while loops
- [ ] Practice break and continue
- [ ] Solve list comprehension problems
- [ ] Complete Week 2 exercises
- [ ] Solve 5 HackerRank problems (control flow)
- [ ] Push code to GitHub

**Exercises:**
- Write calculator program (addition, subtraction, etc.)
- Print multiplication table (1-12)
- Find factorial of number
- Print prime numbers 1-100

---

### Issue 3: Week 3 - Functions & Modules
**Title:** Week 3: Functions & Python Modules  
**Labels:** python, phase-1, week-3  
**Depends on:** Issue 2  
**Description:**

Learn function definition and module usage.

- [ ] Define custom functions
- [ ] Understand parameters and return values
- [ ] Learn default parameters
- [ ] Understand *args and **kwargs
- [ ] Import and use modules (os, sys, json, requests)
- [ ] Create utility module with helper functions
- [ ] Solve 5 HackerRank problems (functions)
- [ ] Push code to GitHub

**Exercises:**
- Create function to calculate GCD
- Create function to check if number is prime
- Create module with utility functions
- Practice importing built-in libraries

---

### Issue 4: Week 4 - File Handling & Project 1
**Title:** Week 4: File I/O & Mini Project 1  
**Labels:** python, phase-1, week-4, project  
**Depends on:** Issue 3  
**Description:**

Master file operations and complete first project.

- [ ] Learn file read/write operations
- [ ] Understand file modes (r, w, a, rb, wb)
- [ ] Work with CSV files
- [ ] Parse JSON files
- [ ] Error handling with try/except
- [ ] Create Project 1: File Organizer
  - [ ] Design program structure
  - [ ] Implement file operations
  - [ ] Test with sample files
  - [ ] Document code
- [ ] Push complete project to GitHub
- [ ] Create comprehensive README

**Project 1 - File Organizer:**
Create a Python script that:
1. Scans a folder
2. Identifies file types (images, documents, code, etc.)
3. Creates subfolders for each type
4. Moves files to appropriate folders
5. Logs all operations

---

## Phase 2: AWS Free Tier Essentials (Weeks 5-7)

### Issue 5: AWS Account Setup & Navigation
**Title:** Phase 2: AWS Account Setup & Exploration  
**Labels:** aws, phase-2, week-5  
**Depends on:** Issue 4  
**Description:**

Set up AWS free tier account and learn console.

- [ ] Create AWS free tier account
- [ ] Enable billing alerts
- [ ] Create IAM user for personal use
- [ ] Explore AWS Management Console
- [ ] Understand common services
- [ ] Review free tier limits
- [ ] Document account setup process

---

### Issue 6: EC2 & boto3 Basics
**Title:** Phase 2: EC2 Instances & boto3  
**Labels:** aws, python, boto3, phase-2, week-6  
**Depends on:** Issue 5  
**Description:**

Learn EC2 and AWS Python SDK.

- [ ] Create EC2 key pair
- [ ] Launch free tier EC2 instance
- [ ] Connect via SSH
- [ ] Install boto3
- [ ] Create Python script to list EC2 instances
- [ ] Write script to manage EC2 instances
- [ ] Solve 3 boto3 exercises
- [ ] Push code to GitHub

---

### Issue 7: S3 Automation Script
**Title:** Phase 2: S3 Bucket Operations with boto3  
**Labels:** aws, python, boto3, phase-2, week-7, project  
**Depends on:** Issue 6  
**Description:**

Create S3 automation project.

- [ ] Create S3 bucket
- [ ] Write script to upload files
- [ ] Write script to download files
- [ ] Create backup automation
- [ ] Implement error handling
- [ ] Document S3 operations
- [ ] Project 2: AWS Automation Suite
- [ ] Push to GitHub

**Project 2 - AWS Automation:**
Build Python scripts for:
1. EC2 Instance Manager
2. S3 Backup Tool
3. Cost Analyzer (basic)

---

## Phase 3: Git & Terraform (Weeks 8-10)

### Issue 8: Git Fundamentals
**Title:** Phase 3: Git & GitHub Mastery  
**Labels:** git, phase-3, week-8  
**Description:**

Master version control.

- [ ] Git installation and setup
- [ ] Create .gitignore
- [ ] Understand branching
- [ ] Practice commit workflows
- [ ] Learn pull requests
- [ ] Practice merging
- [ ] Document git workflow

---

### Issue 9: Terraform Basics
**Title:** Phase 3: Terraform Infrastructure as Code  
**Labels:** terraform, iac, phase-3, week-9  
**Depends on:** Issue 8  
**Description:**

Learn Infrastructure as Code with Terraform.

- [ ] Install Terraform
- [ ] Understand HCL syntax
- [ ] Create simple AWS infrastructure
- [ ] Use variables and outputs
- [ ] Manage state files
- [ ] Create Project 3: Terraform Infra

---

### Issue 10: Project 3 - Terraform AWS Infrastructure
**Title:** Phase 3: Project 3 - Terraform VPC + EC2  
**Labels:** terraform, aws, phase-3, week-10, project  
**Depends on:** Issue 9  
**Description:**

Build infrastructure with Terraform.

- [ ] Design VPC architecture
- [ ] Create main.tf, variables.tf, outputs.tf
- [ ] Deploy VPC with public/private subnets
- [ ] Deploy EC2 instances
- [ ] Configure security groups
- [ ] Document terraform code
- [ ] Push to GitHub
- [ ] Create architecture diagram

---

## Phase 4: Docker (Weeks 11-13)

### Issue 11: Docker Fundamentals
**Title:** Phase 4: Docker Setup & Basics  
**Labels:** docker, phase-4, week-11  
**Depends on:** Issue 10  
**Description:**

Learn containerization.

- [ ] Install Docker Desktop
- [ ] Understand images vs containers
- [ ] Run simple containers
- [ ] Explore Docker Hub
- [ ] Create Dockerfile
- [ ] Build custom image
- [ ] Push to Docker Hub

---

## Phase 5: Kubernetes (Weeks 14-16)

### Issue 12: Kubernetes Fundamentals
**Title:** Phase 5: Kubernetes Basics with Minikube  
**Labels:** kubernetes, phase-5, week-14  
**Depends on:** Issue 11  
**Description:**

Learn Kubernetes basics locally.

- [ ] Install Minikube and kubectl
- [ ] Start local cluster
- [ ] Understand pods, services, deployments
- [ ] Deploy simple application
- [ ] Explore cluster resources
- [ ] Practice scaling

---

## Phase 6: CI/CD Pipelines (Weeks 17-18)

### Issue 13: GitHub Actions
**Title:** Phase 6: GitHub Actions CI/CD  
**Labels:** cicd, github-actions, phase-6, week-17  
**Depends on:** Issue 12  
**Description:**

Automate testing and deployment.

- [ ] Understand workflow files
- [ ] Create simple workflow
- [ ] Add linting step
- [ ] Add testing step
- [ ] Build Docker image in workflow
- [ ] Push to registry
- [ ] Deploy application

---

## Phase 7: Monitoring & Capstone (Weeks 19-20)

### Issue 14: Capstone Project
**Title:** Phase 7: Capstone - Complete Platform  
**Labels:** capstone, phase-7, week-19-20  
**Depends on:** Issue 13  
**Description:**

Integrate all skills into one project.

- [ ] Design platform architecture
- [ ] Create infrastructure with Terraform
- [ ] Containerize application with Docker
- [ ] Deploy to Kubernetes
- [ ] Set up CI/CD with GitHub Actions
- [ ] Add monitoring with CloudWatch
- [ ] Write comprehensive documentation
- [ ] Create demo video (optional)
- [ ] Submit for portfolio review

---

## 📊 Summary

Total Issues: 14  
Total Phases: 7  
Total Weeks: 20  
Target Completion: September 1, 2026

**Status Tracking:**
- 🔴 Not Started
- 🟡 In Progress
- 🟢 Complete

---

**To implement these issues in GitHub:**

1. Create new repository: `pbc-platform-engineer`
2. Copy each issue as a GitHub Issue
3. Add labels, assignees, and dependencies
4. Link issues to milestones
5. Set target dates for each phase
6. Track progress weekly
