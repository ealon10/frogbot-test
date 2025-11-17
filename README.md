# frogbot-test

A test repository for JFrog Frogbot security scanning integration with GitHub.

## Overview

This repository demonstrates the integration of JFrog Frogbot for automated security scanning of pull requests. Frogbot scans for vulnerabilities in project dependencies and provides feedback directly in pull request comments.

## Features

- Automated security scanning on pull requests
- Vulnerability detection in Python dependencies
- Integration with JFrog Platform

## Documentation

- **[JFrog Platform Upgrade Procedure](JFROG_UPGRADE_PROCEDURE.md)** - Comprehensive guide for upgrading JFrog Platform components, Frogbot, and dependencies
- **[Quick Reference Guide](docs/UPGRADE_QUICK_REFERENCE.md)** - Quick reference for common upgrade tasks

## Getting Started

### Prerequisites

- JFrog Platform account
- GitHub repository with appropriate permissions
- Python 3.8 or higher

### Configuration

The repository is configured with Frogbot scanning via GitHub Actions. The workflow is triggered on pull requests and requires the following secrets:

- `JF_URL` - Your JFrog Platform URL
- `JF_ACCESS_TOKEN` - JFrog access token with appropriate permissions

### Dependencies

Current Python dependencies are listed in `requirements.txt`:
- `requests==2.25.0`
- `flask==1.1.1`

## Maintenance

For information on maintaining and upgrading JFrog Platform components, refer to the [JFrog Platform Upgrade Procedure](JFROG_UPGRADE_PROCEDURE.md).

## Contributing

When contributing to this repository:

1. Create a new branch for your changes
2. Ensure all dependencies are properly scanned by Frogbot
3. Address any security vulnerabilities identified
4. Follow the upgrade procedures when updating dependencies

## Resources

- [Frogbot Documentation](https://github.com/jfrog/frogbot)
- [JFrog Platform Documentation](https://jfrog.com/help/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
