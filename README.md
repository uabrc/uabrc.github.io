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

### Markdown Style

Linting is controlled by [.markdownlint.json](.markdownlint.json). Linting codes are documented here: <https://github.com/DavidAnson/markdownlint/tree/main/doc>. Our choices are outlined below.

- **MD003**: Open ATX headers denoted by one or more leading hash `#` characters.
- **MD004**: Unordered list items markers are the dash `-` character.
- **MD007**: Unordered list indentation of 4 characters.
- **MD009**: Trailing spaces not allowed.
- **MD010**: Hard tab characters `\t` not allowed.
- **MD012**: Multiple consecutive blank lines not allowed.
- **MD013**: Line length not enforced. Use word wrapping in your editor instead.
- **MD022**: Headings must have exactly one blank line before and one after.
- **MD025**: Only one top-level heading (single hash `#` character) allowed per file.
- **MD029**: All ordered list item markers are `1.` to provide consistent width and spacing for improved readability.
- **MD030**: Exactly one space character between list item markers and list item contents, e.g., `1. item`.
- **MD031**: Fenced code blocks must have exactly one blank line before and one after.
- **MD033**: No HTML elements allowed, e.g. `<br>`.
- **MD035**: Horizontal rules must be exactly `---`.
- **MD040**: Fenced code block language may contain additional content, allowing the use of, e.g., line numbering with `mkdocs-material`.
- **MD041**: The first line in each file must be a top-level heading (single has `#` character).
- **MD043**: Heading structure is not prescribed.
- **MD044**: Proper names should have correct capitalization. Code blocks are excluded, HTML elements are included. See [.markdownlint.json](.markdownlint.json) for a complete list.
- **MD046**: Code blocks must be fenced style, e.g., surrounded by `` ``` ``.
- **MD048**: Fenced code blocks must use backtick `` ` `` characters.
- **MD049**: Emphasized text (_this text is emphasized_) must use single underscores, e.g., `_this text is emphasized_`.
- **MD050**: Strong text (**this text is strong**) must use double asterisks, e.g., `**this text is strong**`.
- **MD055**: Table rows must have leading and trailing pipe `|` characters.

### Maintenance

#### URL Validation

We are using [linkchecker](https://github.com/linkchecker/linkchecker) to validate external repository URLs.

1. Install `build-env.yml` and activate
1. Run `linkchecker --config=.linkcheckerrc ./docs/*.md > linkchecker.log`
1. Review `linkchecker-out.csv`

#### Manual Markdown Linting

We are using [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2) for markdown linting.

1. Install `build-env.yml` and activate
1. Run `markdownlint-cli2 "**/*.md" "#node_modules" 2> markdownlint-cli2-out.log`
1. Review `markdownlint-cli2-out.log`

We use `.markdownlint.json` to handle markdown formatting rules, rather than placing it in `.markdownlint.json`.
