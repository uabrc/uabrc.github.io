---
hide:
    toc: true
---

# Responsibilities, Expectations, and Policies

{% from "_macro/support.md.j2" import contact_support_link %}

where responsible and professional use of Cheaha accounts, storage, and computational resources is expected to maintain system integrity and support collaborative research. Please refer below for the eligibility requirements and responsibilities of Research Computing services users.

<!-- markdownlint-disable MD046 -->
=== "Student, Staff, XIAS Guest"

    {% include "account/_template/responsibilities_for_all.md.j2" indent content %}

=== "Research Faculty Supervisor"

    {% include "account/_template/responsibilities_for_all.md.j2" indent content %}
    {% include "account/_template/responsibilities_security.md.j2" indent content %}
    - Responsible and accountable for all [XIAS Guest](xias/index.md) actions and behavior.
    - Research data lifecycle management
        - Migrate unused data to [LTS](../data_management/lts/index.md) or archive.
        - Backup critical data.
        - {{ contact_support_link() }} to discuss.

=== "Core Director"

    {% include "account/_template/responsibilities_for_all.md.j2" indent content %}
    {% include "account/_template/responsibilities_security.md.j2" indent content %}
    - Responsible and accountable for all [XIAS Guest](xias/index.md) actions and behavior.
    - Research data lifecycle management
        - {{ contact_support_link() }} to discuss data management plans leveraging no-cost Research Computing resources.
<!-- markdownlint-enable MD046 -->
