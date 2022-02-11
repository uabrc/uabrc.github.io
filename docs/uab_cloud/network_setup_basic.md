# Basic Network Setup

Networking setup should be a one-time setup. Security Groups can and
should be added as needed. While Floating IPs fall under the Networking
fold-out, they should be allocated and released together with instances
to maximize security.

## Creating a Network

1. Click "Network" in the left-hand navigation pane to open the fold-out menu.

    ![!OpenStack Overview page. Networks is selected in the Network Topology fold-out menu in the left-hand navigation pane.](./images/networks_000.png)

2. Click "Networks" in the fold-out menu.

    1. The "Networks" page will open.
    2. The "uab_campus" network entry should already be in the table.

        ![!OpenStack Networks page. The Networks table has one entry. The entry is the default, persistent uab-campus network.](./images/networks_001.png)

3. Click "+ Create Network" to open a dialog box.

4. Fill out the dialog box. Only the "Network" tab is important, we
    will create a subnet as a separate step.

    1. Enter a "Network Name".
    2. Leave "Enable Admin State" checked.
    3. Uncheck "Create Subnet". We will do this as a separate step. The other tabs should be removed.
    4. Leave the "Availability Zone Hints" box empty.

        ![!Create Network dialog. The dialog form is empty except Network Name has been set to my_network.](./images/networks_003.png)

5. Click "Create".

    1. Redirects to the "Networks" page.
    2. There should be a new entry in the table with the name given in (4.a)

        ![!OpenStack Networks page. There is an additional entry in the table. The new entry is my_network.](./images/networks_004.png)

## Creating a Subnet

1. Click "Network" in the left-hand navigation pane to open the
    fold-out menu.

    ![!OpenStack Overview page. Networks is selected in the Network Topology fold-out menu in the left-hand navigation pane.](./images/networks_000.png)

2. Click "Networks" in the fold-out menu.

    1. The "Networks" page will open.
    2. The "uab_campus" network should already be an entry in the table.
    3. At least one other entry must be in the table. See `Creating a Network`.

        ![!OpenStack Networks page. There are two entries in the table. One is the default, persistent uab-campus network. The other is my_network.](./images/networks_004.png)

3. Under the "Actions" column, select the drop-down triangle button in the row corresponding to the network you want to add a subnet to.

    ![!Drop-down box under the Actions column in the my-network row of the Networks table. The drop-down box has been clicked, revealing two options. The selected option is Create Subnet.](./images/subnet_002.png)

4. Click "Create Subnet" in the drop-down to open a dialog box.

5. Fill out the dialog box.

    1. The "Subnet" tab.

        1. Enter a "Subnet Name".
        2. Enter `192.168.0.0/24` as the "Network Address". The trailing `/24` allocates the entire range from `192.168.0.0` through `192.168.0.255` to the subnet.
        3. Ensure "IPv4" is selected in the "IP Version" drop-down box.
        4. Leave "Gateway IP" empty to use the default value of `192.168.0.0`.
        5. Leave "Disable Gateway" unchecked.
        6. Click the "Next \>\>" button to move to the "Subnet Details" tab.

            ![!Create Subnet dialog box. The Subnet tab is selected. The form has not been filled out beyond default values. The Subnet Name has been set to my_subnet.](./images/subnet_003.png)

    2. The "Subnet Details" tab.

        1. Leave "Enable DHCP" checked.
        2. Enter `192.168.0.20,192.168.0.100` in the "Allocation Pools" box. The IP addresses in that range will be assigned to instances on this subnet.
        3. Leave "DNS Name Servers" empty.
        4. Leave "Host Routes" empty.

            ![!Create Subnet dialog box. The Subnet Details tab is selected. The form has been filled out.](./images/subnet_004.png)

6. Click "Create".

    1. Redirects to the "Overview" page for the network the subnet was added to.

        ![!my_network overview page. There are three tabs. The Overview tab is selected.](./images/subnet_005.png)

    2. Click the "Subnets" tab next to "Overview" to verify the subnet was added to the table for this network.

        ![!my_network overview page. The Subnets tab is selected. The table has one entry labeled my_subnet.](./images/subnet_006.png)

## Creating a Router

To follow these directions for creating a router, a `network<Creating a Network>` and `subnet<Creating a Subnet>` must already exist.

