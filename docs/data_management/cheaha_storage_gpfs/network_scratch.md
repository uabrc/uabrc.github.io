# Network Scratch

Network scratch, also known as global scratch or user scratch, provides temporary, high-performance storage for data used in active computations. It is available on login nodes and also shared across compute nodes, making it suitable for data that needs to be accessed during jobs running on multiple nodes. Each user has access to this directory at `/scratch/$USER` or `$USER_SCRATCH`. Use it directory to store very large datasets or temporary pipeline intermediates for a short period of time while running your jobs. The maximum amount of data a single user can store in network scratch is 100 TB at any given time.

<!-- markdownlint-disable MD046 -->
!!! important

    Starting January 2023, scratch data will have limited retention. See [Scratch Retention Policy](#policies-and-expectations) for more information.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! warning

    Research Computing expects each user to keep their scratch areas clean. **The cluster scratch areas are not to be used for archiving data.** In order to keep scratch clear and usable for everyone, files older than 30 days will be eligible for deletion.
<!-- markdownlint-enable MD046 -->

## Policies and Expectations

Data stored in `/scratch` is subject to two limited retention policies.

- Each user will have a quota of 100 TB of scratch storage.
- Files will be retained for a maximum of 30 days, after which they become eligible for deletion.
