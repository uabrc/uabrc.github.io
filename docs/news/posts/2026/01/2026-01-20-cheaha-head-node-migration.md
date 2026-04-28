---
date: 2026-01-20T17:00:00-06:00
categories:
    - Maintenance
---

# 2026-01-30 Cheaha Head Node Migration

We will be moving the Cheaha head node from GPFS4 to GPFS5. Maintenance is scheduled from 5:00 PM January 30th, 2026 to 6:00 AM January 31st, 2026. During this time Cheaha will be unavailable. This move marks the final part of our storage infrastructure upgrade and data migration.

How will this impact your work?

- Cheaha will be unavailable, including via Open OnDemand (OOD at <https://rc.uab.edu>) and SSH.
- The Slurm scheduler, database, and supporting services will be offline.
- All jobs are submitted with a time limit. If the time from submission until maintenance is shorter than a job's time limit, that job will be held in queue until maintenance ends. This means jobs will not run during maintenance, ensuring jobs maintain a consistent state and do not need to be re-run.

<!-- more -->

The head node is being migrated to the GPFS5 filesystem to finalize the storage upgrade and data migration. With the head node on GPFS5, we can retire the GPFS4 storage platform. This final window positions us for further system improvements in year ahead.

We appreciate your patience as we make this important change.
