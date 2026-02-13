# Globus

<!-- markdownlint-disable MD046 -->
!!! announcement

    We are aware of reduced transfer speed into and out of [Long-Term Storage (LTS)](../../storage/lts/index.md) when using Globus and are working on a solution. For some use cases, [`s5cmd`]( ../../storage/lts/interfaces.md#s5cmd) may be a faster alternative. Please see [Our News Section](../../../news/posts/2025-04-07-reduced-lts-transfer-speeds-on-globus.md) for more information.

     Access to Cheaha storage (GPFS) is now available through the new Globus mapped collection "**UAB RCS Cheaha HPC**" for both on-campus and off-campus connections. The new mapped collection replaces the previous "Cheaha cluster on-campus (UAB Science DMZ)" and "Cheaha cluster off-campus (UAB Science DMZ)" mapped collections. This change comes from our recently completed GPFS5 migration and unifies access to Cheaha storage via Globus.
<!-- markdownlint-enable MD046 -->

Globus is a powerful tool for robustly and securely managing data transfers to and from collaborators and within UAB Research Computing. Globus is a GUI-based application and recommended for most single-use and day-to-day data transfer needs.

<!-- markdownlint-disable MD046 -->
!!! note

    UAB Research Computing uses High Assurance Endpoints, meaning there are additional security measures in place to reduce risk and move toward HIPAA compliance. Generally speaking, if you have used Globus in the past, the data transfer interface has not changed, but there are a few new restrictions/changes.

    1. You will be prompted to prove authorization each time you access a UAB Research Computing endpoint or attempt to download files to your local machine from such an endpoint. If you are already logged in with Single Sign-On (SSO) the process is simple. If not, you will need to authenticate with SSO.
    1. Bookmarks are not allowed in High Assurance endpoints.

    For more detailed information on High Assurance please see the Globus official pages below:

    - [High Assurance Security Overview](https://docs.globus.org/guides/overviews/security/high-assurance-overview/)
    - [High Assurance Collections](https://docs.globus.org/guides/overviews/high-assurance/)
<!-- markdownlint-enable MD046 -->

## Globus Endpoints

The following Globus collection (endpoints) are currently available and supported by UAB Research Computing for transferring data to and from collections within the UAB Research Computing storage systems:

- Remote Globus Collection (Endpoints): UAB Research Computing currently supports the following three remote Globus endpoints.
    - UAB Research Computing LTS (Long Term Storage aka S3): Access data on [Long Term Storage (LTS)](../../storage/lts/index.md).
    - UAB RCS Cheaha HPC: Access data on GPFS, including [User Data and Home directories](../../storage/cheaha_storage_gpfs/individual_directories.md), [Scratch](../../storage/cheaha_storage_gpfs/network_scratch.md), and [Project Directories](../../storage/cheaha_storage_gpfs/project_directories.md).
    - UAB Box: Access data on UAB Box.

- Local (Personal) Endpoints: These are Globus collections that you can create on your own computer (laptops, desktops, workstations, and other self-managed systems) with [Globus Connect Personal (GCP)](./gcp_setup.md).

<!-- markdownlint-disable MD046 -->
!!! important

    To use UAB Research Computing endpoints, you will need to ensure you are using your UAB identity.
<!-- markdownlint-enable MD046 -->

Refer to the topics below to learn how to get started with Globus and use its key features.

- [Getting Started](./login_to_globus.md): Access the Globus Web App and login with UAB credentials.
- [Install Globus Connect Personal (GCP)](./gcp_install.md): Turn your personal computer into a Globus endpoint. Only specific folders are accessible by default.
- [Set up and use Globus Connect Personal (GCP)](./gcp_setup.md): Log in, configure your endpoint, select folders, and start transferring files.
- [Globus for Individuals](./globus_individual_tutorial.md): Using Globus as a researcher for personal data transfers.
- [Globus for Organizations (Labs and Cores)](./globus_organization_tutorial.md): Shared endpoints for labs and research cores, with centralized management
- [Globus for Group Management](./globus_group_management.md): Manage access to data via teams and project groups.