1. Click "Network" in the left-hand navigation pane to open the fold-out menu.

    ![!OpenStack Overview page. Routers is selected in the Network Topology fold-out menu in the left-hand navigation pane.](./images/networks_000.png)

2. Click "Routers" in the fold-out menu.

    ![!OpenStack Router page. The Routers table is empty.](./images/routers_001.png)

3. Click "+ Create Router" to open a dialog box.

4. Fill out the dialog box.

    1. Enter a "Router Name".
    2. Leave "Enable Admin State" checked.
    3. Select "uab-campus" in the "External Network" drop down box.
    4. Leave the "Availability Zone Hints" box empty.

    ![!Create Router dialog. The dialog is filled out. The name is my_router.](./images/routers_002.png)

5. Click "Create Router".

    1. Redirects to the "Routers" page.
    2. There should be a new entry in the table with the name given in (4.a)

    ![!OpenStack Routers page. The Routers table has one entry. The entry is the my_router.](./images/routers_003.png)

6. Now we need to connect the router to our subnet. Click the name of the new entry under the "Name" column to open the router "Overview" page.

    ![!my_router overview page. Three tabs are available. The Overview tab is selected.](./images/routers_004.png)

7. Click the "Interfaces" tab.

    ![!my_router overview page. The Instances tab is selected. The table is empty.](./images/routers_005.png)

8. Click "+ Add Interface" to open a dialog box.

9. Fill out the dialog box.

    1. Select an existing network-subnet pair in the "Subnet" drop down box.
    2. If this is your only router on the selected subnet, leave "IP Address" empty to use the subnet gateway.

    ![!Add Interface dialog. The dialog is filled out. The my_network subnet is selected as subnet.](./images/routers_006.png)

10. Click "Submit"

    1. Redirects to the "Interfaces" page for the router.
    2. There should be a new entry in the table.

    ![!my_router overview page. The Instances tab is selected. The table has one entry with a random UUID string as name.](./images/routers_007.png)

## Creating a Security Group

These instructions show you how to prepare to use SSH with your instances. Security Groups are used to set rules for how external devices can connect to our instances. Here we will create an SSH Security Group using a method that can be applied to other types of connections. The method used can be applied to other types of Security Groups as well.

1. Click "Networks" in the left-hand navigation pane to open the fold-out menu.

    ![!OpenStack Overview page. Security Groups is selected in the Network Topology fold-out menu in the left-hand navigation pane.](./images/networks_000.png)

2. Click "Security Groups" in the fold out menu.

    ![!OpenStack Security Groups page. The Security Groups table has one entry, the default, persistent entry labeled default.](./images/security_groups_001.png)

3. Click "+ Create Security Group" to open a dialog box.

4. Fill out the dialog box.

    1. Under "Name" enter `ssh`.
    2. Leave "Description" empty.

    ![!Create Security Group dialog. The dialog has been filled out with the name set as ssh.](./images/security_groups_002.png)

5. Click "Create Security Group".

    1. Redirects to the "Manage Security Group Rules: ssh" page.
    2. There should be an entry for "Egress IPv4" and "Egress IPv6". Leave these alone.

    ![!Manage Security Group Rules for ssh. The Table has two entries, both Egress direction. One is for IPv4 and the other for IPv6. Both have no IP restrictions.](./images/security_groups_003.png)

6. Click "+ Add Rule" to open a dialog box.

    1. Select "SSH" in the "Rule" drop down box. This will change the remaining fields.
    2. Leave "Description" empty.
    3. Select "CIDR" in the "Remote" drop down box.
    4. Type `0.0.0.0/0` in the "CIDR" box. **WARNING!** This is **NOT** good practice! For your research instances, you'll want to constrain the CIDR value further to a narrower range of IP addresses. The rule we have shown here leaves the SSH port open to all IP addresses world-wide.

    ![!Add Rule dialog box. The dialog box is filled out. The rule is set to SSH.](./images/security_groups_004.png)

7. Click "Add".

    1. Redirects to the "Manage Security Group Rules: ssh" page.
    2. There should be a new entry in the table.

    ![!Manage Security Group Rules for ssh. The Table has three entries. The new entry is Ingress direction with IPv4. It is restricted to TCP port 22 on all IPs.](./images/security_groups_005.png)
