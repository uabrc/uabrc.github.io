---
date: 2026-08-12T09:00:00-05:00
categories:
    - Security Issues
---

# Security Issues

## IGV

<!-- markdownlint-disable MD046 -->
!!! danger

    Versions of IGV prior to `2.11.9` use a compromised version of log4j. Those versions are affected by a serious [remote code execution issue](https://www.cve.org/CVERecord?id=CVE-2021-44832). Please transition your software to use versions of IGV >= `2.11.9`.
<!-- markdownlint-enable MD046 -->

## GSEA

<!-- more -->

<!-- markdownlint-disable MD046 -->
!!! danger

    Versions of GSEA prior to `4.2.3` use a compromised version of log4j. Those versions are affected by a serious [remote code execution issue](https://www.cve.org/CVERecord?id=CVE-2021-44832). Please transition your software to use versions of GSEA >= `4.2.3`.
<!-- markdownlint-enable MD046 -->

## Rsync

<!-- markdownlint-disable MD046 -->
!!! danger

    Versions of Rsync prior to `3.4.0` contain [six known vulnerabilities](https://www.openwall.com/lists/oss-security/2025/01/14/3), some of which allow for arbitrary code execution. The risk to our system is minimal because of scoped user permissions. Nevertheless, Cheaha is now using version 3.4.1. Older versions have been removed, apologies for any inconvenience.
<!-- markdownlint-enable MD046 -->
