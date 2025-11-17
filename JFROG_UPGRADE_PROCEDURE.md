# JFrog Platform Upgrade Procedure

## Overview
This document outlines the procedures for upgrading JFrog Platform components used in this repository, including Frogbot and related dependencies.

## Table of Contents
1. [Pre-Upgrade Checklist](#pre-upgrade-checklist)
2. [Frogbot Version Upgrade](#frogbot-version-upgrade)
3. [Dependency Updates](#dependency-updates)
4. [JFrog Platform Configuration Updates](#jfrog-platform-configuration-updates)
5. [Testing and Validation](#testing-and-validation)
6. [Rollback Procedures](#rollback-procedures)
7. [Version Compatibility Matrix](#version-compatibility-matrix)

## Pre-Upgrade Checklist

Before proceeding with any upgrades, ensure the following:

- [ ] Review the latest [Frogbot release notes](https://github.com/jfrog/frogbot/releases)
- [ ] Check [JFrog Platform compatibility](https://jfrog.com/help/r/jfrog-platform-administration-documentation)
- [ ] Backup current workflow configurations
- [ ] Document current versions of all components
- [ ] Review any breaking changes in the changelog
- [ ] Notify team members about planned upgrade
- [ ] Ensure you have admin access to GitHub repository
- [ ] Verify JFrog Platform credentials are valid

## Frogbot Version Upgrade

### Current Configuration
The repository currently uses Frogbot v2 in `.github/workflows/frogbot-scan-pr.yml`.

### Upgrade Steps

1. **Check Latest Version**
   ```bash
   # Visit https://github.com/jfrog/frogbot/releases
   # Or use GitHub CLI
   gh release list --repo jfrog/frogbot --limit 5
   ```

2. **Update Workflow File**
   
   Edit `.github/workflows/frogbot-scan-pr.yml`:
   ```yaml
   steps:
     - uses: jfrog/frogbot@v2  # Change to desired version (e.g., @v2.x.x)
   ```

   Options for version specification:
   - `@v2` - Latest v2.x.x release (recommended for auto-updates)
   - `@v2.x.x` - Specific version (recommended for stability)
   - `@main` - Latest development version (not recommended for production)

3. **Review Breaking Changes**
   - Check the [migration guide](https://github.com/jfrog/frogbot#migration) if upgrading major versions
   - Review environment variable changes
   - Check for deprecated features

4. **Update Environment Variables**
   
   Verify the following secrets are configured in GitHub Settings → Secrets:
   - `JF_URL` - JFrog Platform URL
   - `JF_ACCESS_TOKEN` - JFrog access token
   - `GITHUB_TOKEN` - Automatically provided by GitHub

5. **Test the Upgrade**
   - Create a test pull request
   - Verify Frogbot scan completes successfully
   - Check scan results for accuracy
   - Review any new features or improvements

## Dependency Updates

### Python Dependencies

Current dependencies in `requirements.txt`:
- `requests==2.25.0`
- `flask==1.1.1`

### Update Procedure

1. **Check for Security Vulnerabilities**
   ```bash
   # Using pip-audit
   pip install pip-audit
   pip-audit -r requirements.txt
   ```

2. **Review Latest Versions**
   ```bash
   pip index versions requests
   pip index versions flask
   ```

3. **Update Dependencies**
   
   Update `requirements.txt` with new versions:
   ```
   requests==2.31.0  # or latest stable version
   flask==3.0.0      # or latest stable version
   ```

4. **Test Compatibility**
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install updated dependencies
   pip install -r requirements.txt
   
   # Run tests if available
   pytest tests/  # or your test command
   ```

5. **Security Scan with Frogbot**
   - Create a pull request with updated dependencies
   - Let Frogbot scan the changes
   - Review Frogbot's security findings
   - Address any vulnerabilities found

## JFrog Platform Configuration Updates

### Access Token Rotation

1. **Generate New Access Token**
   - Log in to JFrog Platform
   - Navigate to User Profile → Access Tokens
   - Create new token with appropriate scopes:
     - Read permissions for repositories
     - API access
   - Set expiration date

2. **Update GitHub Secret**
   - Go to GitHub Repository Settings → Secrets and Variables → Actions
   - Update `JF_ACCESS_TOKEN` with new token
   - Update `JF_URL` if JFrog Platform URL has changed

3. **Verify Connection**
   - Trigger Frogbot workflow manually
   - Check workflow logs for authentication success

### JFrog Platform URL Updates

If your JFrog Platform URL changes:

1. Update the `JF_URL` secret in GitHub
2. Format should be: `https://your-instance.jfrog.io`
3. Test connection with a manual workflow run

## Testing and Validation

### Post-Upgrade Testing Checklist

- [ ] Create test pull request
- [ ] Verify Frogbot workflow triggers automatically
- [ ] Check workflow execution completes without errors
- [ ] Verify Frogbot posts comments on PR
- [ ] Confirm vulnerability scanning works correctly
- [ ] Test with different PR scenarios:
  - [ ] New dependencies added
  - [ ] Existing dependencies updated
  - [ ] Security vulnerabilities introduced
  - [ ] Clean PR with no issues
- [ ] Verify permissions are working correctly
- [ ] Check Frogbot comment formatting and content

### Validation Commands

```bash
# Check workflow status
gh run list --workflow=frogbot-scan-pr.yml --limit 5

# View specific workflow run
gh run view <run-id>

# Check workflow logs
gh run view <run-id> --log
```

## Rollback Procedures

### Frogbot Version Rollback

If issues occur after upgrade:

1. **Identify Previous Version**
   ```bash
   git log -- .github/workflows/frogbot-scan-pr.yml
   ```

2. **Revert Workflow File**
   ```bash
   git checkout HEAD~1 -- .github/workflows/frogbot-scan-pr.yml
   git commit -m "Rollback Frogbot to previous version"
   git push
   ```

3. **Verify Rollback**
   - Check workflow runs with previous version
   - Confirm functionality restored

### Dependency Rollback

1. **Revert requirements.txt**
   ```bash
   git checkout HEAD~1 -- requirements.txt
   git commit -m "Rollback dependencies to previous versions"
   git push
   ```

2. **Clear Cache** (if using virtual environment)
   ```bash
   rm -rf venv
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Version Compatibility Matrix

| Component | Current Version | Recommended Version | Notes |
|-----------|----------------|---------------------|-------|
| Frogbot | v2 | v2.x.x (latest) | Check [releases](https://github.com/jfrog/frogbot/releases) |
| JFrog Platform | - | 7.x+ | Minimum required version |
| GitHub Actions | - | Latest | Auto-updated by GitHub |
| Python | 3.x | 3.8+ | For dependency compatibility |
| requests | 2.25.0 | 2.31.0+ | Security updates available |
| flask | 1.1.1 | 3.0.0+ | Major version update available |

## Best Practices

1. **Regular Updates**
   - Review Frogbot releases monthly
   - Update dependencies quarterly
   - Rotate access tokens every 90 days

2. **Version Pinning**
   - Use specific version tags for Frogbot in production
   - Pin dependency versions in requirements.txt
   - Document version choices in PR descriptions

3. **Testing**
   - Test upgrades in a separate branch first
   - Use pull requests for all changes
   - Monitor Frogbot scan results

4. **Documentation**
   - Keep this procedure updated
   - Document any custom configurations
   - Track upgrade history in git commits

5. **Security**
   - Never commit JFrog credentials to repository
   - Use GitHub Secrets for all sensitive data
   - Review Frogbot findings promptly
   - Address critical vulnerabilities immediately

## Troubleshooting

### Common Issues

**Frogbot workflow fails to authenticate:**
- Verify `JF_URL` and `JF_ACCESS_TOKEN` secrets are set correctly
- Check token hasn't expired
- Ensure token has required permissions

**Frogbot doesn't post comments:**
- Verify `pull-requests: write` permission in workflow
- Check `JF_GIT_TOKEN` is set to `${{ secrets.GITHUB_TOKEN }}`
- Review workflow logs for errors

**Dependency conflicts after update:**
- Check compatibility between packages
- Review dependency changelogs
- Consider incremental updates

**Workflow doesn't trigger:**
- Verify workflow file syntax
- Check trigger conditions (pull_request_target)
- Review branch protection rules

## Additional Resources

- [Frogbot Documentation](https://github.com/jfrog/frogbot)
- [JFrog Platform Documentation](https://jfrog.com/help/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)

## Maintenance Schedule

| Task | Frequency | Last Updated | Next Review |
|------|-----------|--------------|-------------|
| Frogbot Version Review | Monthly | - | - |
| Dependency Updates | Quarterly | - | - |
| Access Token Rotation | Every 90 days | - | - |
| Security Audit | Monthly | - | - |
| Documentation Review | Quarterly | - | - |

---

**Document Version:** 1.0  
**Last Updated:** 2025-11-17  
**Maintained By:** Repository Administrators
