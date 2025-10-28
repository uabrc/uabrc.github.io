# Data Management and Transfer Tools

We currently support the following tools on Cheaha to manage data transfers. You can find information for the following tools and services we support;

1. [Globus](./globus.md)
1. [Filezilla](./filezilla.md)
1. [Rclone](./rclone.md)

We also have tutorials to guide your data transfer needs;

1. [Data Transfer (Globus)](../transfer/tutorial/index.md)

## What Data Sharing Method Works Best for My Collaboration?

Choosing the right data sharing tool/method depends on how often you transfer data and who needs access to it. Below are some common scenarios and our recommendations.

## Infrequent Transfer of Your Data

If you are sending data Infrequently, for example, to share results with a collaborator, think about whether the transfer is a copy or a move.

- If the transfer is a copy: You are keeping your own copy. Keep in mind that your version and the recipient’s version may be out of sync over time.

- If the transfer is a move: After confirming the recipient has retrieved the data, it is good practice to delete your local copy to free up storage space.

- **Recommended method:** [Globus](../transfer/globus.md) is the easiest and most robust option. It is also simple to restrict who has access.
    - Put the data into a special directory.
    - [Create a shared Globus collection](../transfer/globus.md#creating-a-guest-collection).
    - [Sharing the collection](../transfer/tutorial/globus_organization_tutorial.md#how-do-i-share-a-collection-with-others) to the intended recipient.

If you expect your collaboration to expand, in the future, use a shared storage allocation ([GPFS](../cheaha_storage_gpfs/project_directories.md) or [LTS](../lts/index.md)). This option allows ongoing collaboration but requires more attention to access control, especially if your data falls under security requirements (e.g.HIPAA, NIST 800-171, CUI, and ITAR).  Collaborations using shared allocations can be managed in two ways:

- Have the intended recipient add you to their shared allocation so you can retrieve/store data.
- Add the intended recipient to your shared allocation so they can retrieve/store data. If the recipient is external, they will need to create a [XIAS account](../../account_management/xias/index.md) .

Always restrict access to only the intended directories or buckets. Examples of access control:

- GPFS: Set [ACLs](../../workflow_solutions/shell.md#manage-researcher-access-to-files-and-directories-getfacl-setfacl) on all other directories with restricted user permissions.
- LTS: Append a [bucket policy](../lts/iam_and_policies.md#bucket-policies) restricted to the specific data and specific user.

## Frequent Transfer of Your Data

If you frequently exchange data, the same principles for infrequent data transfer still apply, but automation becomes important. Consider using Globus Flows or Globus Compute for automated and repeatable workflows. When multiple collaborators need to analyze the same data simultaneously, Globus may no longer be the best option. In that case, use a shared allocation([GPFS](../cheaha_storage_gpfs/project_directories.md) or [LTS](../lts/index.md)) so everyone can work directly with the data in place.

If the collaborator is external, you can still exchange data regularly within shared allocations([GPFS](../cheaha_storage_gpfs/project_directories.md) or [LTS](../lts/index.md)), however, they will need to create a [XIAS account](../../account_management/xias/index.md).

<!-- markdownlint-disable MD046 -->
!!! important
    As always, ensure that appropriate access controls and security practices are applied to protect your data.
<!-- markdownlint-enable MD046 -->
