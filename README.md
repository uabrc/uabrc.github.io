# Researcher Facing Documentation

Our documentation is available at <https://uabrc.github.io/>.

## Contributing

Please see <https://uabrc.github.io/contributor_guide/>.

## Developer Notes

### Generating Partition and QoS tables

The repo for generating these files is located at <https://github.com/wwarriner/slurm_status_tools/>.

To use, install the conda environment and run the following commands.

```bash
python -u sstatus.py -c partitions > partitions.csv
python -u sstatus.py -c qos > qos.csv
```

### Generating and Maintaining Hardware tables

The repo for the main hardware table is located at <https://gitlab.rc.uab.edu/rc-data-science/data-science-internal/cluster-fabric-docs>.

To use follow the readme at the repo.

### Maintenance

#### URLs

We are using [linkchecker](https://github.com/linkchecker/linkchecker) to validate external repository URLs.

1. Install `build-env.yml` and activate
1. Run `linkchecker --config=linkcheckerrc ./docs/*.md > linkchecker.log`
1. Review `linkchecker-out.csv`
