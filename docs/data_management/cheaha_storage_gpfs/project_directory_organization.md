# Project Directory Organization

Effective research data management starts with a well organized directory structure, especially for researchers working on multiple projects under shared allocations. A well organized project directory structure ensures scalability, simplifies collaboration, and makes it easier to manage permissions.

To maintain long-term organization, create a new subdirectory each time your group begins a distinct project. Assign [permissions](#permissions-and-access-control) based on access needs to ensure security while allowing collaboration.

Below is a recommended directory structure to help keep project files, shared research data, and software environments organized within shared allocations on Cheaha.

1. Top-Level Directory

    Suppose the top-level directory is your lab Cheaha project directory, `/data/project/mylab/`.

1. Projects' Directory

    Each project gets its own subdirectory. This keeps things organized and isolated from one another, making it easier to manage and avoid confusion.

    Example:

    ```bash
    /data/project/mylab/project/
    |-- project-1/
    |-- project-2/
    |-- project-3/
    ```

1. Repositories

    If your projects rely on code or software tools that are used across multiple efforts, you can set up a repository directory for shared scripts, tools, or utilities.

    Example:

    ```bash
    /data/project/mylab/repository/
    |-- common-software-tool-1/
    |-- common-software-tool-2/
    ```

1. Shared Research Data

    Having a separate directory for research data that is common across projects helps prevent duplication and ensures that everyone is working with the same dataset.

    Example:

    ```bash
    /data/project/mylab/common-data/
    |-- some-data-used-by-multiple-projects/
    |-- other-shared-data/
    ```

1. Environments

    For projects that require specific software environments (e.g., Conda environments), you can centralize these in a separate directory. This way, you ensure that everyone is using the right tools.

    Example:

    ```bash
    /data/project/mylab/environments/
    |-- shared-conda-env-1.yml
    |-- shared-conda-env-2.yml
    ```

To provide a clearer picture, here is how all the components fit together in the overall structure:

```bash
/data/project/mylab/
|-- project/
|   |-- project-1/
|   |-- ...
|-- repository/
|   |-- common-software-tool-1/
|   |-- ...
|-- common-data/
|   |-- some-data-used-by-multiple-projects/
|   |-- ...
|-- environments/
|   |-- shared-conda-env-1.yml
|   |-- ...
```

## Permissions and Access Control

Permissions for each directory can be managed by either being a member of the group associated with the top-level project directory or by using [Linux permissions](../cheaha_storage_gpfs/index.md#project-directory-permissions) or [Access Control Lists (ACLs)](../../workflow_solutions/shell.md#manage-researcher-access-to-files-and-directories-getfacl-setfacl). Managing proper permissions ensures that team members can access only the resources they need, while protecting sensitive data.

If you plan managing multiple projects and would like assistance with organizing your project directories or managing permissions, please send us a [support ticket](../../help/support.md#how-do-i-create-a-support-ticket).
