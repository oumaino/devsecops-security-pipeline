# Automated DevSecOps Security Pipeline

A portfolio project for building a reproducible DevSecOps pipeline around a Dockerized Flask API.

The pipeline will integrate automated testing, SAST, SCA, secret scanning, configuration scanning, container security, SBOM generation and DAST. Security findings will be collected, normalized and evaluated using risk-based security gates.

**Status:** In progress — Day 2 complete

## Ethical Scope

All security tests are limited to this repository, its local application and its authorized GitHub Actions runners.

## Current Implementation

- Flask JSON API with `/` and `/health` endpoints
- Baseline HTTP security headers
- Automated tests with Pytest
- Docker image running as a non-root user
- Gunicorn production application server
- Docker health check
- GitHub Actions jobs for tests and Docker builds