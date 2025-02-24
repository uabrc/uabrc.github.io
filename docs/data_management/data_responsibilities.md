# Data Access Authorization and Responsibility

Data access authorization and responsibility are critical aspect of managing and securing research data and resources. It ensures that only authorized individuals have access to specific data, maintaining security, compliance, and operational efficiency.

## Shared Allocation

A shared allocation is owned by a PI of a Lab or director of core facility. It is designed for sharing research data among lab members, and collaborators where permissions and access control are typically managed by the PI/director or designated administrators/manager.

PIs/Core directors and their Lab members are responsible for overseeing and managing the allocations, including granting access to specific folders. However, Research Computing may provide support in certain cases. For example, if a folder becomes "locked" (i.e., no group members can change its permissions or access it), the the owner of the allocation or the folder should submit a request for us to fix the issue. In addition, if you need assistance configuring or reconfiguring permissions, we can provide support as a convenience. Simply send us a request via <support@listserv.uab.edu>.

{{ read_csv('data_management/res/cheaha_project_directory.csv', keep_default_na=False) }}

## Individual Allocation

An individual allocations is intended for personal or individual use and is available to all UAB affiliated individuals or UAB employee's sponsored Collaborator. It is tied to the individual’s email and provide 5 TB of home/user directory on Cheaha and additional 5 TB of LTS allocation.

{{ read_csv('data_management/res/cheaha_individual_account.csv', keep_default_na=False) }}

## Data Archival and Backup Procedures

Proper data archival and backup practices ensure efficient storage utilization and data protection. IT is the responsibility of researchers and users of Cheaha to organize data, archive inactive files, and back up critical data.

### Archival

<!-- markdownlint-disable MD046 -->
!!! important

    Archival of data is the responsibility of researchers using Cheaha.
<!-- markdownlint-enable MD046 -->

At this time, Research Computing does not offer a method of archival. If you have need for archival, please feel free to contact [Support](../help/support.md) to start a conversation.

A possible external resource for archival is available through University of Oklahoma (OU) Supercomputing Center for Education and Research (OSCER). Please see the following link for details: <https://www.ou.edu/oscer/resources/ourrstore--ou---regional-research-store>.

### Backups

<!-- markdownlint-disable MD046 -->
!!! important

    Backups of data are the responsibility of researchers using Cheaha.
<!-- markdownlint-enable MD046 -->

A good practice for backing up data is to use the 3-2-1 rule, as [recommended by US-CERT](https://www.cisa.gov/sites/default/files/publications/data_backup_options.pdf):

- **3**: Keep **3** copies of important data. 1 primary copy for use, 2 backup copies.
- **2**: Store backup copies on **2** different media types to protect from media-specific hazards.
- **1**: Store **1** backup copy offsite, located geographically distant from the primary copy.

What hazards can cause data loss?

- Accidental file deletion.
    - Example: mistakenly deleting the wrong files when using the [shell command](../workflow_solutions/shell.md#delete-files-and-directories-rm-rmdir) `rm`.
    - Files deleted with `rm` or any similar command can not be recovered by us under any circumstances.
- Natural disasters.
    - Examples: tornado; hurricane.
    - All of our data sits in one geographical location at the UAB Technology Innovation Center (TIC).
    - Plans to add geographical data redundancy are being considered.
If you have backup needs, we can discuss options based on your use case. We want to engage in a conversation. please send us a support ticket via <support@listserv.uab.edu>.

## Security Exceptions for Accessing Former UAB Personnel Data

UAB IT has a process for granting access to data of former researchers or collaborators who are no longer with the institution. This process ensures compliance with regulatory protocols.

To request access to data of former UAB user, the first step is to fill out the [Third-Party Data Access form](https://uabprod.service-now.com/service_portal?id=sc_cat_item&sys_id=bd3721e2374c27c0daa253b543990e5d). In the “justification/description” field specify that you are requesting access to data for `<BlazerId>` on GPFS at the Research Computing System. Once submitted this form, a ticket is created and routed to the appropriate reviewers for authorization.

If the owner of the data was your student or staff in your lab, then the first choice is probably best (two-levels up supervisor). If the data owner was in a different department or special approval is required (for example a professor in the dept of medicine wanting access to data from a student in the school of engineering), select "Dean, C-level, or Trusted Designee" for the "Approval Type" field. If written approval can be provided directly by the former personnel, you can bypassed completing the form for request.

To simplify data access and management, it is recommended to store critical research data in shared storage areas that are accessible to or owned by the responsible PI, with ownership transfer initiated as needed. If you need help with data management process, please send a support ticket via <support@listserv.uab.edu>, and we will guide you through these steps.

## User responsibilities with UAB-IT policies

All PIs, Core directors, researchers, students, users of UAB-owned computer systems, including Research Computing system, are responsible for adhering to the data and computing infrastructure policies set by UAB-IT.

- [Overall IT policy page](https://www.uab.edu/it/home/policies).
- [Acceptable Use Policy](https://secure4.compliancebridge.com/uab/portal/getdoc.php?file=300).
- [Data Protection and Security Policy](https://secure4.compliancebridge.com/uab/portal/getdoc.php?file=302).
- [Data Access Policy](https://secure4.compliancebridge.com/uab/portal/getdoc.php?file=301).
- [Data Classification](https://www.uab.edu/it/home/policies/data-classification/classification-overview).
