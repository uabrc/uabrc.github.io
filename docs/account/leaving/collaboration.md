---
hide:
    toc: true
---

# Leaving UAB — Continuing Collaboration

{% from "_macro/support.md.j2" import contact_support_link %}

Because you intend to have a continuing collaboration after leaving UAB, you will need to transition from your current RCS account to a new one.

Your current account is based on your BlazerID and will become inaccessible following the grace period. So, to continue operations, you will need to create a new RCS account based on a XIAS account.

{% include "account/_template/xias_need_sponsor.md.j2" %}

## What Is the XIAS Account Transition Procedure?

1. Identify a UAB Sponsor for the XIAS account. This should be one of the UAB-affiliated collaborators you intend to work with.
1. Create the [XIAS Account](../xias/index.md).
1. Create a new [RCS Account](../rcs/create.md)
1. Please {{ contact_support_link() }} to request transfer of data from your previous BlazerID RCS account to your new XIAS RCS account.

    Please use the following template when sending the email.

    Your Sponsor must give approval for the transfer.

    ```text
    RCS Former UAB Affiliate Account Transfer

    Please transfer my BlazerID RCS account data to my XIAS RCS account.

    - My former BlazerID: __
    - My new XIAS email address: __
    - What to transfer
        - Cheaha storage individual allocation: YES/NO
        - Long-Term Storage (LTS) individual allocation: YES/NO
        - Cloud.rc (OpenStack) individual project: YES/NO
    ```

{% include "account/xias/_template/xias_help_section.md.j2" %}
