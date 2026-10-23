# AWS 3-Tier Website

A web application built using AWS services with a frontend, Flask backend, and MySQL database.

## Architecture

1. **Frontend:** HTML and CSS
2. **Load Balancer:** AWS Application Load Balancer (ALB)
3. **Web Servers:** Two Amazon EC2 Ubuntu instances running Apache
4. **Backend:** Python Flask application
5. **Database:** Amazon RDS for MySQL
6. **Networking:** Amazon VPC, public and private subnets, Internet Gateway, and NAT Gateway
7. **Security:** Security Groups control traffic between application components

## Features

- Responsive website frontend
- Load balancing across two EC2 instances
- Flask API to retrieve visitor records
- MySQL database integration
- Apache reverse proxy to the Flask backend
- Flask service managed with systemd

## API Endpoint

`GET /visitors`

Returns visitor records from the MySQL database in JSON format.

## Project Files

- `index.html` — website frontend
- `app.py` — Flask backend
- `.gitignore` — excludes environment secrets and virtual environment
- `README.md` — project documentation

## Configuration

Database settings are stored in a local `.env` file. Never commit passwords, access keys, private keys, or other secrets to GitHub.

## Deployment Notes

- Configure the database endpoint and credentials using environment variables.
- Allow database port 3306 only from the backend server security group.
- Configure Apache to proxy `/visitors` to the local Flask service.
- Keep the RDS database in private subnets.

## AWS Region

Asia Pacific (Mumbai): `ap-south-1`

---
Built as a hands-on AWS 3-Tier Website project.
