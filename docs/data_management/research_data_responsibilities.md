# Research Data Responsibilities

Data access responsibilities are a critical part of managing and securing research data and resources. These responsibilities ensure only authorized individuals have access to specified data, and maintain security, compliance, and operational efficiency.

Data access responsibilities come from applicable laws and regulations, grant funding agency requirements, and UAB institutional policies. If you have questions, concerns, or wish to discuss, please [Contact Us](../help/support.md).

## Shared Allocation

A shared allocation is owned by a PI of a Lab or director of Core facility. It is designed for sharing research data among staff, and collaborators where permissions and access control are typically managed by the PI/director or designated administrators/manager.

Shared storage owners, staff and students are responsible for overseeing and managing the allocations, including granting access to specific folders. However, Research Computing may provide support in certain cases. For example, if a folder becomes "locked" (i.e., no group members can change its permissions or access it), the owner of the allocation or the folder should submit a request for us to fix the issue. In addition, if you need assistance configuring or reconfiguring permissions, we can provide support as a convenience. Simply send us a request via <support@listserv.uab.edu>.

{{ read_csv('data_management/res/cheaha_project_directory.csv', keep_default_na=False) }}

## Individual Allocation

Individual allocations are intended for personal or individual use and are available to all UAB affiliated individuals or UAB employee's sponsored Collaborator. It is tied to the individual’s email and provide 5 TB of home/user directory on Cheaha and additional 5 TB of LTS allocation.

{{ read_csv('data_management/res/cheaha_individual_account.csv', keep_default_na=False) }}

## Data Archival and Backup Procedures

Researchers and users of Cheaha are responsible to organize data, archive inactive files, and back up critical data. For backup and archival solutions, please review our [Data Responsibilities and Procedures](./index.md#data-responsibilities-and-procedures) page. If you need backup and Archival assistance, we can discuss options based on your use cases. Please send us a support ticket via <support@listserv.uab.edu>.

## Security Exceptions for Accessing Former UAB Personnel Data

UAB IT has a process for granting access to data of former researchers or collaborators who are no longer with the institution. This process ensures compliance with regulatory protocols.

To request access to data of former UAB user, the first step is to fill out the [Third-Party Data Access form](https://uabprod.service-now.com/service_portal?id=sc_cat_item&sys_id=bd3721e2374c27c0daa253b543990e5d). We highly recommend requesting access to all three private storage areas. Consider adding the following to the "Justification/Description" box in the security exception form as you fill it out. Replace `<BlazerID>` with the BlazerID of the user you are requesting access for.

```text
Please grant access to "/data/user/", "/home/", "/scratch/" directories of `<BlazerID>`.
```

Once the form is submitted, a Service Request will be created. After the request is reviewed and authorized by appropriate parties, we will reach out to you.

If the owner of the data was your student or staff in your lab, then the first choice is probably best (two-levels up supervisor). If the data owner was in a different department or special approval is required (for example a professor in the dept of medicine wanting access to data from a student in the school of engineering), select "Dean, C-level, or Trusted Designee" for the "Approval Type" field. If written approval can be provided directly by the former personnel, you can bypassed completing the form for request.

To simplify data access and management, it is recommended to store critical research data in shared storage areas that are accessible to or owned by the responsible PI, with ownership transfer initiated as needed. If you need help with data management processes, please send us a support ticket via <support@listserv.uab.edu>, and we will guide you through these steps.

## User Responsibilities With UAB-IT Policies

All PIs, Core directors, researchers, students, users of UAB-owned computer systems, including Research Computing system, are responsible for adhering to the data and computing infrastructure policies set by UAB-IT.

- [Overall IT policy page](https://www.uab.edu/it/home/policies).
- [Acceptable Use Policy](https://secure4.compliancebridge.com/uab/portal/getdoc.php?file=300).
- [Data Protection and Security Policy](https://secure4.compliancebridge.com/uab/portal/getdoc.php?file=302).
- [Data Access Policy](https://secure4.compliancebridge.com/uab/portal/getdoc.php?file=301).
- [Data Classification](https://www.uab.edu/it/home/policies/data-classification/classification-overview).
