# JFrog Platform Upgrade Quick Reference

Quick reference guide for common upgrade tasks. For detailed procedures, see [JFROG_UPGRADE_PROCEDURE.md](../JFROG_UPGRADE_PROCEDURE.md).

## Quick Actions

### Upgrade Frogbot to Latest Version

1. Edit `.github/workflows/frogbot-scan-pr.yml`
2. Update the version:
   ```yaml
   - uses: jfrog/frogbot@v2.x.x  # Replace with latest version
   ```
3. Commit and push
4. Test with a pull request

### Update Python Dependencies

1. Check current versions:
   ```bash
   cat requirements.txt
   ```

2. Update to latest:
   ```bash
   pip install --upgrade requests flask
   pip freeze | grep -E "requests|flask" > requirements_new.txt
   ```

3. Update `requirements.txt` with new versions
4. Create PR and let Frogbot scan for vulnerabilities

### Rotate JFrog Access Token

1. Generate new token in JFrog Platform
2. Update GitHub secret:
   - Settings → Secrets → Actions → `JF_ACCESS_TOKEN`
3. Trigger workflow to test

### Check Frogbot Status

```bash
# View recent workflow runs
gh run list --workflow=frogbot-scan-pr.yml --limit 5

# View specific run details
gh run view <run-id> --log
```

### Emergency Rollback

```bash
# Rollback Frogbot workflow
git checkout HEAD~1 -- .github/workflows/frogbot-scan-pr.yml
git commit -m "Rollback Frogbot version"
git push

# Rollback dependencies
git checkout HEAD~1 -- requirements.txt
git commit -m "Rollback dependencies"
git push
```

## Version Quick Check

| Component | Current | Latest Check Command |
|-----------|---------|---------------------|
| Frogbot | Check workflow file | `gh release list --repo jfrog/frogbot --limit 1` |
| requests | Check requirements.txt | `pip index versions requests \| head -5` |
| flask | Check requirements.txt | `pip index versions flask \| head -5` |

## Pre-Upgrade Checklist

- [ ] Check release notes
- [ ] Backup current configuration
- [ ] Test in separate branch
- [ ] Review breaking changes
- [ ] Update documentation

## Post-Upgrade Verification

- [ ] Workflow triggers successfully
- [ ] Frogbot posts comments
- [ ] No authentication errors
- [ ] Security scans complete
- [ ] All tests pass

## Support

For detailed procedures and troubleshooting, refer to the main [JFROG_UPGRADE_PROCEDURE.md](../JFROG_UPGRADE_PROCEDURE.md) document.
