---
toc_depth: 3
---

# News, Updates, and Changes

## 2025

### 2025-04-21 Planned Maintenance Window

- Planned Start: 2025-04-21 12:00 AM
- Anticipated End: 2025-04-28 12:00 AM
- Impacted Resources: Cloud.rc, Cheaha "amperenodes," "pascalnodes," and "intel-dcb" partitions.

Cloud.rc (OpenStack) and Cheaha nodes within DC Blox will be undergoing maintenance during the week of April 21, 2025. Cloud.rc and Cheaha "amperenodes,” "pascalnodes,” and "intel-dcb" partitions will be inaccessible during maintenance. Note this means all GPU nodes will be inaccessible. Planned growth requires us to move hardware within the DC BLOX data center. Please plan your Research Computing needs around this maintenance window. If you need additional assistance, please reply to this email or reach out to [support@listserv.uab.edu](mailto:support@listserv.uab.edu).

The overall plan, which will increase capacity for planned hardware growth, includes:

- Migrating all our compute, compute-adjacent storage (GPFS), and cloud hardware to a new data hall in the DC BLOX data center.
- Housing long-term storage (LTS) and our expandable GPFS backend (Ceph) in our TIC data center, on campus.
- Upgrading from the end-of-life GPFS version 4 (GPFS4) to version 5 (GPFS5). More details about the storage upgrade will be discussed in the future.

We plan to do this in three phases.

- Phase 1: Migrate hardware from DC BLOX data hall 1 to data hall 2 the week of April 21, 2025.
- Phase 2: Transfer data from GPFS4 to GPFS5. We plan to do this with minimal downtime.
- Phase 3: Migrate remaining compute hardware from TIC to DCBlox. Dates TBD.
