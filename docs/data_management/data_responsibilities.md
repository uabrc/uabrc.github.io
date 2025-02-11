# Data Access Authorization and Responsibility

Data access authorization and responsibility are critical aspect of managing and securing research data and resources. It ensures that only authorized individuals have access to specific data, maintaining security, compliance, and operational efficiency.

## Cheaha Project directory

A Cheaha Project directory is owned by a PI of a Lab or director of core facility. It is designed for sharing research data among lab members, and collaborators where permissions and access control are typically managed by the PI/director or designated administrators/manager.

{{ read_csv('data_management/res/cheaha_project_directory.csv', keep_default_na=False) }}

## Personal Cheaha Account

Personal cheaha accounts are intended for personal or individual use and are available to all UAB affiliated individuals or UAB employee's sponsored Collaborator. These accounts are tied to the individual’s email and provide 5 TB of home/user directory.

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
    - Please restore from a backup.
- Natural disasters.
    - Examples: tornado; hurricane.
    - All of our data sits in one geographical location at the UAB Technology Innovation Center (TIC).
    - Plans to add geographical data redundancy are being considered.
    - Please restore from an offsite backup.
- Unusable backups.
    - Examples: backup software bug; media destroyed; natural disaster at offsite location.
    - Regularly test data restoration from all backups.

How can I ensure data integrity?

- Regularly back up your (and your lab's) data in an offsite location.
- [S3 based long-term storage (LTS)](lts/index.md) can be used for short-term onsite backup.
- Crashplan licenses are available for automatic offsite backups, please contact [Support](../help/support.md) for more information.

## Security Exceptions for Accessing Former UAB Personnel Data

## Data Handling in Shared and Personal Cheaha Accounts After Leaving UAB?
