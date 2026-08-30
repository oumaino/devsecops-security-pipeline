# Pipeline Threat Model and Risk Register

## Scope

This threat model covers the source repository, GitHub Actions runners, security reports, Docker images and the publication process.

## Protected Assets

- Source code and Git history
- GitHub Actions workflows
- Credentials and workflow tokens
- Security reports and scan results
- Docker images and their integrity
- SBOM and provenance evidence

## Initial Risk Register

| ID | Threat scenario | Potential impact | Planned security measures | Status |
|---|---|---|---|---|
| T-01 | A compromised third-party GitHub Action executes malicious code in the runner | Code, reports or workflow credentials could be compromised | Pin actions to verified commit SHAs and apply minimum permissions | Planned |
| T-02 | A password, API key or token is committed to Git history | Unauthorized access and credential exposure | `.gitignore`, Gitleaks, immediate revocation and rotation | Planned |
| T-03 | A Docker image is replaced while retaining the same mutable tag | An untrusted image could be deployed | Reference images by digest and sign validated images with Cosign | Planned |
| T-04 | A missing scanner report is interpreted as a successful scan | A vulnerable build could incorrectly pass the security gate | Require all expected reports and classify missing results as `INCOMPLETE` | Planned |

## Risk Treatment Approach

The pipeline will initially observe and record findings without blocking every build. After the baseline has been reviewed, confirmed high-risk findings and missing mandatory reports will become blocking conditions.

## Review

This register will be updated when controls are implemented, findings are identified or security exceptions are approved.