# LTS FAQ

## What Are Valid Bucket Names in LTS?

Bucket names must be comprised only of lowercase letters, numbers, and hyphens. No capital letters or underscores are allowed. Trying to create a bucket with the disallowed characters will return an error.

## Can I Share My Allocation Access Keys With Other People?

You should never share access keys with anyone. These should be treated similarly to your BlazerID and password. Sharing keys creates a point of vulnerability and if they fall into a nefarious actor's hands, all buckets that allocation owns and the data in them can be deleted.

In some cases, you may not be actively managing data in a bucket even though you own the allocation which owns a shared bucket. Instead of sharing keys with a data steward, instead that steward should be given admin-esque permissions on the required bucket via a policy file.

## How Should I Organize My LTS Shared Allocation?

This is ultimately up to the bucket owner, but there are a couple of single-bucket solutions depending on your specific use-case for LTS:

1. Semi-synced copy of everything in the project allocation.
    - **General permissions:** Data stewards and the bucket owner would have permission to delete any files. All other users would be able to upload and download files only. All users would be able to see all files uploaded by all other users to that bucket./
    - **Purpose:** This fulfills more of a pure backup role compared to option 2. While all users can upload files
    - **Benefits:** The policy file for these permissions is much simpler to create and manage. Limits the number of people who can remove files that might be needed down the line.
    - **Drawbacks:** Needing to ask a steward or the bucket owner to delete individual files introduces friction to data management.
    - [Example Policy File](res/example-synced-project-policy.json){: download="example-synced-project-policy.json" }
1. Active and collaborative external storage. All users would have a specific prefix/folder they have complete control where they can add or remove data at will.
    - **General permissions:** Data stewards and the bucket owner would have permission to delete any files. Regular users would only be able to upload to and delete files from their owned prefix/folder. All users would be able to see and download any files from any other user.
    - **Purpose:** This satisfies the need for expanded storage accessible from Cheaha (via the terminal or Globus). All users have their own allocation they can use as they see fit within the bucket for extra storage while still being able to access, but not alter, files from other users in cases they need to be shared. Part of the bucket, or a separate bucket entirely, can also be used as a backup for old or current datasets where users only have read permissions.
    - **Benefits:** How the bucket can be used is much more malleable and up to the individual users. Empowers them to add and remove data from their own prefix/folder without oversight from stewards or the bucket owner.
    - **Drawbacks:** The policy file is more difficult to craft and manage when researchers needed to be added or removed from the bucket. Allowing users to delete their uploaded data at their discretion may conflict with the owner's view of those data.
    - [Example Policy File](res/example-active-external-storage-policy.json){: download="example-active-external-storage-policy.json" }

While these are two simple solutions, a combination of both can be implemented with some clever crafting of the policy file. As well, you could take advantage of both solutions with multiple buckets. Keep in mind that data in all buckets contribute towards the total storage allocation equally. Once an allocation's storage quota is reached, no files can be added to any bucket owned by that allocation until files are removed.

## Are Automatic Backups to LTS Available?

Automatic backups are not available by default. If you would like to periodically sync your bucket to a directory on your local machine or Cheaha, you will need to set up a cron task to submit a Slurm job that will run a sync. IF you would like to implement this for your own bucket, please [contact us](../../index.md#how-to-contact-us).

## Why Can I Not Interact With a File in My Bucket?

While S3's object storage system does not have POSIX permissions seen in a Linux system entirely, we have found that users who upload files to a shared allocation have ownership permissions on those objects, and the bucket owner and stewards cannot interact with those objects by default. Instead, owners and stewards need to be given explicit permissions to move or delete all objects in a bucket. This can be dealt with by adding the following sections to the policy file:

``` json
{
    "Sid": "admin",
    "Effect": "Allow",
    "Principal": {
        "AWS": [
            "arn:aws:iam:::user/example_core",
            "arn:aws:iam:::user/allocation_owner@uab.edu"
        ]
    },
    "Action": [
        "s3:*"
    ],
    "Resource": [
        "arn:aws:s3:::bucket",
        "arn:aws:s3:::bucket/*"
    ]
},
{
    "Sid": "data-manager",
    "Effect": "Allow",
    "Principal": {
        "AWS": [
            "arn:aws:iam:::user/blazerid@uab.edu"
        ]
    },
    "Action": [
        "s3:ListBucket",
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:GetBucketPolicy",
        "s3:PutBucketPolicy"
    ],
    "Resource": [
        "arn:aws:s3:::bucket",
        "arn:aws:s3:::bucket/*"
    ]
}
```

## How Can I Share a Bucket With All LTS Users?

The following policy file will give read permission to all LTS users for all objects in a bucket:

``` json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "admin",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam:::user/allocation_owner@uab.edu"
                ]
            },
            "Action": [
                "s3:*"
            ],
            "Resource": [
            "arn:aws:s3:::bucket",
            "arn:aws:s3:::bucket/*"
            ]
        },
        {
            "Sid": "read-only-all",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam:::user/*"
                ]
            },
            "Action": [
                "s3:ListBucket",
                "s3:GetObject"
            ],
            "Resource": [
            "arn:aws:s3:::bucket",
            "arn:aws:s3:::bucket/*"
            ]
        }
    ]
}
```

## Can I Change Permissions on a Bucket via Globus?

As of now, there is no way to change permissions on a bucket via [Globus](../transfer/globus.md). The only way to change permissions is via the command line.
