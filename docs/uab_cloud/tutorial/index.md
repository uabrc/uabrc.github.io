# cloud.rc Tutorial

Welcome to the cloud.rc tutorial!

Through this tutorial we will show you how to use cloud.rc to create your very own VM for scientific research on our OpenStack cloud service. The tutorial works best if you read and follow the instructions carefully, and follow the steps in order.

<!-- markdownlint-disable MD046 -->
!!! note

    Virtual machines are disposable! If you get stuck at any point, or things don't seem like they're working as expected, etc., feel free to delete the instance and start over.
<!-- markdownlint-enable MD046 -->

## Prerequisites

To access cloud.rc, you must either be on the UAB Campus Network or the UAB Campus VPN.

Please visit <https://cloud.rc.uab.edu> to ensure you are able to access the site.

You will also need an account created for you by our team. If you believe you need an account but do not have one, please [Contact Us](../../index.md#how-to-contact-us).

## Tutorial Sections

1. [Network](networks.md) - To do anything meaningful with a VM, it will need to be accessible to you and any collaborators. To make it accessible, you will first need to construct a virtual network by which it can communicate with the UAB Campus Network and beyond. This section will show you how to set up a bare-minimum network configuration.
1. [Security](security.md) - Being able to communicate with the internet means we must take security precautions. This is not only good practice, but an [IT Policy requirement](https://www.uab.edu/it/home/policies). Some layers of security are enforced by how we've configured the cloud service. Your responsibility starts with ensuring the VM is only accessible on specific ports and by specific people. This section will show you how to do that.
1. [Instances](instances.md) - Now that we've got a secure network, we are ready to create an instance. Instances are the virtual computing devices used to do the scientific processing for your research. Your responsibility starts with selecting or designing the software you will use, understanding how to install and configure it correctly for your application, and how to use and troubleshoot it. We are not able to provide any support for software within virtual machines.
1. [Volumes](volumes.md) - Optionally, you can set up persistent storage volumes.

## Advanced Information

Once you have completed the tutorial, you might read over some of the following information to advance your understanding and facilitate usage of the tutorial.

- [Remote Access](../remote_access.md) - Different ways to access instances.
- [Installing Software](../installing_software.md) - Good practices and examples of installing common software.
- [Snapshots](../snapshots.md) - Creating reusable custom images based on VMs you've spent time configuring.
- [Make an instance accessible by the public Internet](../remote_access.md#make-instances-publicly-accessible-from-the-internet).
