# Code.rc (GitLab)

## What Is Code.rc?

**Code.rc** is the Research Computing System (RCS) on-premises GitLab server.

## Why Use Code.rc?

Code.rc has features supporting:

- Accountability
    - Track who is responsible for what aspects of project work.
    - Issue tracking and deadlines.
    - Calendars.
    - Project organization via Groups.
- Collaboration
    - Issue tracking with discussions, due dates, cross-linking, and kanban boards.
    - Access control via Roles and Groups.
    - Automation via continuous integration and continuous deployment (CI/CD).
    - Organize workflows among multiple collaborators.
    - Wiki pages.
- Reproducibility
    - Code and project definitions can be kept in a single, central repository
    - The repository serves as a reference for other researchers.
    - Code changes are tracked as a project evolves.
- Security
    - Hosted at UAB Campus.
    - Requires UAB Campus credentials to access.

## What Are Groups, Projects, and Roles?

Managing roles and user permissions within GitLab is essential for maintaining control over repositories and collaboration. Within GitLab, a user (Owner) can assign and update user roles in a group. There are several roles for users within GitLab, and these roles determine the level of permissions a user will have within a Group or project. In GitLab, permissions are organized in a hierarchical group/project tree structure. At the top is a Group, which can contain subgroups and individual projects. This structure makes permission control easy to manage. Groups can represent schools, faculty, departments, labs or cores, while projects hold the actual code, issues, and CI/CD configurations for grants and research they administer.

The available default roles within a group/project are listed in the table;

{{ read_csv('_res/gitlab_roles.csv', keep_default_na=False) }}

