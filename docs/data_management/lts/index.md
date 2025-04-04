# Long-Term Storage

UAB Long-term storage (LTS) is an S3 object-storage platform hosted at UAB. This storage is designed to hold data that is not currently being used in analysis but should be kept for data sharing, recapitulation purposes, or reused for further analysis in the future. This documentation covers multiple methods for accessing LTS in Windows, Mac, and Linux environments.

<!-- markdownlint-disable MD046 -->
!!! tip

    [Globus](../transfer/globus.md#long-term-storage-s3-lts-connector) may be used to transfer data with LTS.
<!-- markdownlint-enable MD046 -->

## Terminology

When talking about S3 storage, some terms are different compared to a normal filesystem. This section is here to briefly explain some differences in case you go to other documentation and see these terms instead.

- `object`: any unit (i.e. file) stored in LTS. Typical folders and files do not exist in S3.
- `bucket`: The root which objects are stored in. Each allocation can have a certain number of buckets and each bucket can be shared individually with other users. Bucket names are unique across the entire LTS platform (see the section on [duplicate names](#avoiding-duplicate-names-for-buckets)).
- `prefix`: Used in place of a file path to an object, and so can be used to represent an object's place in a typical filesystem. Stored as metadata in each object, prefixes are used for searches in a bucket.
- `policy`: sets permissions for whole buckets and individual objects. Policies allow or deny access to buckets for individual allocations. These are controlled by the owner of the bucket.
- `access key`: a unique identifier given to each user for access to LTS, similar to a username. A user's access key is preset and given to them after allocation setup.
- `secret key`: a credential string similar to a password given to each user for access to LTS. The secret key is preset and given to the user after allocation setup.

<!-- markdownlint-disable MD046 -->
!!! danger

    Never give access and secret keys for individual or shared allocations to anyone! Treat them as usename and password, respectively.

    If you need to give elevated permissions to other users to view, upload, download, delete, etc. any data from a bucket, those permissions can be changed via [bucket policies](iam_and_policies.md) without giving out keys. Please [contact Research Computing](../../index.md#how-to-contact-us) for help setting up and applying policies if you need it
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! note

    If you lose your access and secret keys, please submit a [support ticket](../../index.md#how-to-contact-us) to <support@listserv.uab.edu> to request your keys. Keys will only be given to an allocation owner as verified by RC staff.
<!-- markdownlint-enable MD046 -->

This documentation will use the standard file and path terms since those are more easily understood by most users. Just be aware that documentation such as [AWS CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/index.html) will use terms prefix, object, and others that are not standard in a typical filesystem.

## Requesting an Allocation

UAB researchers do not have automatic access to LTS, and currently, single sign on is not enabled. To request access to LTS, please send an email to <support@listserv.uab.edu>. You will be then be given an Access Key and a Secret Access Key, both of which will be used later on. Keep track of both of these keys and do not share them with anyone else, these are your login credentials for LTS. Please visit [Shared Storage](../index.md) to review guidelines to request a LTS allocation.

## Avoiding Duplicate Names for Buckets

Bucket names are shared across all LTS. This means you cannot create a bucket with a name that has already been created by someone else, even if that bucket is not shared with you. When creating bucket names make them specific and/or unique.

At minimum, use something like "blazeridlab" for storing data for your entire lab. Or, use the name of a specific dataset that is being stored. Avoid generic names like "trial" or "my-storage" or "test" or "lab".

Better practice when naming buckets is to use a short, descriptive and memorable name, then append a universally unique identifier (UUID) to the end. Websites like <https://www.uuidgenerator.net/> may be used to generate and copy UUIDs. There are $5.3\times 10^{36}$ possible UUIDs, which means the chance of duplicating one is virtually zero. Please see [Wikipedia](https://en.wikipedia.org/wiki/Universally_unique_identifier#Collisions) for math supporting the low rate of duplication.

## What to Do With Data When I Leave UAB?

See our [Leaving UAB page](../../account_management/leaving_uab.md).
