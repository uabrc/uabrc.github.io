# Researcher Facing Documentation

Our documentation is available at <https://uabrc.github.io/>.

## Contributor Notes

### Prerequisites

We are using Visual Studio Code (VSCode) for development with the following extensions installed. While VSCode is not required, it can help with automating formatting, linting and Anaconda environment management. VSCode may be obtained from [Visual Studio Code](https://code.visualstudio.com/) and documentation is available at [VSCode: Docs](https://code.visualstudio.com/docs).

Several extensions are useful for this project and are listed below. Extensions may be obtained by searching the Extensions Menu in VSCode by pressing `ctrl + shift + x`. More information on managing extensions is available at [VSCode: Extension Marketplace](https://code.visualstudio.com/docs/editor/extension-marketplace).

- Python [`ms-python.python`] (for Anaconda environment management)
- Markdown All in One [`yzhang.markdown-all-in-one`]
- markdownlint [`DavidAnson.vscode-markdownlint`]
- Prettier - Code formatter [`esbenp.prettier-vscode`]

To make the best use of formatting extensions for this project, please add the following block to your `settings.json` file. These changes can be made:

  1. Within the VSCode project file in the `.vscode` folder, affecting only this project *--OR--*
  2. To the global VSCode settings file, affecting all projects. To change the global file, press `ctrl + shift + p` to open the Command Palette, then search for `Preferences: Open Settings (JSON)` and append the following content.

```json
  "[html]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[markdown]": {
    "editor.defaultFormatter": "yzhang.markdown-all-in-one"
  },
  "[yaml]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
```

Before you can get started working on contributions, you'll need a copy of the repository. The first step, done only once, is to fork the repository in GitHub to your personal account. The repository is located at <https://github.com/uabrc/uabrc.github.io>. More in-depth documentation on forking can be found at [GitHub: Fork a Repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

Once the fork has been created, you can clone your fork using the Command Palette (`ctrl + shift + p`) and `Git: Clone...` in VSCode, or at the command line. More information on cloning can be found at [GitHub: Cloning a Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

### Local Machine Setup

The Python extension will activate when you open any Python file. The file `test.py` has been added for convenience, simply open that file to activate the extension. The extension will show the currently activated environment near the bottom-left corner of the VSCode window.

Please create an Anaconda environment using `build_env.yml` using the following.

```shell
conda env create -f build_env.yml
```

Activate the environment in VSCode by clicking the currently activated environment in the bottom-left of the VSCode window. A menu will appear allowing you to select from discovered environments. You may need to reload VSCode to get the environment to appear if it was just created.

### GitHub Setup

To view your changes as they would appear on the official documentation website, you'll need to set up GitHub Pages in your fork. Navigate to your fork repository URL and click the "Settings" tab. Click "Pages" under "Code and automation". Follow the instructions here to set up a source: [GitHub Pages Docs](https://docs.github.com/en/pages).

### Workflow

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

#### File Organization

To Be Determined

#### Linting Known Issues

There are known issues with the markdown linter and some of our non-standard plugins, especially admonitions (specifically a conflict involving fenced vs indented code blocks). To fix these cases please use one of the following methods. The `<lint warning code>` can be found by hovering over the yellow squiggles in VSCode to bring up the warning lens.

To silence a linter warning for a block:

```markdown
<!-- markdownlint-disable <lint warning code> -->
`linter error here`

`maybe multiple lines`
<!-- markdownlint-enable <lint warning code> -->
```

Or for a single line:

```markdown
<!-- markdownlint-disable-next-line -->
`linter error here just for this line`
```

Please do not use these to silence all linter warnings, only for fixing known issues. Please read the warning lenses given by VSCode to identify the cause of the warning.

### Accessibility

Color vision deficiency checker: <https://www.toptal.com/designers/colorfilter/>

### Branding Guidance

- Brand main page: <https://www.uab.edu/toolkit/branding>
- Brand colors: <https://www.uab.edu/toolkit/brand-basics/colors>
- Copyright guidance: <https://www.uab.edu/toolkit/trademarks-licensing/uab-trademarks>