A user assigned the "Guest" role has the least permissions, and the "Owner" has the most permissions. The table summarizes key features and permissions per user role in a Group/Project. For a complete list of permissions each role can perform, please see [GitLab documentation for user permissions](https://docs.gitlab.com/user/permissions/). In the section [Assigning a User's GitLab Role](#how-do-i-assign-gitlab-roles), you will see a guide to create, and assign user roles within your GitLab project.

## Why Are Groups, Projects, and Roles Important?

GitLab’s Group and Project structure offers a powerful way to mirror how your research lab or programs are structured. When we consider the organizational setup at UAB, where a Core oversees several specialized Labs. Each lab is led by a different PI, researcher or department. Within each Lab, multiple projects are being run, possibly by different teams, postdocs, or students. GitLab’s inheritance Group to Project model, shows Groups can contain subgroups and projects, making it possible to organize this exact structure digitally (Core->Lab/Department->Projects). The Core entity at UAB can be represented as a top-level group, each Lab as a subgroup, and individual projects (e.g., datasets, analysis pipelines, or software tools) as repositories within those subgroups.

This structure helps to maintain a clear navigation system, it also ensures efficient role and permission management. The Core can assign high-level oversight roles at the Group level, while Labs can manage their own subgroups independently. Developers and researchers can be granted access only to the projects they work on, without exposing unrelated projects or sensitive data they should not have access to, adhering to the principle of least privilege. Combined with GitLab’s role inheritance and ability to override roles at lower levels, this design promotes scalability, security, and accountability, while supporting collaborative research across a complex institutional environment like UAB.

## How Do I Assign GitLab Roles?

In GitLab, only a user with the role "Owner" can assign or change a GitLab role for a user across "Projects" or "Groups". Whereas, a "Maintainer" has project-level privileges and can only manage users that are part of a "Project" within a "Group", the "Owner" has group-wide privileges that extend to the "Projects" under their "Group". Remember, for a User to be added to a Group, they would need to have a Code.rc account set up. Please see the [Code.rc Account Creation](../account/code.rc/create.md) page for setting one up.

The following instructions are to guide you in creating a group and/or assigning user roles as a group owner.

### Creating a GitLab Group

1. Log in to [Code.rc](https://code.rc.uab.edu/users/sign_in) using your UAB Credentials.

    ![!image showing UAB RC GitLab Landing Page](_img/uab-gitlab-landingpage.png)

1. Click on the "Groups" menu option.

    ![!image showing Logged-in interface](_img/uab-gitlab-group1.png)

1. Select "New group".

    ![!image showing Groups a user has access to on GitLab, with the New group button highlighted](_img/uab-gitlab-group2.png)

1. Now select the "Create group" option. You may select the "Import group" option, if you have projects and their associated data from other Git hosting services. For this guide, we are assuming this is not the case, and you are setting up a new Group.

    ![!image showing the Create group and Import group option, with the Create group option highlighted](_img/uab-gitlab-creategrp.png)

1. Fill out the form to create your group, make sure to include a name, and appropriate "Visibility level". There are three (3) levels for visibility, pick the option meeting your needs. Click on the "Create group" option, and this completes the Group creation process.

    ![!image showing the form to Create group, with the Group name, Visibility level and Create group options highlighted](_img/uab-gitlab-creategrp2.png)

    <!-- markdownlint-disable MD046 -->
    !!! note

        GitLab allows you to define Group visibility using "Public", "Internal", or "Private" settings. A public Group is visible to and can be cloned by anyone, even without a Code.rc account. An internal Group is visible to any authenticated Code.rc user, but access to contribute is still controlled by roles. A private Group is only visible and accessible to users who have been explicitly granted access. These settings work in tandem with permissions to control both who sees what and what they can do in a Group. See [GitLab documentation](https://docs.gitlab.com/user/public_access/) for more information.
    <!-- markdownlint-enable MD046 -->

1. Now that your group has been created, we can [add users with varying roles](#add-and-assign-user-roles-within-a-group-or-project) that grant different user permissions.

    ![!image showing a list of Groups](_img/uab-gitlab-grplist.png)

### Creating a GitLab Project

As a Maintainer or Owner you can create Projects from within a Group. Steps 1 and 2 are same as the instructions for [Creating a Group](#creating-a-gitlab-group), there is a slight deviation at the third step.

1. Log in to [Code.rc](https://code.rc.uab.edu/users/sign_in) using your UAB Credentials.

    ![!image showing UAB RC GitLab Landing Page](_img/uab-gitlab-landingpage.png)

1. Click on the "Groups" menu option. And select the appropriate Group.

    ![!image showing Logged-in interface](_img/uab-gitlab-grouptest.png)

1. From within the group, Select "New project".

    ![!image showing Groups a user has access to on GitLab, with the New group button highlighted](_img/uab-gitlab-projectgroup.png)

1. Now select from one of the options to create new project, in this example we use the "Create blank project" option. You may select the "Import project" option, or "Create from template" option. For this guide, we are assuming this is not the case, and you are setting up a new Project.

    ![!image showing the Create new Project options, with the Create group option highlighted](_img/uab-gitlab-createproject.png)

1. Fill out the form to create your Project, make sure to include a name, and appropriate "Visibility level". There are three (3) levels for visibility, pick the option meeting your needs. Click on the "Create project" option, and this completes the Project creation process.

    ![!image showing the form to Create project, with the Project name, Visibility level and Create project options highlighted](_img/uab-gitlab-createproject2.png)

    <!-- markdownlint-disable MD046 -->
    !!! note

        GitLab allows you to define project visibility using "Public", "Internal", or "Private" settings like in a group. A public project is visible to and can be cloned by anyone, even without a Code.rc account. An internal project is visible to any authenticated Code.rc user, but access to contribute is still controlled by roles. A private project is only visible and accessible to users who have been explicitly granted access. These settings work in tandem with role-based permissions that control who can see what and what they can do in a project. See [GitLab documentation](https://docs.gitlab.com/user/public_access/) for more information.
    <!-- markdownlint-enable MD046 -->

1. Now that your project has been created, we can [add users with varying roles](#add-and-assign-user-roles-within-a-group-or-project) that grant different user permissions. To see members in your project, select the "Manage" option  and then select the "Members" option. This will take you to the list of members who are part of that project.

    ![!image showing the list of Members in a Project](_img/uab-gitlab-projectlist.png)

### Add and Assign User Roles Within a Group or Project

1. Click on the Group/Project, you have requisite permissions to (Owner for Groups, Owner or Maintainer for Projects). From within your Group/Project, click on the "Manage" pane located to the left of your Group/Project. And then click on "Invite members". If you are already part of another Group, dependent on the permissions you have in those Groups, you may be able to add all members of a Group with the "Invite a group" option, but for this guide, we are focusing on the "Invite members" option.

    ![!image showing Members list of a Group in GitLab, with the "Manage", "Members", "Invite a group" and "Invite members" options highlighted](_img/uab-gitlab-invitemembers.png)

    <!-- markdownlint-disable MD046 -->
    !!! note

        Please note, GitLab follows a "Group to Project" inheritance model, where a user added to a Group, would inherit that same role, when a new Project is created unless that role is changed. For instance, a user maybe assigned a Guest role at the Group level, but may have a higher role assigned at the project level.
    <!-- markdownlint-enable MD046 -->

1. The "Invite members" option, would open up to a mini window that shows an interface to invite members with their "Username, name or email address", an option to "Select a role", an option that allows you to set "Access expiration date" for a user, and the "Invite" button.

    ![!image showing options from selecting "Invite members"](_img/uab-gitlab-invitemembers2.png)

    The option "Select a role" is where you select what kind of role, you want the listed user(s) to have. Please refer to the [Groups, Projects, and Roles section](#what-are-groups-projects-and-roles) to see what each user role has permissions to do within your Group/Project.

    ![!image showing Roles available from the "Select a role" option](_img/uab-gitlab-invitemembers3.png)

    <!-- markdownlint-disable MD046 -->
    !!! note

        You can only add uab.edu entities or domain emails to Code.rc, you will get an error like in the image below if you do otherwise. Please see our page on [Code.rc Registration](../account/code.rc/create.md) to address adding external collaborators before attempting the prior steps.

    ![!image showing error from adding non-UAB email or entities](_img/uab-gitlab-domaindiff.png)
    <!-- markdownlint-enable MD046 -->

1. Now you can see a list of Group/Project members, showing their "Account" i.e. their Name and BlazerID, their "Source" i.e. how they joined the group, their "Role" i.e. level of permission within your Group, and "Expiration" i.e. how long they will have access to the group, unless this is changed, the default option is for a user to have access indefinitely. In this guide, one of the user's has an expiration of `2025-04-14`, after this date the user will no longer have access to your Group/Project. In the last column we have "Activity" i.e. additional metadata for the user.

    ![!image showing members in a Group](_img/uab-gitlab-grpmembers.png)

    You can also remove a user from your Group/Project, by clicking on the "More actions" button, the three (3) vertical lines to the right of an Account, and click the "Remove member" option.

    <!-- markdownlint-disable MD046 -->
    !!! note

        To manage security risks please apply the principle of Least Privilege when assigning roles. The principle states that users should be given the minimum level access to perform their roles. This is to mitigate security risks and operational errors. This principle ensures you limit members of your Group who can intentionally or unintentionally make destructive or irrevocable changes.
    <!-- markdownlint-enable MD046 -->

1. You can also change or update a user's role, by selecting one of the other options provided under the "Role" column for an Account. This changes the user's role within the Group/Project.

    ![!image showing roles a member can be changed to or updated to in a Group](_img/uab-gitlab-updaterole.png)
