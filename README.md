# Researcher Facing Documentation

Our documentation is available at <https://uabrc.github.io/>.

## Contributing

Please see <https://uabrc.github.io/contributor_guide.md>.

## Developer Notes

### Generating Partition and QoS tables

The repo for generating these files is located at <https://github.com/wwarriner/slurm_status_tools/>.

To use, install the conda environment and run the following commands.

```bash
python -u sstatus.py -c partitions > partitions.csv
python -u sstatus.py -c qos > qos.csv
```

### Useful Regex

#### Checking Internal Links are Relative

There is no way to fix this automatically, so we rely on checking and reporting. A useful regex is is `\[.+\]\(/[a-zA-Z]+.*\)`. It searches for square brackets with text inside, followed by parentheses with text inside. The text inside the parentheses must start with a slash followed by letters. Another useful regex is similar `\[.+\]\((?!https)[a-zA-Z]+.*\)`. It searches for the same as before, but instead of a slash followed by letters, it starts with any letters except the string `https`, since https links are external.

#### Checking Indentation

Currently Prettier bulleted list indenting is wonky for markdown. In addition to indenting list markers, it pads out spaces after the marker. Please see [this issue](https://github.com/prettier/prettier/issues/5019) for more details. As a result, we can't automatically format markdown documents, so we need to rely on spotting incorrect indents. Use the following regex `^[ ]{1,3}[^ ]`. It will search for one to three spaces followed by a not-space character.
