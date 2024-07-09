# User Accounts and Responsibilities

## Who can access Research Computing systems?

### UAB Employees and Students

- **Eligibility**: Must have an active BlazerID
- **Includes**:
    - UAB Campus and UAB Medicine
    - Faculty, Staff, Postdocs, and Graduate Students

**Note**: Undergraduate student access is not available, apologies for any inconvenience.

### External Collaborators

- **Requirements**: Must be sponsored by UAB Employee.
- **Sponsor's Responsibility**: The sponsor is accountable for any actions taken by the External collaborator on UAB systems. For detail information, please refer to [external collaborators](./xias/index.md/#external-collaborator-xias-accounts) page.

## What are my responsibilities?

In research computing systems, resources are shared among multiple users, and your actions can significantly impact the system and affect others. All users are expected to use their Cheaha account, storage, and computational resources responsibly and professionally. All users are advised to adhere the following responsibilities:

- **Lab PIs and Core Directors**:

    - Data Management and Storage:
        - Periodically check group membership is correct
        - Periodically check access controls to directories and buckets are correct
        - Moving unused data to LTS or external archival solutions
        - Managing backup plans

    - OpenStack Projects:

        - Periodically check group membership is correct
        - Periodically check unused resources are released

Regularly reviewing membership, permissions and access control, especially if conducted frequently, enhances security. It should occur at least once per year and during specific events. These events include:

- Security incidents
- A member of the group leaves the owner's group (e.g. a student leaves a lab group, or moves to a different project)
- A member of the group moves to a role with greater permissions or responsibilities within the owner's group (e.g. a staff member takes on a data stewardship role)

PIs are also responsible for ensuring that if their project(s) are accessible to students, they are aware that metadata about the project(s) may contain [FERPA-protected sensitive data](https://www.uab.edu/registrar/ferpa/faculty-staff).

- **All users**:

    - Regularly clearing `/scratch`
    - Adherence to [UAB IT policies](https://www.uab.edu/it/home/policies)
    - Request computational resources reasonably. Refer to our [compute resource estimation](../cheaha/job_efficiency.md/#estimating-compute-resources)
    - [Responsible Conduct of Research training](https://www.uab.edu/research/home/responsible-conduct-of-research)
    - [Annual account certification of Cheaha account](../account_management/cheaha_account/index.md/#account-requires-certification)

In addition, all Cheaha account users working with Protected Health Information (PHI) data are responsible to review [HIPAA policies](https://www.uab.edu/it/home/policies/compliance/hipaa) and
[HIPAA training](https://www.uab.edu/compliance/areas-of-focus/privacy/training).

## How do I create a Research Computing account?

- **Cheaha Account**: Creating a Cheaha account is currently a self-service process. Both UAB employees, students, and external collaborators can create a Cheaha account by visiting [creating a Cheaha account page](./cheaha_account/index.md).
- **GitLab Account**: If you are a UAB-affiliated researcher and have a BlazerID, you may create an account by visiting [GitLab registration steps for UAB Employees and Students](./gitlab_account.md/#uab-gitlab-registration). If you are a collaborator with a XIAS account, you will need to follow the procedure in [External Collaborators registration](./gitlab_account.md/#xias-external-collaborator-registration).
- **Cloud.rc Account**: To get your Cloud.rc account, please contact [Support](../help/support.md). For detail information on how to access it, please visit our [Cloud.rc](../uab_cloud/index.md) page.

## How do I login to Research Computing Services?

- **Cheaha**: To login to Cheaha:
    - UAB Employees and Students: use your BlazerID
    - External Collaborators: use your XIAS
    - For detail login information, please visit [accessing Cheaha](../cheaha/getting_started.md/#accessing-cheaha) page.  If accessing through Open OnDemand, our online portal, [Duo 2FA](https://www.uab.edu/it/home/security/2-factor) may be required.

- **GitLab**: To login  to the GitLab, the UAB Employees and Students require a BlazerID, while External Collaborators require XIAS email. For detail login information visit the [UAB Employees and Students](./gitlab_account.md/#uab-gitlab-registration) and [External Collaborators](./gitlab_account.md/#xias-external-collaborator-registration) pages respectively.

- **Cloud.rc**: To access the Cloud.rc, you must be on the campus network. For off-campus access, use the [UAB Campus VPN](https://www.uab.edu/it/home/tech-solutions/network/vpn), which requires [Duo 2FA](https://www.uab.edu/it/home/security/2-factor).
UAB employees and students can log in using their BlazerID, while External Collaborators use their XIAS email. For login details, visit our [Cloud.rc](../uab_cloud/index.md/#first-steps) page.

If you are unable to find what you need, please contact our team [here](../index.md#how-to-contact-us).