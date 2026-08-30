# Pipeline Architecture

## Purpose

This project applies automated security controls throughout the build process of a Dockerized Flask API.

## DevSecOps Flow

```mermaid
flowchart TD
    A["Push or pull request"] --> B["GitHub Actions"]
    B --> C["Tests and security scans"]
    C --> D["Collect and normalize findings"]
    D --> E{"Policy decision"}
    E -->|PASS| F["Publish validated image"]
    E -->|FAIL| G["Block and remediate"]
    F --> H["Generate SBOM and sign image"]
```

## Security Controls

| Stage | Control |
|---|---|
| Source code | Semgrep SAST |
| Dependencies | pip-audit SCA |
| Git history | Gitleaks |
| Configuration | Trivy Config |
| Container image | Trivy Image |
| Running application | OWASP ZAP DAST |
| Supply chain | Syft SBOM and Cosign signature |
| Risk decision | Policy-based security gates |

## Trust Boundaries

1. Developer workstation to GitHub repository.
2. GitHub repository to GitHub Actions runner.
3. Runner to the temporary application container.
4. Validated workflow to GitHub Container Registry.