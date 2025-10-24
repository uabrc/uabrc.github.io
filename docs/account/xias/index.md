---
hide:
    toc: true
---

# Create and Manage External Collaborator (XIAS) Accounts

UAB uses the XIAS system for managing external collaborator access to technology resources. To access UAB resources, external collaborators must be sponsored for a XIAS account by a UAB employee. When this occurs, the UAB employee is called "Sponsor" and the external collaborator "Guest".

We recommend Sponsor and Guest stay in close contact during the XIAS account creation process to more quickly identify and resolve any issues that may arise.

{% include "account/xias/_template/revoke_access.md.j2" %}

<!-- markdownlint-disable MD046 -->
!!! info

    XIAS stands for External Identity Access Support
<!-- markdownlint-enable MD046 -->

## What Do We Need Before Starting?

Before starting, you'll need the following prerequisites.

- The Sponsor will need:
    - an [RCS Account](../rcs/index.md);
    - _and_ a list of RCS resources each Guest needs access to;
    - _and_ the email address each Guest wants to register with.
- Guests must be able to access their email addresses.

## How Do I Create a XIAS Account?

The process for creating and configuring a XIAS account has three phases. The Sponsor is responsible for the first two phases and the Guest is responsible for the third phase. RCS adds a fourth phase, Guest RCS account creation, after the first three XIAS phases.

The XIAS account creation phases are outlined in the cards shown below.

{{
    renderer.render_cards(
        cards.account.xias.sponsor_site,
        cards.account.xias.sponsor_user,
        cards.account.xias.guest_instructions,
        cards.account.xias.guest_create_rcs,
    )
}}

## How Do I Manage XIAS Sites and Users?

Do you already have Sites and Users and want to update URIs, end dates, or which Users can access which Sites?

{{
    renderer.render_cards(
        cards.account.xias.manage_site,
        cards.account.xias.manage_user,
    )
}}

{% include "account/xias/_template/xias_help_section.md.j2" %}
