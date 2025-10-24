# Leaving UAB

{% from "_macro/support.md.j2" import contact_support_link %}

If your life and career plans take you away from UAB, then this article is designed to help you. We hope to give you a better understanding of expectations and responsibilities for your account and data.

All [research data](#what-is-research-data) produced as part of UAB research operations is owned by UAB. Funding agencies (e.g., NIH, NSF) often have strict data retention and sharing regulations. Transferring UAB-owned and/or agency funded data requires involvement of the [Office of Sponsored Programs (OSP)](https://www.uab.edu/research/home/osp-about/contact).

If you have questions, concerns, or doubts after reading this page, we highly recommend you {{ contact_support_link() }}.

<!-- markdownlint-disable MD046 -->
!!! note

    The contents of this article apply only to [research data](#what-is-research-data). For administrative and other data you will need to discuss with the UAB Administrative units appropriate to you and your situation. You can discuss with your faculty supervisor or contact <askit@uab.edu> for more information on what to do with other data.
<!-- markdownlint-enable MD046 -->

## What Is Research Data?

Research data acquired, analyzed, created, or produced as part of UAB research operations is property of UAB.

## Why Is Research Data Important?

All research data must be managed according to UAB, UAB IT, and funding agency policies and requirements.

UAB research data may not leave UAB systems without a Data Use Agreement (DUA) signed by the [Office of Sponsored Programs (OSP)](https://www.uab.edu/research/home/osp-about/contact).

## What Is the Grace Period?

Researchers have a {{ account.leaving.grace_period_time }} grace period following the end of their relationship with UAB.

Due to security requirements imposed by US federal funding agencies, we are unable to extend the grace period.

## What Happens to My RCS Account?

Your RCS account will be accessible for 30 days following the end of your relationship with UAB.

The grace period is provided for you to finalize research data transfers.

The same grace period applies to all other Research Computing platform accounts.

If you anticipate needing more than 30 days to finalize transfers, {{ contact_support_link() }} as soon as possible so we can make arrangements or work to improve data transfer efficiency.

## What Are My Next Steps?

For more information on what to do next, please select the tab below that most closely matches your situation.

<!-- markdownlint-disable MD046 -->
=== "I Need Continuing Access"

    If you need RCS access beyond the end of the {{ account.leaving.grace_period_time }} grace period, you will need to create a [XIAS Account](../xias/index.md).

    {% include "account/_template/xias_need_sponsor.md.j2" indent content %}

    Please see [Continuing Collaboration](collaboration.md)

=== "I Will Be Hired in a New Role"

    - **New role doesn't require RCS access?** Please select the "I No Longer Need Access" tab for next steps.
    - **Hire date within grace period?** No action required, expect continuous access.
    - **Hire date after grace period ends?** Please {{ contact_support_link() }}.

=== "I No Longer Need Access"

    If the {{ account.leaving.grace_period_time }} grace period is enough time, then please be aware there are expectations and responsibilities for final handling of your research data.

    Please see [Final Steps For Research Data](final_steps.md)
<!-- markdownlint-enable MD046 -->

{% include "account/xias/_template/xias_help_section.md.j2" %}
