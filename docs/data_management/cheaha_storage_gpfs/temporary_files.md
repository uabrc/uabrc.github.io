# Temporary Files (`/tmp/` Directory)

The `/tmp/` directory is local to each node and reserved for Linux operating system use. A full `/tmp/` directory on a compute node reduces compute performance for everyone using the node. Do not use the directory `/tmp/` as storage for temporary files. Instead, please use [local scratch](./local_scratch.md) for fastest access and [network scratch](./network_scratch.md) for largest space.

Some software packages default to using `/tmp/` without warning or documentation, especially software designed for personal computers. We may reach out to inform you if your software fills `/tmp/`, as it can harm performance on that compute node. If that happens we will work with you to redirect temporary storage to one of the scratch spaces.

<!-- markdownlint-disable MD046 -->
!!! important

    Do not use `/tmp/` for temporary file storage.

    Do use [local scratch](./local_scratch.md) or [network scratch](./network_scratch.md).
<!-- markdownlint-enable MD046 -->

## Software Known to Use `/tmp/`

The following software are known to use `/tmp/` by default, and can be worked around by using the listed flags. See our [Local Scratch page](local_scratch.md) for more information about creating a local temporary directory. Also see our [Network Scratch page](./network_scratch.md) for larger scratch storage. Be sure to delete files when your jobs are finished.

- [Java](https://docs.oracle.com/cd/E63231_01/doc/BIAIN/GUID-94C6B992-1488-4FC7-85EC-91E410D6E7D1.htm#BIAIN-GUID-94C6B992-1488-4FC7-85EC-91E410D6E7D1): `java * -Djava.io.tmpdir=/local/$USER/$SLURM_JOB_ID`
- [UMI Tools](https://umi-tools.readthedocs.io/en/latest/common_options.html): `umi_tools * --temp-dir=/local/$USER/SLURM_JOB_ID`
- [Samtools Sort](http://www.htslib.org/doc/samtools-sort.html): `samtools sort * -T /local/$USER/$SLURM_JOB_ID`
- [GATK Tool](https://gatk.broadinstitute.org/hc/en-us/community/posts/360072269012--tmp-dir-option-user-error): `gatk --java-options * --tmp-dir /local/$USER/$SLURM_JOB_ID`
- [NVIDIA Clara Parabricks](https://docs.nvidia.com/clara/parabricks/latest/gettingstarted.html): `pbrun * --tmp-dir=/local/$USER/$SLURM_JOB_ID`.
- [FastQC](https://home.cc.umanitoba.ca/~psgendb/doc/fastqc.help): `fastqc * -d /local/$USER/$SLURM_JOB_ID`
- [MACS2](https://manpages.org/macs2_callpeak): `macs2 callpeak * --tempdir /local/$USER/$SLURM_JOB_ID`

Software known to use `/tmp/` by default with no known workaround:

- [Keras](https://github.com/tensorflow/tensorflow/blob/5bb81b7b0dd140a4304b92530614502c0c61a150/tensorflow/python/keras/utils/data_utils.py#L205) has `/tmp/.keras` hardcoded as a fallback cache directory if `~/.keras` is inaccessible. See [TensorFlow GitHub Pages issues](https://github.com/tensorflow/tensorflow/issues/38831) for a discussion of the issue.
