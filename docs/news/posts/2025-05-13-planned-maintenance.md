---
date: 2025-05-13T09:00:00-05:00
categories:
    - Maintenance
---

# Planned Maintenance Window

Cheaha compute nodes located at the Technology Innovation Center on campus will be undergoing maintenance from June 16-22, resulting in reduced CPU and GPU capacity during those days, as well as reduced memory limits for jobs. Please plan Research Computing needs around the maintenance window.

<!-- more -->

## What You Can Expect

- Total CPU capacity will be reduced to 25 percent.
- “pascalnode” (P100) GPU capacity will be reduced to 50 percent.
- “amperenode” (A100) GPU capacity will be reduced to 75 percent.
- Jobs requesting more than 512 GB will be held in queue until the maintenance window is complete. Please contact us if large memory jobs must be run during maintenance.
- Researchers will be able to request at most 100 cores (reduced from 264) to more closely align with the reduced capacity.

We will monitor job performance throughout the week and may adjust quality of service values to ensure fairness.

## Why We Are Making Changes

Planned growth requires UAB IT to move compute hardware from the TIC to the new data hall in the DC BLOX data center.

## Other Upcoming Changes

In preparation for this maintenance, we will also be updating the hostname resolution for the OnDemand web endpoint rc.uab.edu and SSH endpoint cheaha.rc.uab.edu. These changes will be announced when scheduled and completed. They should not impact operations or user experience.

## Data Migration Update

We are continuing the migration of all data from GPFS4 to GPFS5. This will be followed by deprecation of GPFS4. We encourage researchers to reach out to us if they want to migrate to GPFS5 at an earlier date of their choosing. GPFS4 is continuously close to capacity and allocations are over-subscribed. Migrating early will help us, your colleagues, and may help you avoid contention for limited space. If you wish to discuss early migration to GPFS5, please contact us.

## Where to Get Help

If you need assistance, or have questions or concerns, please reply to this email or reach out to <support@listserv.uab.edu>.
