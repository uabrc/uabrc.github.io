---
toc_depth: 3
---

# LTS Identity and Access Management

LTS Identity and Access Management (IAM) is a framework for managing identities, roles, and permissions in Long-Term Storage (LTS) solutions, ensuring secure and efficient access to storage spaces like [buckets](./index.md#terminology) or [objects](./index.md#terminology). Understanding access rights and permissions for LTS spaces is essential for effective data management and security. This section aims to clarify common misconceptions regarding ownership, steward roles, access control, and how bucket policies help manage permissions in LTS spaces.

## Terminology

- **Allocation**: An allocation represents a designated storage space with a unique name.
- **Keys**: Keys are the credentials that grant access to an allocation. There are two types of keys:
    - Access Key: The public identifier used to access the allocation, similar to a username.
    - Secret Key: The private password-like credential that must be kept confidential.
- **Stewards**: Stewards are individuals responsible for managing an allocation. Stewards need a full access key pair to perform tasks like creating, deleting, and maintaining buckets. Each steward must maintain separate key pairs for their allocations and any Lab/Core allocations they manage.
- **Owner**: owners responsible for overseeing the management of allocated storage spaces, ensuring compliance with data management policies, and designating appropriate stewards, if needed, to assist in the management of allocation. Owners can include:
    - **Lab PIs**: Manage allocated storage spaces for their respective Labs.
    - **Core Director**: Manage allocated storage spaces for Core facilities.
- **Bucket Policy**: A bucket policy is a [JSON formatted file](https://docs.fileformat.com/web/json/) that you can use to grant access permissions to your LTS bucket and the objects in it. Please refer to [sharing buckets and bucket policy structure](../lts/iam_and_policies.md#sharing-buckets) for more details.
- **Identity and Access Management (IAM)**: IAM is a framework of policies, processes, and technologies used to manage digital identities and control access to resources.

## Shared LTS Allocations

Shared LTS allocations are storage spaces designed for collaborative use by groups and are available to Lab PIs and Core Directors. If a PI is also a Core Director, they are eligible for independent storage allocations for each organization: one for the Lab and one for the Core. Each shared LTS allocation provides 75 TB of storage. These allocations can be named according to the preference of the Lab PI or Core Director. For recommended naming guidelines, refer to our [Naming Shared Storage](../../data_management/index.md#how-do-i-request-shared-storage) documentation.

{{ read_csv('data_management/res/shared_allocation_functional_roles.csv', keep_default_na=False) }}

### How do I grant other users access to my shared LTS Allocation?

By default, only the allocated owner, and stewards if designated, can manage and access a shared LTS allocation using their specific key pairs. Keys from other allocations, such as those for individual LTS allocations, will not grant access to shared Lab or Core allocations. If you manage both Lab and Core allocations, ensure you use the corresponding keys, as keys for one cannot access the other.

To grant other users access to your shared allocation:

- Owners and steward can set permissions using a [bucket policy](../lts/iam_and_policies.md#sharing-buckets).
- Access can be granted to any user with individual LTS allocations.

### How do I assign a steward?

Owners can assign stewards either when requesting LTS account creation or at a later time by sending a request via [Contact Us](../../index.md#how-to-contact-us). The request should include the steward's BlazerID and specify the LTS allocation they should manage. Once assigned, stewards will have the same management permissions as the owner, except for the ability to assign other stewards.

### Who can have what role?

- Owners must be Core Directors or Lab PIs.
- Stewards may be any UAB affiliated person designated by an owner.
- Members may be anyone with an individual LTS allocation.

### How do I gain access to my role?

- Owners and stewards have key sets for the allocation(s) they manage. These key sets are distinct, one per person per allocation, and separate from the key set they use for their individual allocations.
- Members are granted access by [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html) for each bucket they need access to. For more details, please refer to our documentation on [sharing buckets and bucket policy structure](../lts/iam_and_policies.md#sharing-buckets).

## Individual LTS Allocations

Individual LTS allocations are intended for personal or individual use and are available to all UAB affiliated individuals. These allocations are tied to the individual’s email and provide 5 TB of storage.

{{ read_csv('data_management/res/individual_allocation_functional_roles.csv', keep_default_na=False) }}

### How do I grant other users access to my Individual LTS Allocation?

By default, only the allocated user can manage and access their individual LTS allocation using only their designated key pairs. Keys for other allocations, such as those assigned to you as a steward or for shared allocations, do not provide access to your individual LTS allocation.

If you want to grant other users access to your allocation:

- You can set permissions using a [bucket policy](../lts/iam_and_policies.md#sharing-buckets).
- Any user with an individual LTS allocation can be granted access.

## Key Handling and Ownership

- Keys should be treated as sensitive information. Only one individual should know a key pair.
- Each key pair corresponds to a specific allocation, ensuring that access rights are clearly defined.
- Mismanagement of keys can lead to unauthorized access and potential data loss.

Everyone is responsible for managing their key pairs and ensuring they use the correct pair for each allocation and securely store all secret keys. Allocation keys serve as access controls, with the owner retaining the key pairs

## Lost LTS Key Reset

If you have lost your LTS keys, you can request a reset by creating a support ticket via [Contact Us](../../index.md#how-to-contact-us). Please include your BlazerID and specify the LTS account (individual and/or shared) for which you need the key reset, so we can process your request accordingly. Then you will receive an email with a link to a UAB Box text file containing the corresponding key pairs (access key and secret key).

If you, as a Lab/Core PI, do not wish to manage the LTS space yourself, we recommend assigning data Steward permissions to someone who is both trustworthy and has knowledge of, or willingness to learn, [JSON](https://docs.fileformat.com/web/json/#google_vignette) and parts of the [Amazon AWS S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Type_API_Reference.html). If you need help or have concerns about making this decision, please [Contact Us](../../index.md#how-to-contact-us).

## Sharing Buckets

A major use for LTS is storage of data that should be accessible to multiple users from a Lab or research group. By default, buckets are only visible and accessible to the owner of the bucket, and no mechanism exists to search for buckets other users have created.

Instead, sharing buckets must be done through the command line using [bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html). A bucket policy is a JSON formatted file that assigns user read and write permissions to the bucket and to objects within the bucket. If you have not worked with JSON files before, a brief explanation can be found [here](https://docs.fileformat.com/web/json/). It's important to note that the bucket owner will always retain the ability to perform all actions on a bucket and its contents and so do not need to be explicitly granted permissions.

<!-- markdownlint-disable MD046 -->
!!! important

    Your username for LTS could potentially be `<BlazerID>` or `<BlazerID>@uab.edu` depending on when your account was created. It is very important when crafting these policies that the correct username is specified, and these two are not interchangeable. For users with XIAS accounts, your username should be the email address you signed up for the XIAS account with. The usernames are case-sensitive. If you do not remember what your username is, see the email you received with your access key and secret key information or submit a support ticket to support@listserv.uab.edu.
<!-- markdownlint-enable MD046 -->

### Policy Structure

Policies files are essentially built as a series of statements expressly allowing or deny access to functions that interact with objects in S3. A skeleton policy file would look like this:

``` json
{
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "description",
        "Effect": "Allow",
        "Principal": {"AWS": []},
        "Action": [],
        "Resource": []
    }]
}
```

Each statement is made up of a few fields:

1. Sid: a short decription of what the statement is for (i.e. "bucket-access")
1. Effect: "Allow" or "Deny" permissions based on how you want to alter permissions
1. Principal: Essentially a list of users to change permissions for. Have to formatted like `arn:aws:iam:::user/<lts_username>`.
1. Action: A list of commands to allow or deny permission for, depending on the Effect value.
1. Resource: The name of the bucket or objects to apply permissions to. Must be formatted like `arn:aws:s3:::<bucket[/path/objects]>`.

It is currently suggested to have at least two statements, one statement allowing access to the bucket itself, and another statement dictating permissions for objects in the bucket.

For example, if you wanted to give users `bob` and `jane@uab.edu` the ability to list objects in your bucket `bucket1`, the statement would be:

``` json
{
    "Sid": "list-bucket",
    "Effect": "Allow",
    "Principal": {
        "AWS": [
            "arn:aws:iam:::user/bob",
            "arn:aws:iam:::user/jane@uab.edu"
            ]
        },
    "Action": [
        "s3:ListBucket"
    ],
    "Resource": [
        "arn:aws:s3:::bucket1"
    ]
}
```

Critically, this does not allow the given users the ability to read, download, edit, or delete any objects in the bucket. They will be able to list the objects, see the names, sizes, and directory structure but will not be able to interact with the objects. These permissions should be enumerated in a separate statement like:

``` json
{
    "Sid": "read-only",
    "Effect": "Allow",
    "Principal": {
        "AWS": [
            "arn:aws:iam:::user/bob",
            "arn:aws:iam:::user/jane@uab.edu"
            ]
        },
    "Action": [
        "s3:GetObject"
    ],
    "Resource": [
        "arn:aws:s3:::bucket1/*"
    ]
}
```

This permission set allows `bob` and `jane@uab.edu` to download files but not to move, overwrite, delete, or otherwise interact with them. Notice that the Resource value has changed from just `bucket1` to `bucket1/*`. We can set this Resource value to different paths and objects to limit the permissions granted. For example:

1. `bucket1/*`: Apply permissions to all objects in the entire bucket
1. `bucket1/test_folder/*`: Apply permissions to all objects in folder `test_folder`
1. `bucket1/test_folder/*jpg`: Apply read permissions to only JPGs within `test_folder`.

For the last two examples, `bob` and `jane@uab.edu` will not have permission to download any files outside of the `test_folder` folder. All permissions are implicitly denied unless explicitly given in the policy statements.

### Common Actions

Being able to download a file is only one possible action you may want to give permission for. Uploading files as well as altering the policy of the bucket may also be useful to give permissions for. Here is a short list of common actions you may want to give permissions for:

1. `s3:ListBucket`: access to see but not interact with objects
1. `s3:GetObject`: download objects
1. `s3:PutObject`: upload objects
1. `s3:DeleteObject`: remove objects
1. `s3:GetBucketPolicy`: view the current bucket policy
1. `s3:PutBucketPolicy`: change the current bucket policy

A full list of Actions for UAB LTS can be seen on the [Ceph docs](https://docs.ceph.com/en/quincy/radosgw/bucketpolicy/#limitations).

### Example Policies

#### Read-Only for All Files

This will give permissions to `bob` and `jane@uab.edu` for bucket `bucket1`. The permissions will include bucket access (the `list-bucket` statement) as well as read-only permissions for all objects in the bucket (the `read-only` statement). Specifically, they will be able to copy the files from the bucket to another bucket or a local file system.

``` json
    {
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "list-bucket",
        "Effect": "Allow",
        "Principal": {
            "AWS": [
                "arn:aws:iam:::user/bob",
                "arn:aws:iam:::user/jane@uab.edu"
            ]
        },
        "Action": [
            "s3:ListBucket"
        ],
        "Resource": [
            "arn:aws:s3:::bucket1"
        ]
    },
    {
        "Sid": "read-only",
        "Effect": "Allow",
        "Principal": {
            "AWS": [
                "arn:aws:iam:::user/bob",
                "arn:aws:iam:::user/jane@uab.edu"
            ]
        },
        "Action": [
            "s3:GetObject"
        ],
        "Resource": [
            "arn:aws:s3:::bucket1/*"
        ]
    }]
    }
```

#### Read-Write Permissions

This will give read, write, and delete permissions to `bob` and `jane@uab.edu` so they are able to sync directories between a local source folder and the S3 destination. This can be dangerous because of the delete permissions so care should be given in handing out that permission. `s3:DeleteObject` can be set into another statement field and limited to very select users while giving upload permission to many users.

``` json
{
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "list-bucket",
        "Effect": "Allow",
        "Principal": {
            "AWS": [
                "arn:aws:iam:::user/bob",
                "arn:aws:iam:::user/jane@uab.edu"
            ]
        },
        "Action": [
            "s3:ListBucket"
        ],
        "Resource": [
            "arn:aws:s3:::bucket1"
        ]
    },
    {
        "Sid": "read-write",
        "Effect": "Allow",
        "Principal": {
            "AWS": [
                "arn:aws:iam:::user/bob",
                "arn:aws:iam:::user/jane@uab.edu"
            ]
        },
        "Action": [
            "s3:GetObject",
            "s3:PutObject",
            "s3:DeleteObject"
        ],
        "Resource": [
            "arn:aws:s3:::bucket1/*"
        ]
    }]
}
```

#### Tiered Permissions

In some instances, the bucket owner (i.e. ideally the PI for the Lab if this is a shared Lab space) will want to allow certain users to have permissions to alter the policies for new or departing Lab members. This example will give standard read-write permissions to both our Lab members, but only policy altering permissions to `jane@uab.edu`.

``` json
{
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "list-bucket",
        "Effect": "Allow",
        "Principal": {
            "AWS": [
                "arn:aws:iam:::user/bob",
                "arn:aws:iam:::user/jane@uab.edu"
            ]
        },
        "Action": [
            "s3:ListBucket"
        ],
        "Resource": [
            "arn:aws:s3:::bucket1"
        ]
    },
    {
        "Sid": "change-policy",
        "Effect": "Allow",
        "Principal": {
            "AWS": [
                "arn:aws:iam:::user/jane@uab.edu"
            ]
        },
        "Action": [
            "s3:GetBucketPolicy",
            "s3:PutBucketPolicy"
        ],
        "Resource": [
            "arn:aws:s3:::bucket1"
        ]
    },
    {
        "Sid": "read-write",
        "Effect": "Allow",
        "Principal": {
            "AWS": [
                "arn:aws:iam:::user/bob",
                "arn:aws:iam:::user/jane@uab.edu"
            ]
        },
        "Action": [
            "s3:GetObject",
            "s3:PutObject",
            "s3:DeleteObject"
        ],
        "Resource": [
         "arn:aws:s3:::bucket1/*"
        ]
    }]
}
```

### Comments in S3 IAM Policies

IAM policies for `S3`, used by LTS for object-level access control within buckets, are written in `JSON` format. Since `JSON` does not support comments natively, `AWS` does not provide a dedicated comment field in their IAM policy schema.

The optional `SID` field in IAM policies, though intended for uniquely identifying statements, can also be used as an ad-hoc comment. In the example below, the `SID` field provides a description of the statement, serving as a comment.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "This statement grants read access to all objects in bucket1",
      "Effect": "Allow",
      "Principal": {
        "AWS":[
            "arn:aws:iam:::user/bob",
            "arn:aws:iam:::user/jane@uab.edu"
        ]
      },
      "Action": [
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::bucket1",
        "arn:aws:s3:::bucket1/*"
      ]
    }
  ]
}
```

### Specifying "all actions" in IAM Policies

To allow or deny all actions on a specific resource, such as an `S3` bucket or object, use the following `Action` block as part of a `Statement` object to specify that all actions are affected by the statement:

```Json
    "Action": [
    "s3:*"
    ],
```

Here is an example IAM policy that grants all `S3` actions on bucket1 and all its objects:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "This statement grants access to all S3 actions in bucket1",
      "Effect": "Allow",
      "Principal": {
        "AWS":[
             "arn:aws:iam:::user/bob",
             "arn:aws:iam:::user/jane@uab.edu"
        ]
      },
      "Action": [
        "s3:*"
      ],
      "Resource": [
        "arn:aws:s3:::bucket1",
        "arn:aws:s3:::bucket1/*"
      ]
    }
  ]
}
```

### Applying a Policy

Policies can be applied to a bucket either by the owner or by a user who has been given the `s3:PutBucketPolicy` permission. Use s3cmd to apply policies.

<!-- markdownlint-disable MD046 -->
!!! note

    As of now, rclone has not implemented a way to alter policies, and AWS CLI does not apply them to our system correctly. If you have been using rclone or AWS CLI, you will need to configure s3cmd for policy management instead
<!-- markdownlint-enable MD046 -->

Applying a policy is fairly straightforward for both tools. First, you should save the policy as a JSON file. The, you can interact with the policy using these commands:

``` bash
# s3cmd set policy
s3cmd setpolicy <policy_file> s3://<bucket>

# s3cmd view policy
s3cmd info s3://<bucket>

# s3cmd remove policy
s3cmd delpolicy s3://<bucket>
```

### Policy Suggestions

<!-- markdownlint-disable MD046 -->
!!! important

    Policies can be very complicated depending on how many people need access to the bucket and how you want to tier permissions (i.e. which people are read-only, read-write, admin-esq priveleges, etc.). If you need help structuring your policy files please [visit us during office hours](../../help/support.md#office-hours) and we will be happy to help structure your policy file to your needs.
<!-- markdownlint-enable MD046 -->

#### Admin-esq Priveleges

It is suggested to keep the number of people who have permission to delete data and alter policies to a minimum. Inexperience with policies can result in permissions being granted to incorrect users which can potentially lead to irrecoverable consequences. Syncing data without purposeful thought can result in the undesired loss of data.

#### Bucket Ownership

For Labs using LTS to store data from their Cheaha Project Storage directory, it is highly advised that the PI for the Lab creates and owns the bucket and then gives policy changing permissions to another researcher for day-to-day maintenance if desired. For instance, if a Lab manager creates the bucket and then leaves the university without giving policy permissions to other users, the Lab will not be able to change the policies for those data.

#### Sharing Multiple Datasets with Different Groups

Some groups on campus may distribute datasets to other research groups using LTS. If you are distributing data to multiple groups, and those groups should not have access to each other's data, it is highly advised to store those datasets in separate buckets as opposed to separate directories in a single bucket.

An idiosyncrasy of buckets involves the fact that all objects are stored in the top level of the bucket, and once permissions are given to someone to see the bucket, they will be able to see all objects within the bucket without restrictions even if they are not given download permissions for some objects. If any identifying or priveleged information is given in file names on LTS, it could constitute an IRB violation. Additionally, managing permissions for groups to access data only from specific folders makes the policy file much more complicated and prone to errors. When sharing multiple datasets with multiple different groups, it's advised to keep these data in separate buckets and have individual policy files for each bucket to make policy management simpler and less prone to error.
