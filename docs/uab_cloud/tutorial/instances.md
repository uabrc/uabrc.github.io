# Instance Setup and Tutorial

Instances are the basic unit of compute on cloud.rc. Requesting an instance involves a number of steps, and requires that a [Network](networks.md) has already been setup, along with certain [Security](security.md) settings and features. It is also possible to attach persistent reusable [Volumes](volumes.md) to instances.

<!-- markdownlint-disable MD046 -->
!!! important

    If you are viewing this page as part of the cloud.rc tutorial, please follow the steps in order from top to bottom. Ignore any sections on deleting or releasing resources unless you need to correct a mistake.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! note

    Virtual machines are disposable! If you get stuck at any point, or things don't seem like they're working as expected, etc., feel free to delete the instance and start over.
<!-- markdownlint-enable MD046 -->

## Creating an Instance

Creating an instance is possibly a step you'll perform often, depending on your workflow. There are many smaller steps to create an instance, so please take care to check all the fields when you create an instance.

These instructions require that you've set up a [Network](networks.md) and followed all of the instructions on the linked page. You should have a Network, Subnet, Router and Floating IP. You will also need to setup a
[Key Pair](security.md#creating-a-key-pair) and an [SSH Security Group](security.md#creating-a-security-group).

1. Click "Compute" in the left-hand navigation pane to open the fold-out menu.

    ![!cloud.rc Overview page.](./images/key_pairs_000.png)

1. Click "Instances".

    ![!cloud.rc Instances page. The Instances table is empty.](./images/instances_001.png)

1. Click "Launch Instance" to open a dialog box.
1. Fill out the dialog box completely. There are several tabs that will need to be completed.

    ![!Launch Instance dialog. The dialog form has multiple tabs on the left menu. The Details tab is selected. The Details dialog form is empty except the Instance Name is set to my_instance.](./images/instances_002.png)

### Details Tab

1. Enter an "Instance Name". See [Naming Conventions](../index.md#naming-conventions).
1. Enter a "Description".
1. Select "nova" in the "Availability Zone" drop down box.
1. Select "1" in the "Count" field.
1. Click "Next >" to move to the "Source" tab.

### Source Tab

Sources determine what operating system or pre-defined image will be used as the starting point for your operating system (OS).

1. Select "Image" in the "Select Boot Source" drop down box.
1. Select "Yes" under "Create New Volume".
1. Choose an appropriate "Volume Size" in `GB`. Note that for many single-use instances, `20 GB` is more than enough. If you need more because you have persistent data, please create a `persistent volume<volume_setup_basic>`.
1. Select "Yes" or "No" under "Delete Volume on Instance Delete"
    1. "Yes" is a good choice if you don't care about reusing the OS.
    1. "No" is a good choice if the OS volume will be reused.

    ![!Launch Instance dialog. The Source tab is selected.](./images/instances_003.png)

1. Pick an image from the list under the "Available" section.
    1. Use the search box to help find the image that best suits your research needs.
    1. When you find the best image, click the button with an up arrow next to the image.
    1. The image will move to the "Allocated" section above the "Available" section.

    ![!Launch Instance dialog. The Source tab is selected. An Ubuntu 20.04 image has been moved up from the available images list to the allocated images list.](./images/instances_004.png)

1. Click "Next >" to move to the "Flavor" tab.

### Flavor Tab

Flavors determine what hardware will be available to your instance, including cpus, memory and gpus.

1. Pick an instance flavor form the list under the "Available" section.
    1. Use the search box to help find the flavor that best suits your needs.
    1. When you find the best flavor, click the button with an up arrow next to the flavor.
    1. The flavor will move to the "Allocated" section above the "Available" section.

    ![!Launch Instance dialog. The Flavor tab is selected.](./images/instances_005.png)

1. Click "Next >" to move to the "Networks" tab.

### Networks Tab

Networks determine how your instance will talk to the internet and other instances. If you are following along with the tutorial, you should already have a Network set up. See [Network](networks.md) for more information.

1. Pick a network from the list under the "Available' section.
    1. A Network may already be picked in the "Allocated" section. If this is not the correct Network, use the down arrow next to it to remove it from the "Allocated" section. If the Network is correct, skip (ii.) through (iv.).
    1. Use the search box to help find the Network that best suits your needs.
    1. When you find the best Network, click the button with an up arrow next to the Network.
    1. The Network will move to the "Allocated" section above the "available" section.

    ![!Launch Instance dialog. The Networks tab is selected.](./images/instances_006.png)

1. Click "Next >" to move to the "Network Ports" tab.

### Network Ports Tab

1. Leave this tab empty.

    ![!Launch Instance dialog. The Network Ports tab is selected. The dialog form has been left empty.](./images/instances_007.png)

1. Click "Next >" to move to the "Security Groups" tab.

### Security Groups Tab

Security Groups allow for fine-grained control over external access to your instance. If you are following along with the tutorial, you should already have an "ssh" Security Group set up. For more information see [Creating a Security Group](security.md#creating-a-security-group) for more information.

1. Pick the "ssh" Security Group from the "Available" section by pressing the up arrow next to it.
1. The "default" Security Group should already be in the "Allocated" section.

    ![!Launch Instance dialog. The Security Groups tab is selected. The ssh security group has been moved up from the available list to the allocated list.](./images/instances_008.png)

1. Click "Next >" to move to the "Key Pair" tab.

### Key Pair Tab

Key Pairs allow individual access rights to the instance via SSH. If you are following along with the tutorial, you should already have a key pair set up. For more information see [Creating a Key Pair](security.md#creating-a-key-pair).

1. Pick one or more key pairs from the list under the "Available"
    section.
    1. A Key Pair may already be picked in the "Allocated" section. If this is not the correct "Key Pair", use the down arrow next to it to remove it form the "Allocated" section. If the Key Pair is correct, skip (ii.) through (iv.).
    1. Use the search box to help find the Key Pair that best suits your needs.
    1. When you find the best Key Pair(s), click the button with an up arrow next to the Key Pair(s).
    1. The Key Pair(s) will move to the "Allocated" section above the "Available" section.

    ![!Launch Instance dialog. The Key Pair tab is selected. The Key Pair my_key_pair has been moved up from the available list to the allocated list.](./images/instances_009.png)

1. Click "Next >" to move to the "Configuration" tab.

### Configuration Tab

1. Skip this tab.
1. Click "Next >" to move to the "Server Groups" tab.

### Server Groups Tab

1. Skip this tab.
1. Click "Next >" to move to the "Scheduler Hints" tab.

### Scheduler Hints Tab

1. Skip this tab.
1. Click "Next >" to move to the "Metadata" tab.

### Metadata Tab

1. Skip this tab.

### Launching the Instance

Click "Launch Instance" to launch the instance.

1. Redirects to the "Instances" page.
1. There should be a new entry in the table.
1. The instance will take some time to build and boot. When the
    Status column entry says "Active" please move to the next steps.

    ![!The task column of the Instances table reads none indicating the instance is ready for use.](./images/instances_015.png)

### Associate a Floating IP

If you are following along with the tutorial, you should already have a floating IP set up.

1. In the "Actions" column entry, click the drop down triangle and select "Associate Floating IP".
1. A dialog box will open.
1. Select an IP address in the "IP Address" drop down box.
1. Select a port in the "Port to be associated" drop down box.
1. Click "Associate" to return to the "Instances" page and associate the selected IP.

    ![!Manage Floating IP Associations dialog. The form is filled out. The Floating IP Address created earlier is selected under IP Address. The port from the Instance my_instance is selected under Port to be Associated.](./images/instances_017.png)

## Instances Failing to Start

There are a number of reasons an instance might fail. We are able to provide direct support for instances which fail to start for reasons outside the instance itself. To help us correct the error, you'll need to have information from the instance page. Below is an example of a failed instance in the "Instances" table, helpfully named `failed_instance`. Note the "Error" label under the "Status" column.

![!failed instance in instances table](images/instance_failed_001.png)

In the "Instances" table, click the name of your failed instance. You should see a page like below, with some basic metadata about the instance as well as a "Fault" section.

![!failed instance overview page showing id and fault reason](images/instance_failed_002.png)

We will need to "ID" and the reason for the fault. In this case, the instance failed because it could not allocate a GPU, as all GPUs were allocated at the time of its creation. It is not possible to diagnose the specifics without consulting us, so please feel free to contact [Support](../../help/support.md).

Instances can fail for other reasons as well, please contact [Support](../../help/support.md) with the "ID" and "Fault" information.

For instances which fail due to internal reasons, i.e. while using SSH or an application, we are still able to provide support but it will have to be on a case-by-case basis. Be prepared to walk us through the steps you took to set up the instance and any software, as well as any data processing steps, leading up to the failure.

## SSH Into the Instance

If you are following the tutorial, then at this stage you should be able to SSH into your instance from the UAB Campus Network or on the UAB Campus VPN. You will need to [Install an SSH Client](../remote_access.md#install-an-ssh-client) Once your machine has an ssh client, use the following command. If your image uses an operating system other than Ubuntu, such as CentOS, replace the user `ubuntu` with `centos` or whatever is appropriate. The value `<floating ip>` should be whatever IP was assigned in [Creating a Floating IP](networks.md#creating-a-floating-ip), and the value `<private_key_file>` should be whatever your key pair file was named from [Creating a Key Pair](security.md#creating-a-key-pair).

1. [Install an SSH Client](../remote_access.md#install-an-ssh-client) to use SSH from your local machine to your cloud instance.
1. [Manage Your Private Key](../remote_access.md#managing-keys)
    - [Start the SSH Agent](../remote_access.md#starting-the-ssh-agent-for-a-single-session) to enable your system to remember your private key.
    - [Add a Private Key](../remote_access.md#add-a-private-key) to the ssh agent to remember it for future use.
1. [Verify the SSH Client Works](../remote_access.md#ssh-client-usage). Use the following command to connect

    ``` bash
    ssh ubuntu@<floating ip> -i ~/.ssh/<private_key_file>
    ```

    - If your image uses an operating system other than Ubuntu, such as CentOS, replace the user `ubuntu` with `centos`, or whatever may be appropriate.
    - The value `<floating ip>` should be whatever IP was assigned in [Creating a Floating IP](networks.md#creating-a-floating-ip).
    - The value `<private_key_file>` should be whatever your key pair file was named from [Creating a Key Pair](security.md#creating-a-key-pair).

    ![!MINGW64 terminal on Windows. The ssh command has been used to login to the Floating IP Address using the -i command with the locally stored private key my_key_pair.pem. Login was successful. A banner page has been shown and a terminal prompt is waiting for input.](./images/instances_020.png)

1. (optional, but helpful) [Set Up a Configuration File](../remote_access.md#setting-up-a-configuration-file) to simplify the command used to make a connection.

<!-- markdownlint-disable MD046 -->
!!! note

    Reusing a floating IP for a new instance can result in a "Remote Host Identification Has Changed" error, preventing connection. Please see [Remove an Invalid Host Fingerprint](../remote_access.md#remove-an-invalid-host-fingerprint).
<!-- markdownlint-enable MD046 -->

### Streamlining SSH

Refer to [Setting up a Configuration File](../remote_access.md#setting-up-a-configuration-file) in [Cloud Remote Access](../remote_access.md).

## Next Steps

Now you are ready to [Install Software](../installing_software.md), set up [Security Groups](security.md#creating-a-security-group) for [Servers](../installing_software.md#installing-server-software), and optionally [Create a Persistent Volume](volumes.md).

## Deleting an Instance

<!-- markdownlint-disable MD046 -->
!!! note

    Deleting Instances is not part of the tutorial, and is here as a reference.
<!-- markdownlint-enable MD046 -->

To delete an instance, return to the "Instances" page using the left-hand navigation pane. In the table, find the row with the instance you wish to delete, and click the drop-down arrow under "Actions" in that row. Then click "Delete Instance" to open a confirmation dialog.

![!Delete instance entry highlighted in table row actions drop down menu.](./images/delete_instance_001.png)

Click "Delete Instance" again to delete the instance permanently.

![!Delete instance confirmation dialog.](./images/delete_instance_002.png)

<!-- markdownlint-disable MD046 -->
!!! Warning

    It is highly recommended to shut off an instance before deleting it.
<!-- markdownlint-enable MD046 -->

## Help My Instance Is Stuck or Not Working

If your instance is stuck or otherwise not working as expected, first try deleting it and starting over. If you are unable to delete it or it gets stuck while deleting, please contact [Support](../../help/support.md) and copy the the instance ID as shown below.

### Where Is My Instance ID?

To find your instance ID, navigate to the "Instances" table. Click the "Instance Name" for the instance you are interested in to load an information page for that instance.

![!instance table with instance highlighted by mouse](../images/instance-id-001.png)

In the instance information page, navigate to the "Overview" tab. Near the top is a field labeled "ID". The value to the right of "ID" is a Universally Unique ID (UUID) which uniquely names your instance. We need that ID to delete a stuck instance, so please provide it when requesting cloud.rc instance support.

![!instance information overview tab with ID highlighted](../images/instance-id-002.png)

## Continuing the Tutorial

Now that you have set up a [Network](networks.md), [Security Policies](security.md) and an [Instance](instances.md), you are done with the tutorial, congratulations! There is one remaining optional step. If you need a persistent data volume to move between instances, please check our [Volumes](volumes.md) page.
