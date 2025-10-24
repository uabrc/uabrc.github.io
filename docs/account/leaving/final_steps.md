# Leaving UAB — Final Steps

{% from "_macro/support.md.j2" import contact_support_link %}

All UAB students, staff, and faculty should make arrangements to properly manage their data as they prepare to leave UAB.

## What Happens to Data in My Individual Storage Allocations?

Data in your individual storage allocations, on all storage platforms, will be retained for the grace period. We recommend making a plan for your data.

- Download any personal, non-UAB-owned data you want to keep.
- Make arrangements with your research faculty supervisor to transfer any UAB-owned research data to appropriate shared storage allocations. If you have multiple faculty supervisors, please work with each of them.

## What Are My Responsibilities for Lab Shared Allocations?

If you are responsible for lab shared allocations on Research Computing storage platforms, you have certain responsibilities for the data within them. Transferring UAB-owned data requires the involvement of the [Office of Research](https://www.uab.edu/research/home/about/contact-us), specifically the [Office of Sponsored Programs (OSP)](https://www.uab.edu/research/home/osp-about/contact).

For each dataset or project, which option is ideal depends on the state of the project.

- Transfer responsibility of the data to a successor (retiring)?

    1. Make the appropriate arrangements with relevant administrative units (e.g., Office of Research and OSP).
    1. [Globus](../../data_management/transfer/globus.md) may be used to efficiently and robustly transfer the data from one directory on Cheaha to another. Please {{ contact_support_link() }} for more details.

- Transfer the data to a new instutition (moving)?

    1. Contact the Office of Research to create a "Data Use Agreement" with your new institution. Read more on the [OSP Site](https://www.uab.edu/research/home/osp-federal-contracts/fc-other/data-use-agreements).
    1. {{ contact_support_link() }} and your new institution's Research Computing equivalent to determine how to transfer data efficiently.

- Comply with funding agency data retention regulations (retiring)?

    - Find a UAB-affiliated successor to manage the data for you in your absence.
    - _OR_ Find an archival service suitable for long term data retention.

- Something else? Please {{ contact_support_link() }}.

## What Are My Responsibilities for Core Shared Allocations?

Cores should not assume responsibility for any of the research data they produce or acquire.

If the Core will continue operating, then it is assumed there will be a successor. Take whatever necessary administrative steps to transfer control and responsibility for Core operations. Things that may need to be transfered:

- [GPFS (Cheaha) shared allocation](../../data_management/cheaha_storage_gpfs/project_directories.md).
- [LTS shared allocation](../../data_management/lts/index.md).
- [OpenStack Shared Projects](../../uab_cloud/sharing_cloud_environment.md).
- Service account, shared mailboxes, and other shared resources not managed by Research Computing, but which may have an impact on Core operations relating to Research Data acquisition and transfer, such as [Globus](../../data_management/transfer/globus.md).

If the Core will cease operating, please {{ contact_support_link() }} to make arrangements to ensure final disposition of all research data.

{% include "account/xias/_template/xias_help_section.md.j2" %}
