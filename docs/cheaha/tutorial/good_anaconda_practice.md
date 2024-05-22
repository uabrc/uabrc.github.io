# Good Practice for finding Software on Anaconda Issue

Version pinning
Semantic Versioning

What would you like to see added?

To build an environment in Anaconda from scratch, first create a list of names for all the software you will need for your workflow.
Create a file env.yml and add the following (link to yml sections), replacing <> with appropriate values. We will fill out dependencies in the next section.
name: <my-env-name>

channels:
  - anaconda
  # - conda-forge
  # - bioconda
  # etc...
dependencies:
  # - <name>=<version>
  # - pip:  # for pypi packages
  #   - <name>==<version>
  #   for git repos
  #   - git+https://github.com/<user-or-org>/<repo>.git
  #   - git+https://gitlab.com/<user-or-group>/<repo>.git

OR

name: <my-env-name>

dependencies:
  # - <channel>::<name>=<version>
  # - pip:  # for pypi packages
  #   - <name>==<version>
  #   for git repos
  #   - git+https://github.com/<user-or-org>/<repo>.git
  #   - git+https://gitlab.com/<user-or-group>/<repo>.git

Then for each item on the list we will try to find it using Google. The main steps are to locate the package, verify it is up to date, then add it to our env.yml file. We will also add any channels as necessary, and take a special step if the package is on PyPi.

Priority for searching:
1. anaconda <name>.
2. conda-forge <name>.
3. bioconda <name>.
4. pypi <name>.

If we find the package at one of these sources, we can check the version of either noarch (if available) or linux. Noting the version, we can click the "source" or "repo" link (if available) or "homepage". Then we try to find the latest version. For GitHub, click "Releases" on the right-hand side. Verify that the latest Release is the same as, or very close to, the version on Anaconda or Pypi. If so, the package is being maintained on Anaconda/Pypi and suitable for use. Note the exact software name, version, and channel (if not on Pypi).
If we don't find it in any of those, or the Anaconda/Pypi pages are out of date, then we may not be able to use the software in an Anaconda environment. It is possible to try installing a git repository using pip, but care must be taken to choose the right commit or tag: https://pip.pypa.io/en/stable/cli/pip_install/#examples. To search for a git repository try:
6. github <name>.
7. gitlab <name>.
If the list is complete, then add all Anaconda channels to the channels: section. For Anaconda packages, add one line to dependencies for each software as - <name>=<version>. For Pypi packages add - pip: under dependencies. Then under - pip:add (indented)- ==. Refer to the template above for guidance on formatting. For git repos, add them under -pip:` based on examples here: https://pip.pypa.io/en/stable/cli/pip_install/#examples.

If you run into challenges please contact us via email <support@listserv.uab.edu>.
