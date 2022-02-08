# Basic Instance Setup

Instances are the basic unit of compute on OpenStack. Requesting an instance involves a number of steps, and requires that a `network<network_setup_basic>` has already been setup. It is also possible to attach persistent reusable `volumes<volume_setup_basic>` to instances.

## Creating a Floating IP

Floating IPs are required if you want an instance to talk to devices on the internet. These IPs are a shared resource, so they must be allocated when needed and released when no longer needed.

1. Click "Network" in the left-hand navigation pane to open the fold-out menu.

    ![image](./images/networks_000.png)

2. Click "Floating IPs".

    ![image](./images/floating_ips_001.png)

3. Click "Allocate IP to Project" to open a dialog box.

4. Fill out the dialog box.

    1. Select "uab-campus" in the "Pool" drop down box.
    2. Enter a "Description".
    3. Leave "DNS Domain" empty.
    4. Leave "DNS Name" empty.

    ![image](./images/floating_ips_002.png)

5. Click "Allocate IP".

    1. Redirects to the "Floating IPs" page.
    2. There should be a new entry in the table.

    ![image](./images/floating_ips_003.png)

## Creating a Key Pair

A Key Pair is required for SSH access to OpenStack instances for security reasons.

Using a password protected Key Pair is highly recommended for additional security, as it buys time to revoke a key if it is compromised by an attacker. Currently, this is only possible by uploading a custom public key generated on your local machine.

Good practice is to only use one key pair per person and per local machine. So if you have two computers, each one will need its own key pair. If you have two users, each will need their own key pair. Private keys are secrets and should not be passed around. Copying the key increases the risk of the system being compromised by an attacker.

1. Click "Compute" in the left-hand navigation pane to open the fold-out menu.

    ![image](./images/key_pairs_000.png)

2. Click "Key Pairs".

    ![image](./images/key_pairs_001.png)

3. Click "+ Create Key Pair" to open a dialog box.

4. Fill out the dialog box.

    1. Enter a "Key Pair Name".
    2. Select "SSH Key" in the "Key Type" drop down box.

        ![image](./images/key_pairs_002.png)

5. Click "+ Create Key Pair"

    1. Opens a download file dialog box in your browser to download a `pem` file containing the secret private key.
    2. Download the `pem` file. For security reasons this will be your only chance to ever obtain the private key from OpenStack.
    3. Failing to download the `pem` file now means a new key pair will need to be created.

        ![image](./images/key_pairs_003.png)

    4. Redirects to the "Key Pairs" page.
    5. There should be a new entry in the table.

        ![image](./images/key_pairs_004.png)

6. To use the private key on your local machine.

    1. `mv` the `pem` file to the `.ssh` directory under your home directory. If you are on a Windows machine, you'll need to install ssh by one of various means.
    2. `cd` to the `.ssh` directory under your home directory.
    3. `ssh-add <pem_file>` to add the private key to the ssh keyring for use by ssh.
    4. `ssh-add -d <pem_file>` to remove the key.

        ![image](./images/key_pairs_005.png)

!!! note

    It is alternately possible to use a custom key pair created on your local machine. We assume you know how to create a key pair on your local machine and have already done so. To upload a key pair, replace steps 3 and 4 above with the following, perform step 5 from above, and skip step 6.

    3. Click "Import Public Key" to open a dialog box.

    4. Fill out the dialog box.

        1. Enter a "Key Pair Name".
        2. Select "SSH Key" in the "Key Type" drop-down box.
        3. Click "Browse..." to upload a public key file from your custom
            key pair **OR** copy-paste the content of that key file into the
            "Public Key" box.

            ![image](./images/key_pairs_alt_002.png)

## Creating an Instance

Creating an instance is possibly a step you'll perform often, depending on your workflow. There are many smaller steps to create an instance, so please take care to check all the fields when you create an instance.

These instructions require that you've set up a `network<network_setup_basic>` and followed all of the instructions on the linked page. You should have a Network, Subnet, outer and SSH Security Group. You will also need to setup a
`Key Pair<Creating a Key Pair>` and a `Floating IP<Create a Floating IP>`.

1. Click "Compute" in the left-hand navigation pane to open the fold-out menu.

    ![image](./images/key_pairs_000.png)

2. Click "Instances".

    ![image](./images/instances_001.png)

3. Click "Launch Instance" to open a dialog box.

4. Fill out the dialog box completely. There are several tabs that will need to be completed.

    ![image](./images/instances_002.png)

5. "Details" tab.

    1. Enter an "Instance Name".
    2. Enter a "Description".
    3. Select "nova" in the "Availability Zone" drop down box.
    4. Select "1" in the "Count" field.
    5. Click "Next \>" to move to the "Source" tab.

