---
date: 2025-04-07T09:00:00-05:00
categories:
    - Known Issues
---

# Reduced LTS Transfer Speeds on Globus

We are aware of increased transfer times into and out of LTS when using Globus. Transfer times are taking substantially longer than expected. The issue is occurring because of a bug in our version of Ceph, the LTS backend storage system. A bugfix is in the works by the vendor and we will communicate once we know more.

<!-- more -->

At this time, we recommend preferring to use [`s5cmd`](../../data_management/lts/interfaces.md#s5cmd) to transfer large amounts of data into and out of LTS.

Please feel free to [Contact Us](../../help/support.md) for more information or alternative solutions.
