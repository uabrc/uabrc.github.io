# UAB Cloud

Our [cloud.rc](https://dashboard.cloud.rc.uab.edu) portal, based on [OpenStack](https://www.openstack.org/) cloud software, provides a home for more permanent research applications such as web pages and database hosting, as well as a place where researchers can more fluidly develop applications for high performance compute.

Resource quotas are set to ensure that every researcher has a fair share. Please be sure to free up resources when they are no longer needed by deleting instances and volumes.

Currently, access to cloud.rc must be made while on the UAB Campus Network or on the UAB Campus Virtual Private Network (VPN). For more information about using the UAB Campus VPN, please visit [VPN - UAB IT](https://www.uab.edu/it/home/tech-solutions/network/vpn).

To get started using cloud.rc, please navigate to <https://dashboard.cloud.rc.uab.edu/>. A view of the dashboard is shown below.

![!cloud.rc dashboard](images/introduction.png)

To get the most out of cloud.rc, you'll want to make sure you have a working familiarity with the [Linux terminal](../workflow_solutions/shell.md).

Cloud.rc runs on Openstack. If you are new to Openstack or to cloud.rc, it is highly recommended to follow our tutorial to learn how to set up all of the necessary components of a virtual machine (VM) setup. In the tutorial we cover:

1. [Networks](network_setup_basic.md)
2. [Security Policies](security_setup_basic.md)
3. [Instances](instance_setup_basic.md)
4. [Volumes](volume_setup_basic.md) (optional)

The tutorial is intended to be followed in this order. Doing it out of order may result in errors and issues. If you encounter any unexpected issues, unclear instructions or have questions or comments, please contact [Support](../help/support.md). Otherwise, feel free to start the tutorial with [Networks](network_setup_basic.md).

## Naming Conventions

Entities on cloud.rc must be named a certain way or difficult-to-diagnose errors may occur. Entities includes instances, volumes, networks, routers, and anything else that you are allowed to give a name to.

Please use the following rules when naming entities:

- Must: use only letters, numbers, dash `-` and underscore `_`.
- Must: have the first character in the name be a letter.
- Should: use short, descriptive, memorable names.