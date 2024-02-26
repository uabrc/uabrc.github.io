# Data Transfer Case Studies

## Parallel Transfer of Data with s5cmd

A research team on campus was nearing capacity in their [GPFS](../storage.md#what-type-of-storage-do-i-need) `/data/project/` storage allocation. We advised they request an S3-compatible [LTS (Long-Term Storage)](../lts/index.md) allocation and to transfer inactive data to [buckets](../lts/index.md#terminology) in the LTS allocation.

The research team needed to transfer 13 TB of data as quickly as possible to make room for data from active projects.

We initially recommended [Globus](../transfer/globus.md) with the [S3 Connector](../transfer/globus.md#long-term-storage-s3-lts-connector), but determined the average 90 Mbps transfer rate would take about 13.5 days. For many use-cases, the robustness and ease-of-use of Globus means less effort, but in this case the time pressure meant we needed to find a faster alternative.

After some collaborative discussion and research, we found the software [s5cmd](../lts/interfaces.md#s5cmd). The software is intended to be a parallelizable alternative to other S3-compatible data transfer programs such as [s3cmd](../lts/interfaces.md#s3cmd) and [rclone](../transfer/rclone.md).

Unfamiliar with the software, we created a few quick experiments to determine how to make s5cmd as fast as possible. These initial experiments were limited to 1 Gbps due to external network configuration. Moving nodes into our `sciencedmz` partition, with access to a 10 Gbps link, raised the data transfer rate for some of the test cases.

The following bash script was used to run each test case, and random files were generated using <<https://github.com/wwarriner/python_random_file_generator>:. All data was transferred from GPFS to LTS using nodes available on Cheaha. The `express` node had 2x 24 core Intel Xeon E5-2680 v4 CPUs and 768 GB memory. The `amd-hdr100` node had 2x 64 core Epyc 7713 Milan CPUs and 512 GB memory. If you decide to use this script, you'll need to provide your own `$SOURCE_PATH` on the GPFS filesystem and `$DESTINATION_PATH` on LTS.

```shell
#!/bin/bash

start_time="$(date -u +%s.%N)"

s5cmd --stat \
    --numworkers=$SLURM_JOB_CPUS_PER_NODE \
    --endpoint-url=https://s3.lts.rc.uab.edu/ \
    cp \
    $SOURCE_PATH \
    s3://$DESTINATION_PATH/

end_time="$(date -u +%s.%N)"
elapsed="$(bc <<<"$end_time-$start_time")"
echo "Total of $elapsed seconds elapsed for process"
```

The test cases and results are in the following table. Globus is provided for comparison. Please be aware that Globus data transfers occur serially and are not hand-tuned for speed on specific datasets. Globus works best with data transfers that require minimal human interaction and can run over long periods. From the data, we realized that more cores provide greater benefit when there are a larger number of smaller files to transfer.

| # files | MiB / file | numworkers (cores) | mem (GB) | source       | rate (Gbps) | time for 13 TB (hr) |
| ------: | ---------: | -----------------: | -------: | ------------ | ----------: | ------------------: |
|         |            |                  1 |          | Globus       |        0.09 |               320.0 |
|         |            |                    |          |              |             |                     |
|    1000 |         10 |                  8 |        8 | `express`    |        0.95 |                30.0 |
|    1000 |         10 |                100 |      200 | `amd-hdr100` |        8.00 |                 3.6 |
|         |            |                    |          |              |             |                     |
|      39 |       1024 |                  8 |        8 | `express`    |        5.10 |                 5.6 |
|       1 |       4800 |                100 |       64 | `amd-hdr100` |        0.67 |                19.4 |

Exploring the features of s5cmd further, we found the `--concurrency` flag for the `cp` subcommand. The flag allows s5cmd to break files into chunks of a chosen size, and transfer a chosen number of those chunks at the same time. Changing the script above to include the `--concurrency` flag, we have the following script. With this script, the speed of single large file transfers (last line in the table) was increased by ~20% to 0.8 Gbps.

```shell
#!/bin/bash

start_time="$(date -u +%s.%N)"

s5cmd --stat \
    --numworkers=$SLURM_JOB_CPUS_PER_NODE \
    --endpoint-url=https://s3.lts.rc.uab.edu/ \
    cp \
    --concurrency=$SLURM_JOB_CPUS_PER_NODE \
    $SOURCE_PATH \
    s3://$DESTINATION_PATH/

end_time="$(date -u +%s.%N)"
elapsed="$(bc <<<"$end_time-$start_time")"
echo "Total of $elapsed seconds elapsed for process"
```

## checksum verification

rclone

## Conclusions

The key takeaways of using s5cmd:

- leverages parallelim to greatly increase transfer speeds
- performs best with multiple files against LTS
- many small files? use high numworkers, low concurrency
- few large files? use high numworkers, high concurrency
- concurrency should be no larger than numworkers
- use rclone for checksum verification

## How to use it

link to lts interfaces
