---
toc_depth: 3
---

# News, Updates, and Changes

## 2025

### 2025-08-26 Use of Integrated Development Environments (IDEs)

Please do not use IDEs like VSCode "Remote - SSH" or Cursor Server to connect to Cheaha. These methods run all of their processes on the login node, which are automatically terminated. Instead, use "Remote - Tunnel" as described in the [VSCode Tunnel](./cheaha/open_ondemand/hpc_desktop.md#visual-studio-code-remote-tunnel) section. See [additional information](../getting_started.md#why-you-should-avoid-running-jobs-on-login-nodes) about running jobs on the Login node.

### 2025-05-13 Planned Maintenance Window

Cheaha compute nodes located at the Technology Innovation Center on campus will be undergoing maintenance from June 16-22, resulting in reduced CPU and GPU capacity during those days, as well as reduced memory limits for jobs. Please plan Research Computing needs around the maintenance window.

#### What You Can Expect

- Total CPU capacity will be reduced to 25 percent.
- “pascalnode” (P100) GPU capacity will be reduced to 50 percent.
- “amperenode” (A100) GPU capacity will be reduced to 75 percent.
- Jobs requesting more than 512 GB will be held in queue until the maintenance window is complete. Please contact us if large memory jobs must be run during maintenance.
- Researchers will be able to request at most 100 cores (reduced from 264) to more closely align with the reduced capacity.

We will monitor job performance throughout the week and may adjust quality of service values to ensure fairness.

#### Why We Are Making Changes

Planned growth requires UAB IT to move compute hardware from the TIC to the new data hall in the DC BLOX data center.

#### Other Upcoming Changes

In preparation for this maintenance, we will also be updating the hostname resolution for the OnDemand web endpoint rc.uab.edu and SSH endpoint cheaha.rc.uab.edu. These changes will be announced when scheduled and completed. They should not impact operations or user experience.

#### Data Migration Update

We are continuing the migration of all data from GPFS4 to GPFS5. This will be followed by deprecation of GPFS4. We encourage researchers to reach out to us if they want to migrate to GPFS5 at an earlier date of their choosing. GPFS4 is continuously close to capacity and allocations are over-subscribed. Migrating early will help us, your colleagues, and may help you avoid contention for limited space. If you wish to discuss early migration to GPFS5, please contact us.

#### Where to Get Help

If you need assistance, or have questions or concerns, please reply to this email or reach out to <support@listserv.uab.edu>.

### 2025-05-05 Research Computing Customer Survey

We are asking folks who use our services to complete our Research Computing Survey. We want the best information possible on how users enjoy the services we offer and what ideas you have for the future.
Please go to <https://uab.co1.qualtrics.com/jfe/form/SV_dbaFBqVXIVkSbum> to complete the survey by Friday, May 16 – it should take fewer than Five (5) minutes.

The [survey](https://uab.co1.qualtrics.com/jfe/form/SV_dbaFBqVXIVkSbum) is designed to gather feedback from UAB researchers, faculty, students, and staff on their use of Research Computing services. Your responses will help us better understand your resource needs, improve our services, and prioritize future enhancements. All responses are confidential and will be used solely for internal assessment and planning by UAB IT Research Computing.

### 2025-04-21 Planned Maintenance Window

- Planned Start: 2025-04-21 12:00 AM
- Anticipated End: 2025-04-28 12:00 AM
- Impacted Resources: Cloud.rc, Cheaha "amperenodes," "pascalnodes," and "intel-dcb" partitions.

Cloud.rc (OpenStack) and Cheaha nodes within DC Blox will be undergoing maintenance during the week of April 21, 2025. Cloud.rc and Cheaha "amperenodes,” "pascalnodes,” and "intel-dcb" partitions will be inaccessible during maintenance. Note this means all GPU nodes will be inaccessible. Planned growth requires us to move hardware within the DC BLOX data center. Please plan your Research Computing needs around this maintenance window. If you need additional assistance, please reply to this email or reach out to <support@listserv.uab.edu>.

The overall plan, which will increase capacity for planned hardware growth, includes:

- Migrating all our compute, compute-adjacent storage (GPFS), and cloud hardware to a new data hall in the DC BLOX data center.
- Housing long-term storage (LTS) and our expandable GPFS backend (Ceph) in our TIC data center, on campus.
- Upgrading from the end-of-life GPFS version 4 (GPFS4) to version 5 (GPFS5). More details about the storage upgrade will be discussed in the future.

We plan to do this in three phases.

- Phase 1: Migrate hardware from DC BLOX data hall 1 to data hall 2 the week of April 21, 2025.
- Phase 2: Transfer data from GPFS4 to GPFS5. We plan to do this with minimal downtime.
- Phase 3: Migrate remaining compute hardware from TIC to DCBlox. Dates TBD.

#### For GPFS5 Early Adopters

- Open OnDemand will be unavailable for the duration of the maintenance window.
- SSH will be available through an IP address, to be determined. To access this IP address you will need to be on the UAB VPN.

To explain further, as part of our storage platform upgrade from GPFS4 to GPFS5, we have duplicated essential login services. These include OOD and the Login Node, as well as a transparent Proxy Node. When you SSH into Cheaha the Proxy Node forwards your connection to the appropriate Login Node automatically.

The Proxy Node and GPFS5 OOD are both hosted on equipment that will be unavailable during the maintenance window (Cloud.rc/OpenStack). We will make the GPFS5 Login Node available directly, behind the UAB Firewall, with a specified IP address (to be determined).

How do I use the UAB VPN? Please see: <https://www.uab.edu/it/home/tech-solutions/network/vpn>.

### 2025-04-07 Reduced LTS Transfer Speeds on Globus

We are aware of increased transfer times into and out of LTS when using Globus. Transfer times are taking substantially longer than expected. The issue is occurring because of a bug in our version of Ceph, the LTS backend storage system. A bugfix is in the works by the vendor and we will communicate once we know more.

At this time, we recommend preferring to use [`s5cmd`](https://docs.rc.uab.edu/data_management/lts/interfaces#s5cmd) to transfer large amounts of data into and out of LTS.

Please feel free to [Contact Us](./help/support.md) for more information or alternative solutions.
