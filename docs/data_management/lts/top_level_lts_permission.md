# Top-level LTS Permissions

Understanding top-level access rights for Long-Term Storage (LTS) spaces is essential for effective data management and security. This section aims to clarify common misconceptions regarding ownership and access rights in LTS space.

## Terminology

- **Allocation**: An allocation represents a designated storage space with a unique name.
- **Keys**: Keys are the credentials that grant access to an allocation. There are two types of keys:
    - Access Key: The public identifier used to access the allocation, similar to a username.
    - Secret Key: The private password-like credential that must be kept confidential.
- **Stewards**: Stewards are individuals responsible for managing an allocation. Stewards need a full access key pair to perform tasks like creating, deleting, and maintaining buckets. Each steward must maintain separate key pairs for their allocations and any lab/Core allocations they manage.
- **Owner**: owners responsible for overseeing the management of allocated storage spaces, ensuring compliance with data management policies, and designating appropriate stewards, if needed, to assist in the management of allocation. Owners can include:
    - **Lab PIs**: Manage allocated storage spaces for their respective labs.
    - **Core Director**: Manage allocated storage spaces for Core facilities.
- **Bucket Policy**: A bucket policy is a [JSON formatted file](https://docs.fileformat.com/web/json/) that you can use to grant access permissions to your LTS bucket and the objects in it. Please refer to [sharing buckets and bucket policy structure](../lts/policies.md#sharing-buckets) for more details.

## Shared LTS Allocations

Shared LTS allocations are storage spaces designed for collaborative use by groups and are available to Lab PIs and Core Directors. If a PI is also a Core Director, they are eligible for independent storage allocations for each organization: one for the Lab and one for the Core. The shared LTS allocation provides 75 TB of storage. These allocations can be named according to the preference of the PI or Core Director. For recommended naming guidelines, refer to our [Naming Shared Storage](../../data_management/storage.md#how-do-i-request-shared-storage) documentation.

{{ read_csv('data_management/res/shared_allocation_functional_roles.csv', keep_default_na=False) }}

### How do I grant other users access to my shared LTS Allocation?

By default, only the allocated owner, and stewards if designated, can manage and access a shared LTS allocation using their specific key pairs. Keys from other allocations, such as those for individual LTS allocations, will not grant access to shared lab or core allocations. If you manage both lab and core allocations, ensure you use the corresponding keys, as keys for one cannot access the other.

To grant other users access to your shared allocation:

- The Owners, or a steward if one has been designated, can set permissions using a [bucket policy](../lts/policies.md#sharing-buckets).
- Access can be granted to any user with system access, including those with individual LTS allocations and an active Cheaha account.

### How do I assign a steward?

Owners can assign stewards either when requesting LTS account creation or at a later time by sending a request via [Contact Us](../../index.md#how-to-contact-us). The request should include the steward's BlazerID and specify the LTS allocation they should manage. Once assigned, stewards will have the same management permissions as the owner, except for the ability to assign other stewards.

### Who can have what role?

- Owners must be Core Directors or Lab PIs.
- Stewards may be any UAB affiliated person designated by an owner.
- Members may be anyone with access to the system, i.e., someone who has created an individual LTS allocation and has a Cheaha account.

### How do I gain access to my role?

- Owners and stewards have key sets for the allocation(s) they manage. These key sets are distinct, one per person per allocation, and separate from the key set they use for their individual allocations.
- Members are granted access by [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html) for each bucket they need access to. For more details, please refer to our documentation on [sharing buckets and bucket policy structure](../lts/policies.md#sharing-buckets).

## Individual LTS Allocations

Individual LTS allocations are intended for personal or individual use and are available to all UAB affiliated individuals. These allocations are tied to the individual’s email and provide 5 TB of storage.

{{ read_csv('data_management/res/individual_allocation_functional_roles.csv', keep_default_na=False) }}

### How do I grant other users access to my Individual LTS Allocation?

By default, only the allocated user can manage and access their individual LTS allocation using only their designated key pairs. Keys for other allocations, such as those assigned to you as a steward or for shared allocations, do not provide access to your individual LTS allocation.

If you want to grant other users access to your allocation:

- You can set permissions using a [bucket policy](../lts/policies.md#sharing-buckets).
- Any user with system access, including those with their own individual LTS allocation and an active Cheaha account, can be granted access.

## Key Handling and Ownership

- Keys should be treated as sensitive information. Only one individual should know a key pair.
- Each key pair corresponds to a specific allocation, ensuring that access rights are clearly defined.
- Mismanagement of keys can lead to unauthorized access and potential data loss.

Everyone is responsible for managing their key pairs and ensuring they use the correct pair for each allocation and securely store all secret keys. Allocation keys serve as access controls, with the owner retaining the key pairs

## Lost LTS Key Reset

If you have lost your LTS keys, you can request a reset by creating a support ticket via [Contact Us](../../index.md#how-to-contact-us). Please include your BlazerID and specify the LTS account (individual and/or shared) for which you need the key reset, so we can process your request accordingly. Then you will receive an email with a link to a UAB Box text file containing the corresponding key pairs (access key and secret key).

If you, as a lab/core PI, do not wish to manage the LTS space yourself, we recommend assigning data Steward permissions to someone who is both trustworthy and has knowledge of, or willingness to learn, [JSON](https://docs.fileformat.com/web/json/#google_vignette) and parts of the [Amazon AWS S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Type_API_Reference.html). If you need help or have concerns about making this decision, please [Contact Us](../../index.md#how-to-contact-us).
