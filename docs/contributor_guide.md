# Contributor Guide

We welcome contributions from our community. To ensure a high-quality documentation experience, we have some guidelines for contributors who wish to create.

<!-- markdownlint-disable MD046 -->
!!! construction

    This contributor guide is a work in progress and may change and develop over time. Please bear with us, and feel free to offer suggestions.
<!-- markdownlint-enable MD046 -->

## Prerequisites

We are using Visual Studio Code (VSCode) for development with the following extensions installed. While VSCode is not required, it can help with automating formatting, linting and Anaconda environment management. VSCode may be obtained from [Visual Studio Code](https://code.visualstudio.com/) and documentation is available at [VSCode: Docs](https://code.visualstudio.com/docs).

Several extensions are useful for this project and are listed below. Extensions may be obtained by searching the Extensions Menu in VSCode by pressing `ctrl + shift + x`. More information on managing extensions is available at [VSCode: Extension Marketplace](https://code.visualstudio.com/docs/editor/extension-marketplace).

- Python [`ms-python.python`] (for Anaconda environment management)
- Markdown All in One [`yzhang.markdown-all-in-one`]
- markdownlint [`DavidAnson.vscode-markdownlint`]
- Prettier - Code formatter [`esbenp.prettier-vscode`]

To make the best use of formatting extensions for this project, please add the following block to your `settings.json` file. These changes can be made:

  1. Within the VSCode project file in the `.vscode` folder, affecting only this project *--OR--*
  2. To the global VSCode settings file, affecting all projects. To change the global file, press `ctrl + shift + p` to open the Command Palette, then search for `Preferences: Open Settings (JSON)` and append the following content.

### VSCode `settings.json` Additions

```json
  "[html]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[markdown]": {
    "editor.defaultFormatter": "yzhang.markdown-all-in-one"
  },
  "[yaml]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "markdownlint.config": {
    "MD046": { "style": "fenced" }
  },
  "markdown.extension.list.indentationSize": "inherit"
```

Before you can get started working on contributions, you'll need a copy of the repository. The first step, done only once, is to fork the repository in GitHub to your personal account. The repository is located at <https://github.com/uabrc/uabrc.github.io>. More in-depth documentation on forking can be found at [GitHub: Fork a Repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

Once the fork has been created, you can clone your fork using the Command Palette (`ctrl + shift + p`) and `Git: Clone...` in VSCode, or at the command line. More information on cloning can be found at [GitHub: Cloning a Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

### Local Machine Setup (Laptop/Desktop)

The Python extension will activate when you open any Python file. The file `test.py` has been added for convenience, simply open that file to activate the extension. The extension will show the currently activated environment near the bottom-left corner of the VSCode window.

Please create an Anaconda environment using `build_env.yml` using the following.

```shell
conda env create -f build_env.yml
```

Activate the environment in VSCode by clicking the currently activated environment in the bottom-left of the VSCode window. A menu will appear allowing you to select from discovered environments. You may need to reload VSCode to get the environment to appear if it was just created.

To build the documentation locally, use `mkdocs build`. Be sure to fix all warnings before submitting a pull request.

### GitHub Setup

To view your changes as they would appear on the official documentation website, you'll need to set up GitHub Pages in your fork. Navigate to your fork repository URL and click the "Settings" tab. Click "Pages" under "Code and automation". Follow the instructions here to set up a source: [GitHub Pages Docs](https://docs.github.com/en/pages).

## Workflow

1. Open the cloned repository in VSCode.
2. Create a branch with a short but meaningful name for your intended changes.
3. Make changes to markdown files.
4. Commit changes to the new branch.
5. Push the branch to your remote repository on GitHub.
6. Check your contributions match
7. Make a pull request to the upstream repository.

From here your pull request will go through a review process. The following criteria are checked.

1. No linting errors
2. Correct formatting
3. Image alternate text (alt text)
4. Images must use the gallery functionality, formatted as `![!alttext](path/to/file)`. Note the leading `!` in the alttext.
5. Valid internal and external links

We will also make an attempt to check your information for accuracy, as well as proofread the text. Bear in mind our time is limited and we are not infallible, so please double-check your pull requests!

## File Organization

To Be Determined

## Formatting

- Links must be one of the following formats including all punctuation and brackets:
    - Bare:
        - `<https://google.com>`
        - `<support@listserv.uab.edu>`
    - Named with a schema:
        - `[website](https://google.com)`
        - `[email](mailto:support@listserv.uab.edu)` note the `mailto:` schema!
    - Relative internal
        - `[relative internal](help/faq.md)`
- All internal links must be relative. For example, use `./file.md` not `/docs/file.md`.

## Redirects

If a page name must change, or the location of a page must change, it is necessary to create a redirect for that page so we don't break bookmarks and incoming links targeting our documentation.

Redirecting pages is possible using the plugin at <https://github.com/datarobot/mkdocs-redirects>. To redirect a page, add a line in `mkdocs.yml` under the following keys. The line takes the form `original page location: new page location`, and each side of `:` must be a full path under `docs/`. An example is below.

```yaml
plugins:
  - redirects:
      redirect_maps:
        account_management/uab_researcher.md: account_management/cheaha_account.md
```

## Section Index Pages

To create a section index page:

1. Create a file called `index.md` in a reasonable directory location for that section.
2. Add something like the following to that section entry under `nav:` in `mkdocs.yml`.

    ```yml
    nav:
      ...
      - Cheaha Guide:
        - cheaha/index.md  # add the index.md here.
        - Hardware: ...
        - ...
      ...
    ```

3. When a site visitor clicks `Cheaha Guide` in the nav pane, the page `cheaha/index.md` will be loaded.

## Linting Known Issues

There are known issues with the markdown linter and some of our non-standard plugins, especially admonitions (specifically a conflict involving fenced vs indented code blocks). To fix these cases please use one of the following methods. The `<lint warning code>` can be found by hovering over the yellow squiggles in VSCode to bring up the warning lens.

Please do not use these to silence all linter warnings, only for fixing known issues. Please read the warning lenses given by VSCode to identify the cause of the warning.

### Silence Linter Warning for a Block

```markdown
<!-- markdownlint-disable <lint warning code> -->
`linter error here`

`maybe multiple lines`
<!-- markdownlint-enable <lint warning code> -->
```

### Silence Linter Warning for a Single Line

We encourage denoting the warning being silenced here by filling out the `<lint warning code>`, though it isn't required for the single line case.

```markdown
<!-- markdownlint-disable-next-line <lint warning code> -->
`linter error here just for this line`
```

### False Positive Lint Warnings from Admonitions

We allow and encourage the use of [admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#supported-types) in our documentation, where appropriate. Because these are created using a plugin and are "non-standard" `markdown`, the VSCode `markdownlint` extension does not recognize admonitions and may produce a false positive warning about inconsistent code block styles.

Two styles of code block are allowed in `markdown`: `fenced` and `indented`. To work around the false positive warning about admonitions, we require all code blocks to be `fenced`. This is enforced by adding an entry to the [VSCode `settings.json` file](#vscode-settingsjson-additions). Now all admonitions will be consistently assigned the warning `MD046`, which can be disabled by placing all admonitions in between the following comment block fences. The comment lines must be indented to the same level as the start of the admonition.

```markdown
<!-- markdownlint-disable MD046 -->

<!-- markdownlint-enable MD046 -->
```

The process can be simplified in VSCode using snippets. Bring up the command palette and type `snippets` and open `Preferences: Configure User Snippets`. Then type `markdown` and open it. A `json` file will be opened. Add the following content between the outermost braces and then save the file.

```json
  "Disable Markdown Lint MD046 for a Block": {
    "prefix": "md046 disable",
    "body": [
      "<!-- markdownlint-disable MD046 -->",
      "$TM_SELECTED_TEXT",
      "<!-- markdownlint-enable MD046 -->"
    ],
    "description": "Disables warning Markdown Lint MD046 for the selected block."
  }
```

The snippet will surround selected text with the appropriate linter disable fencing for MD046. To use the snippet, opne the IntelliSense lens using `ctrl + space` (or `cmd + space`), then type `md046` until the `prefix` shows up as the first entry in the list. Then press `tab`.

The workaround is needed because `markdownlint` has no plans to add support for admonitions. There is no `markdownlint` plugin for that support either, and we don't have the ability to develop such a plugin.

## Accessibility

Color vision deficiency checker: <https://www.toptal.com/designers/colorfilter/>
Contrast checker: <https://webaim.org/resources/contrastchecker/>

## Branding Guidance

- Brand main page: <https://www.uab.edu/toolkit/branding>
- Brand colors: <https://www.uab.edu/toolkit/brand-basics/colors>
- Copyright guidance: <https://www.uab.edu/toolkit/trademarks-licensing/uab-trademarks>

## Terminology

- `Research Computing (RC)` for the IT group supporting campus HPC resources.
- `UAB Campus Network` for the hard-wired network physically located on UAB campus, and the UAB Secure wifi.
- `UAB Campus VPN` for the VPN to tunnel remote connections through the UAB Campus Network.
