# Network Setup and Tutorial

Networking setup should be a one-time setup. While Floating IPs fall under the Networking fold-out, they should be allocated and released together with instances to maximize security.

<!-- markdownlint-disable MD046 -->
!!! important

    If you are viewing this page as part of the cloud.rc tutorial, please follow the steps in order from top to bottom. Ignore any sections on deleting or releasing resources unless you need to correct a mistake.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! note

    Virtual machines are disposable! If you get stuck at any point, or things don't seem like they're working as expected, etc., feel free to delete the instance and start over.
<!-- markdownlint-enable MD046 -->

## Networks

### Creating a Network

1. Click "Network" in the left-hand navigation pane to open the fold-out menu.

    ![!cloud.rc Overview page. Networks is selected in the Network Topology fold-out menu in the left-hand navigation pane.](./images/networks_000.png)

1. Click "Networks" in the fold-out menu.

    1. The "Networks" page will open.
    1. The "uab_campus" network entry should already be in the table.

        ![!cloud.rc Networks page. The Networks table has one entry. The entry is the default, persistent uab-campus network.](./images/networks_001.png)

1. Click "+ Create Network" to open a dialog box.

1. Fill out the dialog box. Only the "Network" tab is important, we
    will create a subnet as a separate step.

    1. Enter a "Network Name". See [Naming Conventions](../index.md#naming-conventions).

    1. Leave "Enable Admin State" checked.

    1. Uncheck "Create Subnet". We will do this as a separate step. The other tabs should be removed.

    1. Leave the "Availability Zone Hints" box empty.

        ![!Create Network dialog. The dialog form is empty except Network Name has been set to my_network.](./images/networks_003.png)

1. Click "Create".

    1. Redirects to the "Networks" page.
    1. There should be a new entry in the table with the name given in (4.a)

        ![!cloud.rc Networks page. There is an additional entry in the table. The new entry is my_network.](./images/networks_004.png)

### Deleting a Network

<!-- markdownlint-disable MD046 -->
!!! note

    Deleting Networks is not part of the tutorial, and is here as a reference.
<!-- markdownlint-enable MD046 -->

To delete a network, return to the "Networks" page using the left-hand navigation pane. In the table, find the row with the network you wish to delete, and click the drop-down arrow under "Actions" in that row. Then click "Delete Network" to open a confirmation dialog.

![!Delete network entry highlighted in table row actions drop down menu.](./images/delete_network_001.png)

Click "Delete Network" again to delete the network permanently.

![!Delete network confirmation dialog.](./images/delete_network_002.png)

<!-- markdownlint-disable MD046 -->
!!! important

    You will not be able to delete the network if it has a [subnet](#subnets) with any connected [routers](#routers) or ports. They will need to be removed or deleted first.
<!-- markdownlint-enable MD046 -->

## Subnets

### Creating a Subnet

1. Click "Network" in the left-hand navigation pane to open the fold-out menu.

    ![!cloud.rc Overview page. Networks is selected in the Network Topology fold-out menu in the left-hand navigation pane.](./images/networks_000.png)

1. Click "Networks" in the fold-out menu.

    1. The "Networks" page will open.

    1. The "uab_campus" network should already be an entry in the table.

    1. At least one other entry must be in the table. See `Creating a Network`.

        ![!cloud.rc Networks page. There are two entries in the table. One is the default, persistent uab-campus network. The other is my_network.](./images/networks_004.png)

1. Under the "Actions" column, select the drop-down triangle button in the row corresponding to the network you want to add a subnet to.

    ![!Drop-down box under the Actions column in the my-network row of the Networks table. The drop-down box has been clicked, revealing two options. The selected option is Create Subnet.](./images/subnet_002.png)

1. Click "Create Subnet" in the drop-down to open a dialog box.

1. Fill out the dialog box.

    1. The "Subnet" tab.

        1. Enter a "Subnet Name". See [Naming Conventions](../index.md#naming-conventions).

        1. Enter `192.168.0.0/24` as the "Network Address". The trailing `/24` allocates the entire range from `192.168.0.0` through `192.168.0.255` to the subnet.

        1. Ensure "IPv4" is selected in the "IP Version" drop-down box.

        1. Leave "Gateway IP" empty to use the default value of `192.168.0.0`.

        1. Leave "Disable Gateway" unchecked.

        1. Click the "Next \>\>" button to move to the "Subnet Details" tab.

            ![!Create Subnet dialog box. The Subnet tab is selected. The form has not been filled out beyond default values. The Subnet Name has been set to my_subnet.](./images/subnet_003.png)

        <!-- markdownlint-disable MD046 -->
        !!! note

            If you receive an error like

            ```
            Failed to create subnet `192.168.0.0/24`...
            Invalid input for operation: Gateway is not valid on a subnet.
            ```

            Try changing the gateway IP address to `192.168.0.1` and trying again.
        <!-- markdownlint-disable MD046 -->

    1. The "Subnet Details" tab.

        1. Leave "Enable DHCP" checked.
        1. Enter `192.168.0.20,192.168.0.100` in the "Allocation Pools" box. The IP addresses in that range will be assigned to instances on this subnet.
        1. Leave "DNS Name Servers" empty.
        1. Leave "Host Routes" empty.

            ![!Create Subnet dialog box. The Subnet Details tab is selected. The form has been filled out.](./images/subnet_004.png)

1. Click "Create".

    1. Redirects to the "Overview" page for the network the subnet was added to.

        ![!my_network overview page. There are three tabs. The Overview tab is selected.](./images/subnet_005.png)

    1. Click the "Subnets" tab next to "Overview" to verify the subnet was added to the table for this network.

        ![!my_network overview page. The Subnets tab is selected. The table has one entry labeled my_subnet.](./images/subnet_006.png)

### Deleting a Subnet

<!-- markdownlint-disable MD046 -->
!!! note

    Deleting Subnets is not part of the tutorial, and is here as a reference.
<!-- markdownlint-enable MD046 -->

To delete a subnet, return to the "Networks" page using the left-hand navigation pane. In the table, find the row with the associated subnet, and click the name of the network to go to that network's page.

![!Network page where one entry is associated with the subnet to be deleted.](./images/delete_subnet_001.png)

Click on the "Subnets" tab to go to the subnets table. In the table, find the row with the subnet you wish to delete, and click the drop-down arrow under "Actions" in that row. Then click "Delete Subnet" to open a confirmation dialog.

![!Delete subnet entry highlighted in table row actions drop down menu.](./images/delete_subnet_001.png)

Click "Delete Subnet" again to delete the subnet permanently.

![!Delete subnet confirmation dialog.](./images/delete_subnet_002.png)

<!-- markdownlint-disable MD046 -->
!!! important
    You will not be able to delete the subnet if it is associated with any [routers](#routers) or ports. They will need to be removed or deleted first.
<!-- markdownlint-enable MD046 -->

## Routers

### Creating a Router

To follow these directions for creating a router, a [Network](#creating-a-network) and [Subnet](#creating-a-subnet) must already exist.

1. Click "Network" in the left-hand navigation pane to open the fold-out menu.

    ![!cloud.rc Overview page. Routers is selected in the Network Topology fold-out menu in the left-hand navigation pane.](./images/networks_000.png)

1. Click "Routers" in the fold-out menu.

    ![!cloud.rc Router page. The Routers table is empty.><](./images/routers_001.png)

1. Click "+ Create Router" to open a dialog box.

1. Fill out the dialog box.

    1. Enter a "Router Name". See [Naming Conventions](../index.md#naming-conventions).
    1. Leave "Enable Admin State" checked.
    1. Select "uab-campus" in the "External Network" drop down box.
    1. Leave the "Availability Zone Hints" box empty.

    ![!Create Router dialog. The dialog is filled out. The name is my_router.](./images/routers_002.png)

1. Click "Create Router".

    1. Redirects to the "Routers" page.
    1. There should be a new entry in the table with the name given in (4.a)

    ![!cloud.rc Routers page. The Routers table has one entry. The entry is the my_router.](./images/routers_003.png)

1. Now we need to connect the router to our subnet. Click the name of the new entry under the "Name" column to open the router "Overview" page.

    ![!my_router overview page. Three tabs are available. The Overview tab is selected.](./images/routers_004.png)

1. Click the "Interfaces" tab.

    ![!my_router overview page. The Instances tab is selected. The table is empty.](./images/routers_005.png)

1. Click "+ Add Interface" to open a dialog box.

1. Fill out the dialog box.

    1. Select an existing network-subnet pair in the "Subnet" drop down box.
    1. If this is your only router on the selected subnet, leave "IP Address" empty to use the subnet gateway.

    ![!Add Interface dialog. The dialog is filled out. The my_network subnet is selected as subnet.](./images/routers_006.png)

1. Click "Submit"

    1. Redirects to the "Interfaces" page for the router.
    1. There should be a new entry in the table.

    ![!my_router overview page. The Instances tab is selected. The table has one entry with a random UUID string as name.](./images/routers_007.png)

### Deleting a Router

<!-- markdownlint-disable MD046 -->
!!! note

    Deleting Routers is not part of the tutorial, and is here as a reference.
<!-- markdownlint-enable MD046 -->

To delete a router, return to the "Routers" page using the left-hand navigation pane. In the table, find the row with the router you wish to delete, and click the drop-down arrow under "Actions" in that row. Then click "Delete Router" to open a confirmation dialog.

![!Delete router entry highlighted in table row actions drop down menu.](./images/delete_router_001.png)

Click "Delete Router" again to delete the router permanently.

![!Delete router confirmation dialog.](./images/delete_router_002.png)

## Floating IPs

### Creating a Floating IP

Floating IPs are required if you want an instance to talk to devices on the internet. These IPs are a shared resource, so they must be allocated when needed and released when no longer needed.

1. Click "Network" in the left-hand navigation pane to open the fold-out menu.

    ![!cloud.rc Overview page with Networks selected in the Network Topology fold-out menu in the left-hand navigation pane.](./images/networks_000.png)

1. Click "Floating IPs".

    ![!cloud.rc Floating IPs page. The Floating IPs table is empty.](./images/floating_ips_001.png)

1. Click "Allocate IP to Project" to open a dialog box.

1. Fill out the dialog box.

    1. Select "uab-campus" in the "Pool" drop down box.
    1. Enter a "Description".
    1. Leave "DNS Domain" empty.
    1. Leave "DNS Name" empty.

    ![!Allocate Floating IP dialog. The dialog form is empty.](./images/floating_ips_002.png)

1. Click "Allocate IP".

    1. Redirects to the "Floating IPs" page.
    1. There should be a new entry in the table.

    ![!Floating IPs page. The table has one entry.](./images/floating_ips_003.png)

### Releasing a Floating IP

<!-- markdownlint-disable MD046 -->
!!! note

    Releasing Floating IPs is not part of the tutorial, and is here as a reference.
<!-- markdownlint-enable MD046 -->

To release a floating IP, return to the "Floating IPs" page using the left-hand navigation pane. In the table, find the row with the floating IP you wish to release, and click the drop-down arrow under "Actions" in that row. Then click "Release Floating IP" to open a confirmation dialog.

![!Release floating IP entry highlighted in table row actions drop down menu.](./images/release_floating_ip_001.png)

Click "Release Floating IP" again to release the floating IP.

![!Release floating IP confirmation dialog.](./images/release_floating_ip_002.png)

## Continuing the Tutorial

Now that you have set up a [Network](networks.md), the next step is to apply [Security Policies](security.md) to be able to communicate with it. To continue the tutorial, please visit [Security Policies](security.md) next.