6. "Source" tab. Sources determine what operating system or pre-defined image will be used as the starting point for your operating system (OS).

    1. Select "Image" in the "Select Boot Source" drop down box.
    2. Select "Yes" under "Create New Volume".
    3. Choose an appropriate "Volume Size" in `GiB`. Note that for many single-use instances, `20 GiB` is more than enough. If you need more because you have persistent data, please create a `persistent volume<volume_setup_basic>`.
    4. Select "Yes" or "No" under "Delete Volume on Instance Delete"
        1. "Yes" is a good choice if the OS volume will be reused.
        2. "No" is a good choice if you don't care about reusing the OS.

        ![image](./images/instances_003.png)

    5. Pick an image from the list under the "Available" section.
        1. Use the search box to help find the image that best suits your research needs.
        2. When you find the best image, click the button with an up arrow next to the image.
        3. The image will move to the "Allocated" section above the "Available" section.

        ![image](./images/instances_004.png)

    6. Click "Next \>" to move to the "Flavor" tab.

7. "Flavor" tab. Flavors determine what hardware will be available to your instance, including cpus, memory and gpus.

    1. Pick an instance flavor form the list under the "Available" section.
        1. Use the search box to help find the flavor that best suits your needs.
        2. When you find the best flavor, click the button with an up arrow next to the flavor.
        3. The flavor will move to the "Allocated" section above the "Available" section.

        ![image](./images/instances_005.png)

    2. Click "Next \>" to move to the "Networks" tab.

8. "Networks" tab. Networks determine how your instance will talk to the internet and other instances. See `networking<network_setup_basic>` for more information.

    1. Pick a network from the list under the "Available' section.
        1. A Network may already be picked in the "Allocated" section. If this is not the correct Network, use the down arrow next to it to remove it from the "Allocated" section. If the Network is correct, skip (ii.) through (iv.).
        2. Use the search box to help find the Network that best suits your needs.
        3. When you find the best Network, click the button with an up arrow next to the Network.
        4. The Network will move to the "Allocated" section above the "available" section.

        ![image](./images/instances_006.png)

    2. Click "Next \>" to move to the "Network Ports" tab.

9. "Network Ports" tab. *Coming Soon!*

    1. Leave this tab empty.

        ![image](./images/instances_007.png)

    2. Click "Next \>" to move to the "Security Groups" tab.

10. "Security Groups tab. Security Groups allow for fine-grained control
    over external access to your instance. For more information see
    `Creating a Security Group<network_setup_basic>` for more
    information.

    1. Pick the "ssh" Security Group from the "Available" section by
        pressing the up arrow next to it.
    2. The "default" Security Group should already be in the
        "Allocated" section.

        ![image](./images/instances_008.png)

    3. Click "Next \>" to move to the "Key Pair" tab.

11. "Key Pair" tab. Key Pairs allow individual access rights to the
    instance via SSH. For more information see `Creating a Key Pair`.

    1. Pick one or more key pairs from the list under the "Available"
        section.
        1. A Key Pair may already be picked in the "Allocated" section.
            If this is not the correct "Key Pair", use the down arrow
            next to it to remove it form the "Allocated" section. If the
            Key Pair is correct, skip (ii.) through (iv.).
        2. Use the search box to help find the Key Pair that best suits
            your needs.
        3. When you find the best Key Pair(s), click the button with an
            up arrow next to the Key Pair(s).
        4. The Key Pair(s) will move to the "Allocated" section above
            the "Available" section.

        ![image](./images/instances_009.png)

    2. Click "Next \>" to move to the "Configuration" tab.

12. "Configuration" tab. *Coming Soon!*

    1. Skip this tab.
    2. Click "Next \>" to move to the "Server Groups" tab.

13. "Server Groups" tab. *Coming Soon!*

    1. Skip this tab.
    2. Click "Next \>" to move to the "Scheduler Hints" tab.

14. "Scheduler Hints" tab. *Coming Soon!*

    1. Skip this tab.
    2. Click "Next \>" to move to the "Metadata" tab.

15. "Metadata" tab. *Coming Soon!*

    1. Skip this tab.

16. Click "Launch Instance" to launch the instance.

    1. Redirects to the "Instances" page.
    2. There should be a new entry in the table.

        ![image](./images/instances_014.png)

    3. The instance will take some time to build and boot. When the
        Status column entry says "Active" please move to the next steps.

        ![image](./images/instances_015.png)

17. Associate Floating IP.

    1. In the "Actions" column entry, click the drop down triangle and
        select "Associate Floating IP".
    2. A dialog box will open.
    3. Select an IP address in the "IP Address" drop down box.
    4. Select a port in the "Port to be associated" drop down box.
    5. Click "Associate" to return to the "Instances" page and
        associate the selected IP.

        ![image](./images/instances_017.png)

At this stage you should be able to SSH into your instance from on
campus or on the UAB VPN.

## SSH Into the Instance

If you are following the steps from top to bottom, then at this stage
you should be able to SSH into your instance from on campus or on the
UAB VPN. To do so be sure your local machine has ssh and then use the
following command If you are using a different operating system, such as
CentOS, replace the user `ubuntu` with `centos` or whatever is
appropriate.

``` bash
ssh ubuntu@<floating ip> -i ~/.ssh/<keypair_name>.pem
```

![image](./images/instances_020.png)
