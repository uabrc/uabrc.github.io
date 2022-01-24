# Globus

## Setting up Globus Connect Personal

[Globus Connect Personal](https://www.globus.org/globus-connect-personal) is software meant to be installed on local machines such as laptops, desktops,
workstations and self-owned, local-scale servers. Globus maintains excellent documentation for installation on [MacOS](https://docs.globus.org/how-to/globus-connect-personal-mac/), [Linux](https://docs.globus.org/how-to/globus-connect-personal-linux) and [Windows](https://docs.globus.org/how-to/globus-connect-personal-windows).

To verify your installation is complete, please visit <https://app.globus.org> and log in. Click "Endpoints" in the left-hand navigation pane and then click the "Administered By You" tab. Look in the table for the endpoint you just created.

## Moving Data Between Endpoints

1. Log in to the Globus App online at <https://app.globus.org> using UAB Single Sign-On (SSO). Start typing "University of Alabama at Birmingham" into the "Use your existing organizational login" text box and selected it when it appears in the list.

    ![](./images/globus_001_login.png)

2. Click File Manager in the left-hand navigation pane.

    ![](./images/globus_002_nav_pane_file_manager.png)

3. Ensure the center icon for the "Panels" selection is picked.

    ![](./images/globus_003_panels.png)

4. Click the "Search" icon in the "Collection" text box near the top-left or top-right of the page to locate an endpoint. There are multiple ways to find an endpoint. For some endpoints you may be asked to log in, which is true of all UAB endpoints. Some UAB endpoints may also require that you be on the UAB VPN.

    ![](./images/globus_004_search_bar.png)

    1. Begin typing in the box to search for an endpoint. To find UAB-related endpoints, search for "UAB". There are two Cheaha endpoints

        1. Cheaha cluster on-campus (UAB Science DMZ) for machines that are on campus or connected to the VPN.
        2. Cheaha cluster off-campus (UAB Science DMZ) for machines that are off campus and not on the VPN.

    2. The "Recent" tab shows endpoints that have most recently been used.

        ![](./images/globus_005_recent_tab.png)

    3. The "Bookmarks" tab shows a list of endpoint bookmarks.

        ![](./images/globus_006_bookmarks_tab.png)

    4. The "Your Collections" tab shows all endpoints owned by you. For most users this will be one or more Globus Connect Personal endpoints.

        ![](./images/globus_007_your_collections_tab.png)

    5.  The "Shared With You" tab shows any private endpoints that have
        been shared with you by other users, possibly collaborators.

    6.  The "More Options" tab will show a brief text on installing
        Globus Connect Personal.

5. When an endpoint has been selected you will see a list of folders and files on the default path for that endpoint in the bottom box. You can use the "Path" box to type a path to find the files you are looking for.

    ![](./images/globus_010_one_endpoint_done.png)

6. Repeat the process of selecting an endpoint for the other "Collection" text box.

    ![](./images/globus_011_two_endpoint_done.png)

7. When both endpoints have been selected and you have chosen the correct paths for each endpoint, select files and/or folders on the side you wish to transfer FROM. We will call this side the source endpoint, and the other side the target endpoint. Selections may be made by clicking the checkboxes that appear when you hover over each file or folder.

    ![](./images/globus_012_selected_files.png)

8. When all files and folders have been selected from the source endpoint, click the "Start" button on the source endpoint side. This will start a transfer process from source to target. The files will be placed in the currently open path on the target endpoint.

    ![](./images/globus_013_popup.png)

9. A green pop-up notification will appear indicating the transfer has started. Click "View details \>" to be taken to the status of the transfer. You can also check on the status of any transfers by clicking the "Activity" button in the left-hand navigation pane.

### Transfer and Sync Options

Between the two "Start" buttons on the "File Manager" page is a "Transfer & Sync Options" drop down menu. Click that button to change the options. More information on each option. A brief summary of the options are...

    ![](./images/globus_040_transfer_and_sync_options.png)

1. sync - Sync files only, rather than create new files.
2. delete files - Delete any files on the target that are not on the source. Useful for forcing identical filesystems when syncing.
3. preserve source - Copies file "modified time" metadata.
4. verify integrity - Verifies that checksums are identical on source and target after transfer completes. Highly recommended to have this checked.
5. encrypt transfer - Encrypts data before leaving source and decrypts after arriving at destination. Recommended for all transfers, required and enforced for all UAB endpoints.
6. skip files - Skips source files that cause errors during the transfer. Otherwise the entire transfer will stop when an error is encountered.
7. quota fail - Fails instead of retries when the target storage quota is exceeded.

### Common Errors

1. File Not Found - This may mean that a file was not readable by Globus. Check that the file hasn't moved or changed names during the transfer. It is recommended to not modify files while they are being transferred by Globus.
2. Permission Denied - Globus is not able to access the files because permissions do not allow it. For Globus Connect Personal, be sure the containing folder is on the "Accessible Folders" list. Be sure that your user account has access to read the file.

### More Information

A [Globus FAQ](https://docs.globus.org/faq/globus-connect-endpoints/) is available for additional information on endpoints and transfers.

## Using Bookmarks

To save a bookmark, use the File Manager interface to select an endpoint and navigate to a path on that endpoint. Then click the bookmark button as shown below.

    ![](./images/globus_060_create_bookmark.png)

To manage bookmarks, click "Bookmarks" in the left-hand navigation pane. Click the "Pencil" icon to edit a bookmark. Click the "Trash Bin" icon to delete a bookmark.

    ![](./images/globus_061_manage_bookmarks.png)

## Managing Shared Collections from a Globus Connect Personal Endpoint

It is NOT RECOMMENDED to make Globus Connect Personal endpoints public as this is insecure. It is more difficult to manage access controls for the entire Globus Connect Personal endpoint than for a shared collection. Shared collections make it simpler to share different data with distinct collaborators, and to manage who has access to what data. Be secure, use shared collections!

### Creating a Shared Collection

1. Click "Endpoints" in the left-hand navigation pane.

2. Click the "Administered By You" tab.

    ![](./images/globus_100_shared_admin_tab.png)

3. In the table, find the endpoint you wish to share data from and click its name. You will be taken to the page for that endpoint.

4. Click the "Collections" tab.

    ![](./images/globus_101_shared_collections.png)

5. Click the "Add a Guest Collection" button.

6. Fill out the form.

    ![](./images/globus_102_shared_collection_form.png)

    1. Manually enter a path or click the Browse button to select a folder.
    2. Give a short but memorable name for your shared collection. This information will be useful for your collaborators.
    3. Optionally fill in a more detailed description of the shared collection for your records.
    4. Optionally fill in searchable keywords.

7. Click "Create Share" to move to the next step. You will be taken to the page for the newly created collection, which is now a full-fledged endpoint. Any further references to "an endpoint" will be about the newly created, shared collection.

8. Make sure you are on the "Permissions" tab. You should see a permissions table with your name in the first row.

    ![](./images/globus_103_shared_permissions.png)

9. Click "Add Permissions -- Share With" to share your endpoint with other users.

10. Fill out the form.

    ![](./images/globus_104_shared_add_permissions.png)

    1. Optionally enter a path within the shared endpoint or use the Browse button. If you leave the path as just a slash, the entire shared endpoint will be shared with these users.
    2. Select who to share with.
        1. User - One or more users.
        2. Group - All members of a group.
        3. All Users - All globus users. **Warning! This exposes data publicly!**
    3. Search for users to add, or a group, depending on your choice above. You should be able to find any globus user using the search box. **Warning! Be certain of which user you are selecting! Check the email domain!**
    4. If adding users, optionally enter a message so they know why they are being added.
    5. Select permissions. Read is automatically selected and cannot be changed. Write permissions are optional.

11. Click "Add Permission" to add permissions for these users or groups.
    You will be returned to the page for the shared endpoint and should
    be on the "Permissions" tab and should see the user or group in the
    table.

### Deleting a Shared Collection

1. Click "Endpoints" in the left-hand navigation pane, then c

2. Click the "Administered By You" tab.

    ![](./images/globus_100_shared_admin_tab.png)

3. Click the right caret ">" icon at the right side of the row with the endpoint you wish to delete. You will be taken to the information page for that endpoint.

4. Click "X Delete Endpoint" and a confirmation dialog will open at the top of the page. Respond to the dialog to delete the endpoint, or to cancel.

    ![](./images/globus_105_shared_delete.png)

## Setting up Globus Connect Server

Under construction!
