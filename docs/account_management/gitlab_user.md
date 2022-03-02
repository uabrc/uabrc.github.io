# UAB GitLab Overview and Registration

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

## UAB GitLab Registration

### UAB-Affiliated Researcher Registration

If you are a UAB affiliated researcher and have a BlazerId, you may create an account by logging in at the site above using the `ldap` tab. Please use your single sign-on (SSO) credentials.

<!-- markdownlint-disable MD046 -->
!!! note "Please use BlazerID and password instead of UABMC credentials"

    Please use your BlazerID and BlazerID password for UAB GitLab. UABMC credentials are a different sign in system and will likely not work. Central IT groups like Research Computing do not have a way to access UABMC credentials.

![!gitlab login pane with ldap tab selected](images/gitlab_user_ldap.png)
<!-- markdownlint-enable MD046 -->

## UABMC Researcher Registration

Please use your BlazerID and BlazerID credentials to sign in following the directions for UAB-Affiliated Researchers. UABMC credentials should not be used for UAB GitLab.

## XIAS External Collaborator Registration

If you are a collaborator with a XIAS account you'll need to follow a different procedure.

1. Ensure that your sponsor has included `https://gitlab.rc.uab.edu` in the list of approved URIs on the XIAS configuration page.
2. Email support@listserv.uab.edu providing your full name, XIAS account email address, and sponsor.
3. UAB Research Computing will create the account.
4. You will recieve an email from gitlab.rc.uab.edu with a link to create a password.
5. Navigate to <https://gitlab.rc.uab.edu>.
6. Click the `Standard` tab.
7. In the `Username or email` field type the part of your XIAS email address before the `@` symbol. Do not include the `@` symbol or anything after it.
8. Fill out the `Password` field with the GitLab password you created in Step #4.
9. Click `Sign in`.

![!gitlab login pane with standard tab selected](images/gitlab_user_standard.png)

<!-- markdownlint-disable MD046 -->
!!! warning

    XIAS account researchers can only be granted access if their sponsor adds the GitLab URL to the list of approved URIs. Please see [XIAS Sites](xias_sites.md) for more information.
<!-- markdownlint-enable MD046 -->