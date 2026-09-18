# Network Scratch

Network scratch, also known as global scratch or user scratch, provides temporary, high-performance storage for data used in active computations. It is available on login nodes and also shared across compute nodes, making it suitable for data that needs to be accessed during jobs running on multiple nodes. Each user has access to this directory at `/scratch/$USER` or `$USER_SCRATCH`. Use it directory to store very large datasets or temporary pipeline intermediates for a short period of time while running your jobs. The maximum amount of data a single user can store in network scratch is 100 TB at any given time.

<!-- markdownlint-disable MD046 -->
!!! important

    Files in network scratch are deleted when their creation time and last access time are both 90 or more days ago. The purpose of this policy is to ensure network scratch and Cheaha remain performant and available for all researchers using the platform. Network scratch is temporary storage. It is not intended for archiving data or storing the only copy of important data. Please move data that must be retained to `/data/project/<project>`, `/data/user/$USER`, or Long-Term Storage (LTS), depending on the use case.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! warning

    Research Computing expects each user to keep their scratch areas clean. **The cluster scratch areas are not to be used for archiving data.**
<!-- markdownlint-enable MD046 -->

## Policies and Expectations

Data stored in `/scratch` is subject to two limited retention policies.

- Each user will have a quota of 100 TB of scratch storage.
- Files in network scratch are deleted when their creation time and last access time are both 90 or more days ago.
- Network scratch is temporary storage and should not be used for archiving data.
- Research Computing expects each user to keep their scratch area clean and remove unneeded files as soon as possible.
