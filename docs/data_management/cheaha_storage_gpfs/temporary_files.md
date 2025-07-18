# Temporary Files (`/tmp/` Directory)

Please do not use the directory `/tmp/` as storage for temporary files. The `/tmp/` directory is local to each node, and a full `/tmp/` directory harms compute performance on that node for all users. Instead, please use [local scratch](./scratch.md#local-scratch) for fastest access and [`$USER_SCRATCH`](./scratch.md#user-scratch) for largest space.

Some software packages default to using `/tmp/` without any warning or documentation, especially software designed for personal computers. We may reach out to inform you if your software fills `/tmp/`, as it can harm performance on that compute node. If that happens we will work with you to identify ways of redirecting temporary storage to one of the scratch spaces.

## Software Known to Use `/tmp/`

The following software are known to use `/tmp/` by default, and can be worked around by using the listed flags. See [Local Scratch](scratch.md#local-scratch) for more information about creating a local temporary directory. You may need to manually create (and clean) `/local/$USER/$SLURM_JOB_ID/`.

- [Java](https://docs.oracle.com/cd/E63231_01/doc/BIAIN/GUID-94C6B992-1488-4FC7-85EC-91E410D6E7D1.htm#BIAIN-GUID-94C6B992-1488-4FC7-85EC-91E410D6E7D1): `java * -Djava.io.tmpdir=/local/$USER/$SLURM_JOB_ID`
- [UMI Tools](https://umi-tools.readthedocs.io/en/latest/common_options.html): `umi_tools * --temp-dir=/local/$USER/SLURM_JOB_ID`
- [Samtools Sort](http://www.htslib.org/doc/samtools-sort.html): `samtools sort * -T /local/$USER/$SLURM_JOB_ID`
- [GATK Tool](https://gatk.broadinstitute.org/hc/en-us/community/posts/360072269012--tmp-dir-option-user-error): `gatk --java-options * --tmp-dir /local/$USER/$SLURM_JOB_ID`
- [NVIDIA Clara Parabricks](https://docs.nvidia.com/clara/parabricks/latest/gettingstarted.html): `pbrun * --tmp-dir=/local/$USER/$SLURM_JOB_ID`.
- [FastQC](https://home.cc.umanitoba.ca/~psgendb/doc/fastqc.help): `fastqc * -d /local/$USER/$SLURM_JOB_ID`
- [MACS2](https://manpages.org/macs2_callpeak): `macs2 callpeak * --tempdir /local/$USER/$SLURM_JOB_ID`

Software known to use `/tmp/` by default with no known workaround:

- [Keras](https://github.com/tensorflow/tensorflow/blob/5bb81b7b0dd140a4304b92530614502c0c61a150/tensorflow/python/keras/utils/data_utils.py#L205) has `/tmp/.keras` hardcoded as a fallback cache directory if `~/.keras` is inaccessible. See [TensorFlow GitHub Pages issues](https://github.com/tensorflow/tensorflow/issues/38831) for a discussion of the issue.
