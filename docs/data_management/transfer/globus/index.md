# Globus

<!-- markdownlint-disable MD046 -->
!!! announcement

    We are aware of reduced transfer speed into and out of [Long-Term Storage (LTS)](../../storage/lts/index.md) when using Globus and are working on a solution. For some use cases, [`s5cmd`]( ../../storage/lts/interfaces.md#s5cmd) may be a faster alternative. Please see [Our News Section](../../../news/posts/2025-04-07-reduced-lts-transfer-speeds-on-globus.md) for more information.
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

Below are the main topics covered here to help you get started with Globus and its key features.

- Install Globus Connect Personal (GCP): Turn your personal computer into a Globus endpoint. Only specific folders are accessible by default.
- Set up and use GCP: Log in, configure your endpoint, select folders, and start transferring files.
- Globus for Individuals: Using Globus as a researcher for personal data transfers.
- Globus for Organizations (Labs and Cores): Shared endpoints for labs and research cores, with centralized management
- Globus for Group Management: Manage access to data via teams and project groups.

Globus allows you to transfer data to and/or from collections (endpoints). UAB Research Computing currently supports the following endpoints:

- Remote Endpoints: UAB Research Computing currently supports the following three remote endpoints.
    - UAB Research Computing LTS (Long Term Storage aka S3)
    - UAB RCS Cheaha HPC
    - UAB Box

- Local Endpoints: These are collections that you can create on your own computer (laptops, desktops, workstations, and other self-managed systems) with Globus Connect Personal (GCP).

<!-- markdownlint-disable MD046 -->
!!! important

    To use UAB Research Computing endpoints, you will need to ensure you are using your UAB identity.
<!-- markdownlint-enable MD046 -->
