# Storage

Research Computing offers several data storage options to meet individual or shared needs of UAB researchers, depending on their requirement and use-cases. The types of storage available, procedures for requesting access, responsibilities, and usage guidelines are detailed in the following sections.

## What Type of Storage Do I Need?

There are multiple locations for data storage both on and off Cheaha each with a specific purpose. You can look at the table below to help determine the storage platform we provide that best matches your needed use-case. After reviewing the table, proceed to the [How to Choose the Right Storage for My Use Case](#how-to-choose-the-right-storage-for-my-use-case) section for additional guidance on selecting the most suitable storage for your needs. If you need additional assistance, please contact [Support](../help/support.md).

{{ read_csv('data_management/res/storage_overview.csv', keep_default_na=False) }}

### How to Choose the Right Storage for My Use Case?

When you have different types of data with varying storage needs, choosing the right storage is not an easy task. Below, we will walk you through common data storage needs and use cases.

- **I have lots of data that rarely or never changes**:
    - If your data is large and does not change frequently, [Long-Term Storage (LTS)](../data_management/lts/index.md) is your ideal option.
- **I need to do a lot of processing on the data**:
    - If your data is frequently accessed or modified, [Cheaha Storage (GPFS)](../data_management/cheaha_storage_gpfs/index.md) is a perfect option for your use case.
    - When you have finished working with the data, please consider putting it into [LTS](../data_management/lts/index.md). Please [Contact Us](../help/support.md#how-to-request-support) for more information.
- **I am just learning how to use Cheaha for very small personal projects**:
    - If you are new to Cheaha and working with small personal projects, you do not need a complex storage solution. [User Data](../data_management/cheaha_storage_gpfs/individual_directories.md#home-and-user-data-directories) is a simple and accessible option for beginners and smaller datasets.
    - If you find your project growing, or you need to collaborate with others at UAB, consider a shared allocation on [GPFS](../data_management/cheaha_storage_gpfs/index.md) and/or [LTS](../data_management/lts/index.md). Please refer to the instructions on [how to request a shared allocation](#how-do-i-request-shared-storage).
- **I need somewhere to store lots of temporary files while I do my processing**:
    - If you need a place to store large amounts of temporary data while processing data, [Network Scratch](../data_management/cheaha_storage_gpfs/network_scratch.md) is the best option.
- **I am working with high-throughput or I/O bound applications, like AI training or evaluation, or I have many very small files**:
    - For high-performance tasks, like AI training, [Local Scratch](../data_management/cheaha_storage_gpfs/local_scratch.md) provides fast and optimized data access for intensive I/O workloads..
- **I have a combination of needs and am unsure of how to proceed**:
    - If your use case spans across multiple types of storage needs, [Contact Us](../help/support.md#how-to-request-support) to discuss your requirements, and we wll help you find the best solution.

## What Individual Storage Solutions Are Available?

Every Cheaha user has personal directories found at `/home/$USER` (or `$HOME`) and `/data/user/$USER` (or `$USER_DATA`), which are created automatically during account registration. In addition, individual allocations on Long-Term Storage (LTS) are also available upon request. Please read more about [Long-Term Storage](./lts/index.md) and [User Data and Home Directories](./cheaha_storage_gpfs/individual_directories.md#home-and-user-data-directories).

### How Do I Request Individual Cheaha (`GPFS`) Storage?

An individual Cheaha (`GPFS`) storage is automatically created as part of the Cheaha account setup. No separate request is required.

### How Do I Request Individual Long-Term Storage?

To request individual Long-Term Storage, please first read and understand how [Long-Term Storage](./lts/index.md) differs from traditional file systems, like GPFS on Cheaha. Decide if it is suitable for your needs. Then please feel free to contact [Support](../help/support.md).

## What Shared Storage Solutions Are Available?

Shared Storage is available via two services. We have [Project Storage](./cheaha_storage_gpfs/project_directories.md) (located in `/data/project` or Cheaha) and [Long-Term Storage (LTS)](./lts/index.md). The two offerings are suited to different sets of use-cases and are available upon request, so please read on to determine which may be most suitable.

[Project Storage](./cheaha_storage_gpfs/project_directories.md) is best-suited for changing or dynamic data. Specifically::

- Data needing/undergoing analysis
- Exploratory data
- Temporary data needed longer than 30 days

In contrast, [Long-Term Storage](./lts/index.md) is best-suited for unchanging or static data. Specifically:

- Instrument-acquired data
- Completed analyses
- Hosting data for others to copy
- Hosting data for the public internet
- "Pick-up" and "drop-off" locations for data as part of a workflow

Shared Storage is available for labs headed by a PI _and_ for Core facilities headed by a director.

Shared Storage is allocated on a per-organization basis, not on a per-person basis. If an individual researcher manages both a lab and a Core, they may request independent storage allocations for each organization. Each organization may request both Project Storage and Long-Term Storage.

### Which Platform Do I Need an Allocation For?

You can request one or both storage platforms, depending on your project’s needs.

- Request [Cheaha Storage (GPFS)](./cheaha_storage_gpfs/index.md) if you need fast, cluster-integrated storage to support active analysis or collaboration on Cheaha.
- Request [Long-Term Storage (LTS)](./lts/index.md) if you need to store, or share data that does not change frequently.

You can benefit from requesting and using both platforms: keeping active and changing data in GPFS during analysis, then moving completed or less active data into LTS for long-term preservation, and bringing it back from LTS to GPFS when further work is needed.

### How Do I Request Shared Storage?

To request shared Project Storage or Long-Term Storage, please contact [Support](../help/support.md). To ensure prompt allocation of Shared Storage, please follow the guidelines below:

- Requests must be made to <support@listserv.uab.edu> or via the [AskIT HelpDesk](https://www.uab.edu/it/home/).
- Requests must come from one of the proposed owners (a Lab PI, a Research Core director, or both).
- The role of Lab PI entitles a person to a project space for that lab.
- The role of Research Core director entitles a person to a project space for that core. If one person has both roles, they may have two shared Storage spaces, one for each role.
- All proposed owners must have created their [Research Computing accounts](../account/rcs/create.md) at the time of the request.

Please provide the following information. Missing information can delay allocation of Shared Storage as we either look up the information, or ask followup questions.

- **Responsible Party/Owner:** The BlazerID of the person claiming responsibility for what happens and what is stored in the space. Typically this would be a Principal Investigator (PI) or a Core Director.
    - Multiple responsible parties are allowed.
    - We need one person declared as "primary" owner. This person will be the literal owner (in the Linux sense) for Project Storage.
- **Members:** A list of BlazerIDs of people to give access to the space. (Note: this only applies to Project Storage. LTS access controls are managed differently.)
- **Type of Organization:** Is the Shared Storage request for a lab, core, campus administrative group, or something else?
- **Name of Organization:** The _specific_ name of the organization the Shared Storage request is for.
- **Parent Organization:** The name of the parent organization for your organization. Please be as detailed as possible.
- **Purpose of Shared Storage:** The research purpose for the storage, how do you intend to use it? Please feel free to be as detailed as you like, but please limit to a few sentences at most.
- **Internal UAB Collaborator Organizations:** The name(s) of any other UAB organizations participating in the Shared Storage.
- **External Collaborator Organizations:** The name(s) of any external organizations participating in the Shared Storage.
- **Regulatory Requirements:** List any regulatory requirements or agencies affecting data to be stored in the space. Possibilities include, but are not limited to: IRB, EHR, HIPAA, PHI, FERPA.
- **Name of Shared Storage:** Please give us a generic name specific to your project/Lab.

    - For Labs, we recommend using the format `<BlazerID>_lab`, where `<BlazerID>` is the BlazerID of the Principal Investigator (PI). Alternatively, the PI may choose to use their first or last name instead of the BlazerID.
    - For Cores, we recommend using a shortened version of the Core name. For example: `core_facility_space`
    - For Project Storage, the name you choose will be used in the path `/data/project/<BlazerID>_lab` on Cheaha. Also, this name,`<BlazerID>_lab`, will be given to your shared LTS allocation.

    <!-- markdownlint-disable MD046 -->
    !!! Tip

        - Keep the name short, memorable, and relevant.
        - Use `underscores (_)` or `hyphen (-)` to separate words.
        - To serve future projects, consider names that are generic.
    <!-- markdownlint-disable MD046 -->

If some members have not created their accounts at the time of the request, we will proceed with allocating the Shared Storage. Additional members may be added at a later time in a new service request.

### How Do I Make Changes to Shared Storage Membership?

To request changes in Shared Storage membership, please contact [Support](../help/support.md). Please take note of the following guidelines to ensure changes can be made promptly.

- We must have written approval from an owner to make membership changes.
- The exact name of the Shared Storage. If it is Project Storage, the path to the storage location, i.e., `/data/project/...`.
- Please give BlazerIDs of members to add or remove.

### How Can I Get a Larger `/data/project/` (GPFS) Allocation?

At this time, due to constraints on total GPFS storage, we are not able to increase `/data/project/` allocations. Please consider batching your analyses by leveraging a combination of [LTS](./lts/index.md) to store raw and/or input data, and [Network Scratch](./cheaha_storage_gpfs/network_scratch.md) for temporary storage of up to 100 TB of data for use during analysis.

If you wish to have further discussion of options for expanding your GPFS allocation and other workarounds tailored to your workflow, please [Contact Support](../help/support.md). Please also note that project storage is not just for a single project only, it is meant as a storage for multiple projects.

### How Can I Get a Larger LTS Lab Allocation?

At this time, due to constraints on total [LTS](./lts/index.md) storage, increasing an LTS allocation requires purchasing additional hardware. Below are some facts about purchasing additional storage nodes.

- Allocation increases occur by purchasing whole storage nodes.
- Each node has 133 TB of usable storage.
- Nodes are purchased with researcher funds at vendor cost.
- No markups are added to the cost of nodes.
- Purchased nodes are racked with existing hardware in our data centers.
- Purchased nodes are maintained by Research Computing with the same level of service as other hardware.
- Purchased nodes are supported for 5 years from date of purchase, the industry standard for commercial datacenter hardware.
- Once an order is placed with the vendor, we can provide additional storage immediately _if_ free storage is available, regardless of lead-time.

If you have additional questions _or_ wish to discuss further, please [Contact Support](../help/support.md).

### If I Can't Get a Larger Allocation, What Alternatives Are There?

One alternative we recommend is breaking your dataset into batches. A generic, template workflow might be something like below.

- Copy a batch of data from LTS, or an internet source, to [Network Scratch](./cheaha_storage_gpfs/network_scratch.md).
- Perform analyses on copied data in network scratch.
- Store intermediate or final results in `/data/project/` or LTS.
- Delete copied data from network scratch.
- Start again with the next batch.

When all batches have been processed, begin processing or aggregating the resulting data.

If you wish to discuss other alternatives tailored to your workflow, please [Contact Support](../help/support.md).

### How Can I Effectively Manage My Data?

Keep files well-organized and clearly named, back up regularly, and archive or delete unused data.

### How Is My Data Protected Against Disk Failure?

Please see the "Redundancy" row in the [storage table](#what-type-of-storage-do-i-need) to learn how different storage platforms protect data against disk failure.

### What Are My Responsibilities for Data Management?

Periodically review permissions, clean up unused data, and follow institutional Storage and security policies. Please review our [Research Data Responsibilities](./research_data_responsibilities.md#research-data-responsibilities) page for details.

## Data Responsibilities and Procedures

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
- Unusable backups.
    - Examples: backup software bug; media destroyed; natural disaster at offsite location.

If you need backup services, please [Contact Us](../help/support.md#how-to-request-support), and we can discuss options based on your specific use case.

### HIPAA Compliance

Cheaha is HIPAA compliant and can accept Protected Health Information (PHI) data. Currently, [long-term storage](lts/index.md) is NOT HIPAA compliant but will be in the future.

For UAB policies surrounding PHI data, please see the following URLs.

- [Data Classification](https://www.uab.edu/it/home/policies/data-classification/classification-overview)
- [Data Protection and Security Policy](https://secure4.compliancebridge.com/uab/portal/getdoc.php?file=302)
- [Data Access Policy](https://secure4.compliancebridge.com/uab/portal/getdoc.php?file=301)
- [HIPAA Data Policy](https://www.uab.edu/it/home/policies/compliance/hipaa)

<!-- markdownlint-disable MD046 -->
!!! important

    It is the responsibility of researchers to make sure PHI is accessible _only_ to people on the relevant IRB, with a demonstrated need to know. If PHI is stored in a project directory where some researchers are not on the IRB, their access to those files should be restricted using Access Control Lists (ACLs). Access control should be planned in advance of moving PHI data to Cheaha. If you need assistance setting up ACLs properly, please contact [Support](../help/support.md).
<!-- markdownlint-enable MD046 -->

Managing PHI data can be challenging. There are experts on Campus who can provide assistance. Please contact [Support](../help/support.md) if you intend to use Research Computing services in combination with PHI and PHI-derived data.
