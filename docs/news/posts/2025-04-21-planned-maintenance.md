---
date: 2025-04-21T09:00:00-05:00
categories:
    - Maintenance
---

# Planned Maintenance Window

- Planned Start: 2025-04-21 12:00 AM
- Anticipated End: 2025-04-28 12:00 AM
- Impacted Resources: Cloud.rc, Cheaha "amperenodes," "pascalnodes," and "intel-dcb" partitions.

Cloud.rc (OpenStack) and Cheaha nodes within DC Blox will be undergoing maintenance during the week of April 21, 2025. Cloud.rc and Cheaha "amperenodes,” "pascalnodes,” and "intel-dcb" partitions will be inaccessible during maintenance. Note this means all GPU nodes will be inaccessible. Planned growth requires us to move hardware within the DC BLOX data center. Please plan your Research Computing needs around this maintenance window. If you need additional assistance, please reply to this email or reach out to <support@listserv.uab.edu>.

<!-- more -->

The overall plan, which will increase capacity for planned hardware growth, includes:

- Migrating all our compute, compute-adjacent storage (GPFS), and cloud hardware to a new data hall in the DC BLOX data center.
- Housing long-term storage (LTS) and our expandable GPFS backend (Ceph) in our TIC data center, on campus.
- Upgrading from the end-of-life GPFS version 4 (GPFS4) to version 5 (GPFS5). More details about the storage upgrade will be discussed in the future.

We plan to do this in three phases.

- Phase 1: Migrate hardware from DC BLOX data hall 1 to data hall 2 the week of April 21, 2025.
- Phase 2: Transfer data from GPFS4 to GPFS5. We plan to do this with minimal downtime.
- Phase 3: Migrate remaining compute hardware from TIC to DCBlox. Dates TBD.

## For GPFS5 Early Adopters

- Open OnDemand will be unavailable for the duration of the maintenance window.
- SSH will be available through an IP address, to be determined. To access this IP address you will need to be on the UAB VPN.

To explain further, as part of our storage platform upgrade from GPFS4 to GPFS5, we have duplicated essential login services. These include OOD and the Login Node, as well as a transparent Proxy Node. When you SSH into Cheaha the Proxy Node forwards your connection to the appropriate Login Node automatically.

The Proxy Node and GPFS5 OOD are both hosted on equipment that will be unavailable during the maintenance window (Cloud.rc/OpenStack). We will make the GPFS5 Login Node available directly, behind the UAB Firewall, with a specified IP address (to be determined).

How do I use the UAB VPN? Please see: <https://www.uab.edu/it/home/tech-solutions/network/vpn>.
