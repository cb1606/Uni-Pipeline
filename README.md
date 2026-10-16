# Uni-Pipeline

A beginner data engineering project demonstrating SQL, Python, data transformation, and ETL concepts using synthetic university-style academic data.

## Overview

Uni-Pipeline is a practical project designed to build data engineering skills by working with student records and academic performance data.

The project focuses on moving raw data through a simple pipeline, transforming it into a useful format, and preparing it for analysis.

## Project Goals

- Practise SQL data extraction
- Learn data cleaning and transformation with Python
- Understand ETL and ELT concepts
- Implement data quality checks
- Develop Git and GitHub version control skills
- Learn how to design and document data pipelines

## Current Features

- Student records stored in CSV format
- SQL-based student performance classification
- Python-based student performance transformation
- Git version control with a dedicated development branch

## Technologies

- Python
- SQL
- CSV
- Git
- GitHub

## Project Structure

    Uni-Pipeline/
    ├── data/
    │   ├── students.csv
    │   └── student_performance.csv
    ├── notebooks/
    ├── sql/
    ├── src/
    │   └── transform_students.py
    └── README.md

## Pipeline Overview

The planned pipeline follows these stages:

1. Extract student records from a source.
2. Validate and clean the data.
3. Transform student performance records.
4. Classify performance using defined rules.
5. Save the transformed data for analysis.

## Development Workflow

Git is used to track changes and maintain a history of project development.

1. Create a branch for a new feature or improvement.
2. Make changes to the project.
3. Review changes using `git diff`.
4. Stage files using `git add`.
5. Commit changes using `git commit`.
6. Push the branch to GitHub using `git push`.
7. Merge approved changes into the main branch when ready.

## Planned Improvements

- Add automated data quality checks
- Expand the Python transformation pipeline
- Improve SQL queries and data validation
- Add synthetic student, subject, and results datasets
- Explore Oracle Database integration
- Integrate Microsoft Fabric when suitable access is available
- Document the data model and pipeline architecture

## Data Privacy

This project is intended to use synthetic data for portfolio and learning purposes.

No real student records or confidential university data should be committed to this repository.

## Project Status

In progress. This project will evolve as new data engineering skills and tools are learned.
