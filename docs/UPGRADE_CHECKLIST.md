# Upgrade Checklist Template

Use this checklist when performing upgrades to JFrog Platform components.

## Upgrade Information

- **Date:** _____________________
- **Performed By:** _____________________
- **Upgrade Type:** [ ] Frogbot [ ] Dependencies [ ] JFrog Platform Config [ ] Other: _____________________
- **Branch Name:** _____________________
- **Pull Request:** _____________________

## Pre-Upgrade Steps

- [ ] Review release notes and changelog
- [ ] Check compatibility matrix
- [ ] Document current versions
- [ ] Create backup branch
- [ ] Notify team members
- [ ] Verify access credentials

### Current Version Information

| Component | Current Version | Target Version |
|-----------|----------------|----------------|
| Frogbot | | |
| requests | | |
| flask | | |
| Other: | | |

## Upgrade Execution

### Configuration Changes

- [ ] Update `.github/workflows/frogbot-scan-pr.yml` (if applicable)
- [ ] Update `requirements.txt` (if applicable)
- [ ] Update GitHub secrets (if applicable)
- [ ] Update documentation

### Files Modified

```
List files that were modified during upgrade:
- 
- 
- 
```

### Commands Executed

```bash
# Document commands used during upgrade


```

## Testing and Validation

- [ ] Create test pull request
- [ ] Verify workflow triggers
- [ ] Confirm Frogbot scan completes
- [ ] Check Frogbot comments appear
- [ ] Verify security scan results
- [ ] Test dependency installation
- [ ] Run application tests
- [ ] Check for runtime errors

### Test Results

```
Document test results:


```

## Post-Upgrade Verification

- [ ] All tests passing
- [ ] No authentication errors
- [ ] Workflow permissions correct
- [ ] Security scans functional
- [ ] Documentation updated
- [ ] Team notified of completion

## Issues Encountered

```
Document any issues encountered and how they were resolved:


```

## Rollback Plan

- [ ] Documented rollback steps if needed
- [ ] Tested rollback procedure (if required)

### Rollback Commands (if needed)

```bash
# Commands to rollback changes


```

## Sign-Off

- [ ] Upgrade completed successfully
- [ ] All tests passing
- [ ] Documentation updated
- [ ] PR merged

**Completed By:** _____________________  
**Date:** _____________________  
**PR Link:** _____________________

## Notes

```
Additional notes or observations:


```

---

**Template Version:** 1.0  
**Last Updated:** 2025-11-17
