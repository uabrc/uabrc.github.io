# Working with Snapshots

Snapshots are instances or volumes frozen at a moment in time, able to be used in the future. Think of snapshots as a photograph of the state of an instance or volume. Anything done to an instance or volume after the snapshot is taken won't affect the snapshot. We can also create a new instance or volume from an existing snapshot, and continue from that point in time.

## Creating an Instance Snapshot

Instance snapshots are a helpful way to store the state of an instance for later use. Repeating tedious tasks like [Software Installs](./installing_software.md) can be avoided by taking a snapshot at a known-good point during set up of an instance environment, saving time in the future if something goes wrong. Instance snapshots may also be shared with other users to simplify workflows and onboarding new collaborators. To create an instance snapshot please follow the steps below. We assume you are already logged in at [cloud.rc](./introduction.md)

1. Navigate to "Compute" and then "Instances" in the left-hand navigation menu to open the "Instances" page.
2. To make a snapshot of a particular instance, click the drop down menu under the "Actions" column in the row of the desired instance. Then click "Create Snapshot".

    ![!instances table with create snapshot button highlighted](./images/create_snapshot_001.png)

3. A dialog box will open. Fill in the "Snapshot Name" with a memorable name suitable for future reference, then click "Create Snapshot".

    ![!create snapshot dialog](./images/create_snapshot_002.png)

4. You will be taken to the "Images" page, where you new snapshot will appear in its own row in the table.

    ![!images page showing new snapshot](./images/create_snapshot_003.png)

    <!-- markdownlint-disable MD046 -->
    !!! note

        Notice the snapshot has size of zero bytes. The instance snapshot is a convenience pointer to the underlying volume snapshot, so it has no size itself. To see the size of the underlying volume snapshot, click "Volumes" and then "Snapshots" in the left hand navigation menu.

        Don't worry, you'll still be able to create an instance from this snapshot later.
    <!-- markdownlint-enable MD046 -->

## Creating an Instance from an Instance Snapshot

To create an instance from an instance snapshot, follow the directions below, assuming you have [Created an Instance Snapshot](#creating-an-instance-snapshot).

1. Navigate to "Compute" and then "Instances" in the left-hand navigation menu to open the "Instances" page.
2. Click the "Launch Instance" button.

    ![!instances table with launch instance button highlighted](./images/use_snapshot_001.png)

3. A dialog box will open. Follow the instructions at [Basic Instance Setup](./instance_setup_basic.md) until you get to the "Source" tab.
4. In the "Source" tab, select "Instance Snapshot" under the "Select Boot Source" drop down menu.

    ![!launch instance dialog on source tab with instance snapshot selected in select boot source drow down](./images/use_snapshot_002.png)

5. The "Available" table will change, and should contain your previously created instance snapshots.
6. Press the up arrow in the appropriate row of the "Available" table to move that instance snapshot to the "Allocated" table.

    ![!launch instance dialog on source tab with snapshot in allocated table](./images/use_snapshot_003.png)

    <!-- markdownlint-disable MD046 -->
    !!! note

        On the "Flavor" tab, only flavors with large enough disk capacity to hold the snapshot will be allowed. Flavors that are too small will show a yellow triangular caution symbol. Examples are shown below for a 40 GB instance snapshot.

        ![!example of flavors too small to hold an instance snapshot](./images/use_snapshot_004.png)
    <!-- markdownlint-enable MD046 -->

7. Continue following the instructions at [Basic Instance Setup](./instance_setup_basic.md) to start the instance.

## Sharing Snapshots

<!-- markdownlint-disable MD046 -->
!!! construction

    Under construction.
<!-- markdownlint-enable MD046 -->
