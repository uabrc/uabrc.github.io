# UAB GitLab Account Management

Welcome to UAB GitLab! This is a UAB-specific [GitLab](https://about.gitlab.com/). GitLab is similar to [GitHub](https://github.com/), but hosted here at UAB on secure servers.

## GitLab Use Cases

### For Researchers

GitLab can be used:

- For reproducibility
    - Analysis and software code can be kept in one, central repository everyone can use instead of spread across multiple computers/places.
    - Code can be versioned and tracked as it changes over time.
    - Software versions can be recorded, virtual environments can be documented, and containers can be recorded to help future-proof analyses.
- Collaboration
    - GitLab is a central place to create code, edit, and track needed code changes (issues) with your lab and collaborators.
    - Multiple people can use, modify, and merge changes in code while communicating with the broader team all along the way.
- Security
    - Unlimited private repositories for internal code projects.
    - Set behind UAB authentication.

### For Software Developers (and Researchers!)

UAB GitLab is useful for software developers. It is a single application for the entire software development lifecycle. From project planning and source code management to continuous integration (CI) and continuous deployment (CD), monitoring, and security.

Our GitLab instance may be found at <https://gitlab.rc.uab.edu>.

## Creating a New Account

Please choose the subsection below that matches how you are associated with UAB.

### UAB Campus or UAB Medicine (UABMC) Affiliated

Authenticate with your BlazerID credentials under the `ldap` tab at <https://gitlab.rc.uab.edu>. UABMC credentials are not supported.

![!gitlab login pane with ldap tab selected](./images/gitlab_researcher_ldap.png)

<!-- markdownlint-disable MD046 -->
!!! note "Please use BlazerID and password instead of UABMC credentials"

    Please use your BlazerID and BlazerID password for UAB GitLab. UABMC credentials are a different sign in system and will likely not work. Central IT groups like Research Computing do not have a way to access UABMC credentials.
<!-- markdownlint-enable MD046 -->

### XIAS External Collaborator

If you are a collaborator with a XIAS account you'll need to follow the procedure below. If you do not have an account, first please visit our [XIAS page](xias/index.md) and follow the instructions there.

1. Communicate with your sponsor to ensure that `https://gitlab.rc.uab.edu` is included in the list of approved URIs. If they are unsure of what this means, please direct them to our [XIAS PI Site Management page](xias/pi_site_management.md).
2. Email <support@listserv.uab.edu> providing your full name, your XIAS account email address, and your sponsor's full name.
3. UAB Research Computing will create the account.
4. You will recieve an email from <https://gitlab.rc.uab.edu> with a link to create a password.
5. Navigate to <https://gitlab.rc.uab.edu>.
6. Click the `Standard` tab.
7. In the `Username or email` field type the part of your XIAS email address before the `@` symbol. Do not include the `@` symbol or anything after it.
8. Fill out the `Password` field with the GitLab password you created in Step #4.
9. Click `Sign in`.

![!gitlab login pane with standard tab selected](./images/gitlab_researcher_standard.png)

<!-- markdownlint-disable MD046 -->
!!! warning

    XIAS account researchers can only be granted access if their sponsor adds the GitLab URL to the list of approved URIs. Please see our [XIAS PI Site Management page](./xias/pi_site_management.md) for more information.
<!-- markdownlint-enable MD046 -->
