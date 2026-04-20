# Domain Cache Detector (Django)

This project is a web-based application designed to detect DNS cache poisoning attacks using a combination of DNSSEC validation and machine learning techniques. It is built using the Django framework and aims to improve DNS-level security by identifying suspicious or manipulated DNS responses.

## Overview

The Domain Name System (DNS) plays a critical role in internet communication by translating domain names into IP addresses. However, DNS was not originally designed with strong security features, making it vulnerable to attacks such as cache poisoning. In such attacks, attackers inject false information into a DNS resolver’s cache, which can redirect users to malicious websites.

This project addresses this issue by analyzing DNS responses in real time and detecting anomalies using a Random Forest machine learning model along with DNSSEC verification.

## Features

* DNS query analysis using dnspython
* DNSSEC validation for authenticity checking
* Feature extraction including TTL, latency, mismatch ratio, and DNSSEC score
* Machine learning based classification using Random Forest
* Threat categorization into Low, Medium, and High levels
* Web-based dashboard built with Django
* Option to generate reports

## Technology Stack

Backend: Django (Python)
Machine Learning: Scikit-learn (Random Forest)
DNS Processing: dnspython
Frontend: HTML, CSS, JavaScript
Data Processing: Pandas, NumPy

## System Workflow

The system works in multiple stages:

1. DNS queries are performed for selected domains
2. Relevant features such as latency, TTL, and DNSSEC score are extracted
3. These features are passed into a trained Random Forest model
4. The model predicts the likelihood of cache poisoning
5. Results are displayed on the dashboard with a threat level

## Installation and Setup

Clone the repository:

git clone https://github.com/your-username/domain-cache-detector-django.git

Navigate to the project folder:

cd domain-cache-detector-django

Create a virtual environment:

python -m venv venv

Activate the environment (Windows):

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the server:

python manage.py runserver

## Project Report

The detailed project report is available in the repository:

DTU_Domain_Cache_Detector_Report.docx

It includes system design, methodology, implementation details, and analysis.

## Security Perspective

This project combines cryptographic verification through DNSSEC and intelligent detection using machine learning. It is capable of identifying suspicious DNS behavior even in environments where DNSSEC is not fully implemented.

## Limitations

* The system currently works on a predefined list of domains
* It is not fully real-time in its current version
* The machine learning model can be improved with a larger dataset

## Future Work

* Enable continuous real-time DNS monitoring
* Improve model performance using larger datasets and advanced algorithms
* Implement live alert systems such as email or notifications
* Deploy the application on a cloud platform

## Author

Mayur Patil
MTech (Cybersecurity)
