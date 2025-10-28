# Welcome to UAB Research Computing

The Research Computing System (RCS) provides a framework for sharing research data, accessing computing power, and collaborating with peers on campus and around the globe. We have deployed a dynamic "network of services" to facilitate organizing, studying, and sharing research data.

## Announcements

<!-- markdownlint-disable MD046 -->
<!-- markdownlint-disable no-inline-html -->
{% if announcements %}
{% for announcement in announcements %}
???+ announcement "Announcement: {{ announcement.title }}"
    {{ announcement.content | indent(4) }}
    <hr>
    <div class="dates">
        <div class="effective-dates">
            **Effective:**
            {%- if announcement.start_date %}
            {{ announcement.start_date }}
            {% endif -%}
            {%- if announcement.start_date and announcement.end_date -%}
            —
            {%- endif -%}
            {%- if announcement.end_date %}
            {{ announcement.end_date }}
            {% endif -%}
        </div>
        <div class="posted-date">
            _Posted: {{ announcement.posted_date }}_
        </div>
    </div>
{% else %}
    {{ no_announcements }}
{% endfor %}
{% else %}
    {{ no_announcements }}
{% endif %}
<!-- markdownlint-enable no-inline-html -->
<!-- markdownlint-enable MD046 -->

## How Do I Get Started?

{{
    renderer.render_cards(
        cards.news,
        cards.account.rcs.create,
        cards.platforms.cheaha.ood.overview,
        cards.platforms.cheaha.slurm.overview,
        cards.data.individual_storage,
        cards.data.shared_storage,
        cards.data.transfer_options,
    )
}}

### Featured Tutorials

- Compute
    - [Getting Started on Cheaha with Open OnDemand (OOD)](./cheaha/open_ondemand/index.md)
    - [`sbatch` Jobs with Slurm](./cheaha/slurm/slurm_tutorial.md)
    - [PyTorch and Tensorflow on Cheaha with Anaconda](./cheaha/tutorial/pytorch_tensorflow.md)
    - [Getting Started with Cloud.RC for On-Premises Cloud Computing](./uab_cloud/tutorial/index.md)
- Data Management
    - [How Do I Use Globus for Data Transfer?](./data_management/transfer/tutorial/index.md)
    - [What Type of Storage Do I Need?](./data_management/index.md#what-type-of-storage-do-i-need)

### Success Stories

- December 17th, 2024: [Cheaha helps Cardenas lab speed up work](https://www.uab.edu/it/news/item/cheaha-helps-cardenas-lab-speed-up-work)
- March 19th, 2024: [Open Science Grid Gives Power of Multiple Cheahas](https://www.uab.edu/it/news/item/open-science-grid)
- March 19th, 2024: [NVIDIA Clara Parabricks Tool Speeds Genomic Analysis for UAB Researchers](https://www.uab.edu/it/news/item/parabricks-speeds-genomic-analysis)
- [more stories...](https://www.uab.edu/it/news/research-computing)

### Outreach

The UAB IT Research Computing Group has collaborated with a number of prominent research projects, organizations, and Research Core Facilities at UAB to identify use cases and develop requirements. Our collaborators include, but are not limited to, the following list.

- [Center for Clinical and Translational Science (CCTS)](https://www.uab.edu/ccts/)
- [Center for Computational Genomics and Data Science (CGDS)](https://sites.uab.edu/cgds/)
- [Department of Computer Science](https://www.uab.edu/cas/computerscience/)
- [Heflin Center for Genomic Scieces (HCGS)](https://www.uab.edu/hcgs/)
- [Institutional Research Core Program (IRCP)](https://www.uab.edu/cores/ircp/)
    - [Cryo-Electron Microscopy Facility (CEMF or CryoEM)](https://www.uab.edu/cores/ircp/cryo-em)
    - [Flow Cytometry and Single Cell Core Facility (FCSC)](https://www.uab.edu/cores/ircp/fcsc)
    - [Small Animal Imaging Facility (SAIF)](https://www.uab.edu/cores/ircp/saif)
    - [UAB Biological Data Science Core (U-BDS)](https://www.uab.edu/cores/ircp/bds)
- [Lister Hill Library (LHL)](https://library.uab.edu/locations/lister-hill)
- [O'Neal Comprehensive Cancer Center (CCC)](https://www.onealcanceruab.org/)
- [School of Engineering (SoE)](https://www.uab.edu/engineering/home/)
- [South Eastern Biosafety Laboratory (SEBLAB)](https://www.uab.edu/research/seblab/)

If you would like to build a collaborative effort with Research Computing, please [Contact Us](#how-to-contact-us).

## How to Contact Us

{{
    renderer.render_cards(
        cards.support.email,
        cards.support.office_hours,
        cards.support.page,
    )
}}

## About Us

Research Computing is developed and supported by UAB IT's Research Computing Group. We are developing a core set of applications to help you easily incorporate our services into your research processes and this documentation collection to help you leverage the resources already available. We follow the best practices of the Open Source community and develop our software in an open-source fashion.

Research Computing is an out growth of the UABgrid pilot, launched in September 2007 which has focused on demonstrating the utility of unlimited analysis, storage, and application for research. RCS is built on the same technology foundations used by major cloud vendors and decades of distributed systems computing research, technology that powered the last ten years of large scale systems serving prominent national and international initiatives like the [Open Science Grid](https://osg-htc.org/), [XSEDE](https://www.xsede.org/), the [LHC Computing Grid](https://wlcg.web.cern.ch/), and [NCIP](https://datascience.cancer.gov/).
