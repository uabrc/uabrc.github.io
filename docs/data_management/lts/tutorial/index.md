---
toc_depth: 3
---
# LTS and S3 Basic Tutorial

Effective data management and sharing are essential for maintaining data integrity and facilitating collaboration in research. UAB’s Long-Term Storage (LTS) offers a robust solution for securely archiving data that may not be actively used but remains crucial for future research and compliance. The [`s3cmd`](https://s3tools.org/s3cmd) command-line tool complements this by enabling efficient management and transfer of files to and from LTS.

Why use LTS and `s3cmd` for your research data? LTS provides a secure and long term storage solution for preserving your valuable data over time. To manage this data efficiently, `s3cmd`is the key. `s3cmd` simplifies interactions with LTS, making it easy to upload, download, and organize your files. In addition, `s3cmd` allows you to define various policies including for read and read/write access to your data, enhancing security and control over your research data. Together, LTS and `s3cmd` provide an efficient approach to data management in your research workflow.

Below are the tutorials we currently have on using LTS and s3cmd:

- [Basic workflow with Individual LTS and s3cmd](./individual_lts_tutorial.md): This tutorial provides step-by-step instructions for moving files to and from your individual LTS allocation using the Cheaha system. It covers the installation, configuration and use of the different `s3cmd` commands, as well as setting up access policies.
- [Basic workflow with Shared LTS and s3cmd](./shared_lts_tutorial.md): This tutorial provides step-by-step instructions for configuring a shared LTS allocation using the Cheaha system. It covers bucket management, switching between individual and Shared LTS allocations profiles, using various s3cmd commands, and setting up access policies for shared LTS buckets.
