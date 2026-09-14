
# RCS Onboarding for New PIs

Are you a new PI joining UAB? Welcome to UAB-IT Research Computing System. Below is the information we need to ensure you have the best experience and the fastest possible startup.

Please review the sections on this page and contact <support@listserv.uab.edu> to begin the onboarding conversation, or join our [Zoom Office Hours](../index.md#how-to-contact-us) for live assistance.

<!-- markdownlint-disable MD046 -->

=== "Who Will Be Onboarding With You?"

    ### Team Members?
    All team members, including the PI, will need to create [Research Computing System Account](rcs/create.md)

    ## Do You Want to Designate a Data Manager?
    PIs can designate a "Data Manager" who will:

    - Serve as the primary point of contact for data transfers and initial data management
    - Manage day‑to‑day data operations (For example: [access control](../workflow_solutions/shell.md#manage-researcher-access-to-files-and-directories-getfacl-setfacl), [directory structure](../data_management/storage/cheaha_storage_gpfs/project_directories.md#project-directory-organization))
    - Coordinate shared storage requests and oversee user access for shared allocations.

=== "Data Transfer"

    Are you transferring data from another institution?

    - How much data in TB?
    - Does your institution have a Globus subscription?
    - How did you transfer data from your storage systems at your previous institution?
    - How can we contact your institution's Research Computing or IT group responsible for assisting with data transfers?
    - Do you have a Data Use Agreement from your institution authorizing you to transfer the data?
    - Which parts of your data require special security considerations?
        - RCS is equipped to handle HIPAA and NIST 800-171 data.
        - We offer several [data transfer options](../data_management/transfer/index.md).
        - Anything else? Please let us know.

=== "Storage & Access"

    ## Shared Storage Allocations
    In addition to their individual allocations, PIs and Core Directors are eligible to request Shared [GPFS](../data_management/storage/cheaha_storage_gpfs/index.md) or [LTS](../data_management/storage/lts/index.md) allocations for collaborative work and project data storage needs.

    To request shared storages, please refer to the [storage request guide](../data_management/storage/index.md#how-do-i-request-shared-storage). You will need to include:

    - A list of team members who will need access to the shared allocation, if any.
    - Sensitive data requirements, if any.
    - Data Manager designated as steward, if any.

    **Note**: Please make sure all team members who will have access to the shared allocation and the PI have created a [Research Computing System Account](rcs/create.md).
    ## Access Control
    Members can access data in a shared allocation in different ways, depending on the type of shared allocation.

    === "Cheaha Project Directory"

        For [Cheaha Project Directory](../data_management/storage/cheaha_storage_gpfs/project_directories.md), members can access data through two methods:

          - Unix Group membership: Access to data in Cheaha project directory is granted through Unix group assignments. Users may be added based on a request from the Data Manager with PI approval, or through a direct request from the PI.
          - [Access Control Lists (ACLs)](../workflow_solutions/shell.md#manage-researcher-access-to-files-and-directories-getfacl-setfacl): Permissions applied to specific files or directories, with access requests handled the same way as Group membership, or the allocation owner can grant the required permissions directly.

    === "Long-term storage (LTS)"

        For [LTS](../data_management/storage/lts/index.md), members can access data through [Bucket policies](../data_management/storage/lts/iam_and_policies.md#bucket-policies).

    Once the appropriate access permissions have been configured, members can transfer or access data using the available [data transfer tools](../data_management/transfer/index.md#data-management-and-transfer-tools).

=== "Compute (Cheaha)"

    ## Getting Started on Cheaha
    Once accounts and storage are set up, your team can begin using Cheaha, and other Research Computing services.

    First steps:

    - [Login to Cheaha](../cheaha/getting_started.md#accessing-cheaha)
    - Test compute node access and learn about the differences between [Login and Compute Nodes](../cheaha/getting_started.md#login-vs-compute-nodes)
    - [Use modules](../cheaha/software/modules.md) and [software environments](../cheaha/software/software.md)
    - Explore additional services:
     - [UAB Cloud](../uab_cloud/index.md)
     - [Code.rc (GitLab)](../code.rc/index.md)
     - [Outreach & Training](../education/courses.md)

<!-- markdownlint-enable MD046 -->

## Expectations and Responsibilities

PIs are responsible for maintaining appropriate administrative security controls for their data. We provide guidance and a secure platform to support compliant data management.

All PIs, Core Directors, researchers, students, and any users of UAB‑owned computer systems are responsible for adhering to the data and computing infrastructure [policies](../data_management/research_data_responsibilities.md#user-responsibilities-with-uab-it-policies) set by UAB-IT.
