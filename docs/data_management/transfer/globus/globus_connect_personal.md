# How to Use Globus Connect Personal (GCP)

Globus Connect Personal (GCP) is a tool that lets you turn your personal computer into a Globus endpoint so you can transfer data to and from the Globus ecosystem.

## How Do I Choose Specific Folders to Share Using Globus Connect Personal?

### Choose Specific Folders on Windows

1. In your Windows system tray, locate the icon that looks like a small letter "g" in a circle. This is the icon for Globus Connect Personal. If you cannot locate the icon in the system tray, then open the Globus Connect Personal app on your computer and look for it again.

    ![Expanded system tray showing icon of a small letter "g" in a circle.](../tutorial/images/go-choose-folder/win/001-sys-tray.png)

1. Right-click the icon to open the context menu and click "Options..."
    ![Context menu of Globus system tray icon showing options.](../tutorial/images/go-choose-folder/win/002-context-menu.png)

1. A new window will appear with a tab labelled Access. In the Access tab is an interface to configure folders available on your GCP Collection. For most use cases, you should not check the writeable checkbox. Below is a summary of what each part of the menu does.

   - **(1) Accessible Folders** table with Folder, Shareable and Writeable columns. Any folder listed here will appear on your GCP Collection. Your research data folder or directories must be listed here to be shareable.
   - **(2) Shareable** column checkboxes controlling which folders can be shared with other users. Each of your research data directories must have this checkbox ticked to be shareable from the Collection. **Check this box only if you want to share your data with others.**
   - **(3) Writeable** column checkboxes controlling which folders can be written to by other users. If a folder is shared with other users, then they will be able to add, delete, or change the contents. We recommend against ticking these boxes for Research Cores serving data to customers. **Check this box only if you want others to be able to change your data.**
   - **(4) Plus `+` and minus `-` buttons** that allow you to add or remove folders from the list.
   - **(5) Save** button which saves changes made to this tab of the options.

    ![Access tab of GCP options menu showing the default settings.](../tutorial/images/go-choose-folder/win/003-access-tab-default.png)

1. Use the plus `+` and minus `-` buttons to add your research data folders and remove other folders, as needed. Click the "Shareable" checkbox next to each research data folder. Click "Save" when finished.

    In this example, we removed the default `C:/Users/%username%/Documents` folder with the minus `-` button and added the `D:/data` folder with the `+` button and check the "Shareable" box. You will want to pick the folder where your research data is stored.

    ![Access tab of GCP options menu showing new settings.](../tutorial/images/go-choose-folder/win/004-access-tab-changed.png)

1. Click the "General" tab. The "General" tab enables you to control some settings for the application itself and which folder is the default folder. The default folder will be the first one shown when accessing the Collection.

   - **(1) Run when Windows starts** checkbox enabling starting Globus Connect Personal when you start Windows. **Check this box if GCP should always be on when the computer is on.**
   - **(2) Home Folder** text field that lets you choose which folder will be the default folder for your Collection. We recommend setting this to your primary shared folder from the previous step to simplify navigating your Collection in the Globus Web App.
   - **(3) Save** button which saves changes made to this tab of the options. Be sure to click "Save" if you make changes here.

    ![General tab of GCP options menu showing default settings.](../tutorial/images/go-choose-folder/win/005-general-tab-default.png)

1. Check "Run when Windows starts" if needed. Change the "Home Folder" to match your research data folder. Click "Save" when done.

    In this example, we set the "Home Folder" to match the research data folder, `D:/data` we added in a previous step. If you have multiple research directories to share, you will need to choose just one for this field. Be sure to click save when you are done.

    ![General tab of GCP options menu](../tutorial/images/go-choose-folder/win/006-general-tab-changed.png)

To verify the existence and accessibility of your Collection proceed to [How Do I Find Collections I Created or Own?](../tutorial/globus_organization_tutorial.md#how-do-i-find-collections-i-created-or-own)

### Choose Specific Folders on MacOS

1. In your MacOS notification area, locate the icon that looks like a small letter "g" in a circle. This is the icon for Globus Connect Personal. If you cannot locate the icon in the notification area, then open the Globus Connect Personal app on your computer and look for it again.

    ![Notification area showing icon of a small letter "g" in a circle.](../tutorial/images/go-choose-folder/mac/001-notification-area.png)

1. Right-click or command-click the icon to open the context menu. Click "Preferences…​".

    ![Context menu of Globus system tray icon showing preferences.](../tutorial/images/go-choose-folder/mac/002-context-menu.png)

1. A new window will appear with a tab labelled "Access". Click the "Access" tab if it is not already selected. In this "Access" tab is an interface to configure folders available on your GCP Collection. For most use cases, you should not check the writeable checkbox. Below is a summary of what each part of the menu does.

    - **(1) Accessible Directories and Files** table with "Directory or File", Shareable and Writeable columns. Any folder listed here will appear on your GCP Collection. Your research data folder or directories must be listed here to be shareable.

        <!-- markdownlint-disable MD046 -->
        !!! note

            The terms Directories and Folders are synonyms here.

        <!-- markdownlint-enable MD046 -->

    - **(2) Shareable** column checkboxes controlling which folders can be shared with other users. Each of your research data directories must have this checkbox ticked to be shareable. **Check this box only if you want to share your data with others.**
    - **(3) Writeable** column checkboxes controlling which folders can be written to by other users. If a folder is shared with other users, then they will be able to add, delete, or change the contents. We recommend against ticking these boxes for Research Cores serving data to customers. **Check this box only if you want others to be able to change your data.**
    - **(4) Plus `+` and minus `-`** buttons that allow you to add or remove folders from the list.

    ![Access tab of GCP options menu showing the default settings.](../tutorial/images/go-choose-folder/mac/003-access-tab.png)

1. Use the plus `+` and minus `-` buttons to add your research data folders and remove other folders, as needed. Click the "Shareable" checkbox next to each research data folder. Click "Save" when finished.

To verify the existence and accessibility of your Collection proceed to [How Do I Find Collections I Created or Own?](../tutorial/globus_organization_tutorial.md#how-do-i-find-collections-i-created-or-own)

## How Do I Find Collections I Created or Own?

To find a Collection you own, use the following steps.

1. Navigate to the [Globus Web App](../tutorial/globus_individual_tutorial.md#how-do-i-get-onto-the-globus-web-app) using your browser. You should be at the File Manager page.

    ![File Manager page of the Globus Web App](../tutorial/images/common/file-manager.png)

1. Click either of the Collection Search bar at the top of the File Manager page. This will take you to the Collection Search page.

    ![Collection Search page of the Globus Web App](../tutorial/images/common/collection-search-page.png)

1. Click the Your Collections tab to display a list of Collections you have created or own.

    ![Your Collections tab showing a GCP Collection.](../tutorial/images/go-my-collections/003-your-collections.png)

1. From here there are two options:

    1. Click the name of the Collection to select it for a file transfer and be taken back to the File Manager page.

        ![File Manager page showing selected Collection on left-hand panel.](../tutorial/images/go-my-collections/004-file-manager-selection-made.png)

    1. Click the three dots icon at the right side of the entry to be taken to the Collection details page.

        ![Collectionm details page with overview tab selected.](../tutorial/images/go-my-collections/005-collection-details-page.png)

## How Do I Enable Collection Sharing for My Globus Account?

Before you can share Collections from your Globus Connect Personal (GCP) Collection with others, you must do a one-time setup for your account. You will need to join the "University of Alabama at Birmingham (HA)" (UAB HA) subscription group. Sharing any Collection requires a paid subscription with Globus. UAB Research Computing has a subscription, but Globus does not know your BlazerID is part of our subscription until you join the subscription group. So, Globus also does not know the GCP Collection you created is part of our subscription. By joining our UAB HA group, you and your GCP Collection are confirmed to be part of our subscription, and you can share Collections from the GCP Collection.

To join the UAB HA group, we need to receive both a UAB support request, and a request to join the UAB HA group within the Globus Web App. We need both because we sometimes get spam applications through Globus. Having a Support Request helps us filter the spam. Please use the following steps to join.

1. Submit a [Support Request](../../../help/support.md#how-do-i-create-a-support-ticket). In the request please include the following.

    - Your BlazerID.
    - The text "Please add me to the Globus UAB HA subscription group."
    - The reason you need to be able to share a Collection in Globus. For Research Cores, this would be to share data with your customers.

1. In your browser [get onto the Globus Web App](../tutorial/globus_individual_tutorial.md#how-do-i-get-onto-the-globus-web-app).
1. In the left hand navigation panel click "Groups" to be taken to the Groups page.

    ![Globus groups page with no groups.](../tutorial/images/go-uab-ha-group-access/001-groups-page.png)

1. Ensure the "MY GROUPS" box is unchecked. In the "Filter groups" search bar enter "University of Alabama at Birmingham" to locate the "University of Alabama at Birmingham (HA)" (UAB HA) group.

    ![Globus group page showing search results with University of Alabama at Birmingham (HA) listed](../tutorial/images/go-uab-ha-group-access/002-groups-search.png)

1. Click on the UAB HA group name to be taken to the group details page. The Overview tab should be selected.

    ![UAB HA subscription group details page with overview tab selected.](../tutorial/images/go-uab-ha-group-access/003-uab-ha-overview.png)

1. Click on the "Join this Subscription" button to be taken to the form to submit a request to join.

    ![UAB HA subscription group join request form.](../tutorial/images/go-uab-ha-group-access/004-join-form.png)

1. Fill in the form fields and click the "Submit Application" button when completed. This will send you to a page notifying you that your membership is pending. A request has been sent to Research Computing, so please wait until you see a reply in the support request.

    ![Notice of pending membership.](../tutorial/images/go-uab-ha-group-access/005-pending.png)

1. When your membership has been accepted, you can verify by [returning to the Globus Web App](../tutorial/globus_individual_tutorial.md#how-do-i-get-onto-the-globus-web-app) and navigating to the Groups page. Check the "MY GROUPS". You should see "University of Alabama at Birmingham (HA)" listed with a green, circled checkmark and the word "ACTIVE".

    ![Groups page with my groups checked showing UAB HA subscription group](../tutorial/images/go-uab-ha-group-access/006-my-groups.png.png)

When you have completed the steps in this section, proceed to [creating a Collection](#how-do-i-create-a-collection).

## How Do I Create a Collection?

There are three ways to create a Collection.

- Start from [an existing Collection you created or own](../tutorial/globus_organization_tutorial.md#how-do-i-find-collections-i-created-or-own).
- [Install Globus Connect Personal](./install_gcp.md#how-to-install-globus-connect-personal-gcp) and [share a folder](#how-do-i-choose-specific-folders-to-share-using-globus-connect-personal) to create a Collection.
- Install and configure one or more Collections with Globus Connect Server. To do this, please [Contact Support](../../../help/support.md#how-do-i-create-a-support-ticket) to start a discussion.

The instructions below assume you are starting from an existing Collection. The instructions will work to create a subset of your Globus Connect Personal Collection.

1. [Get onto the Globus Web App]../tutorial/globus_individual_tutorial.md#how-do-i-get-onto-the-globus-web-app).
1. [Find the existing Collection](../tutorial/globus_organization_tutorial.md#how-do-i-find-collections-i-created-or-own) and access its details page.
1. Click the "Collection" tab.

    ![Overview tab of details page with Collection tab to the right.](../tutorial/images/go-create-collection/001-collection-tab.png)

1. Click the "+ Add Guest Collection" button to be taken to a form to create the new Collection.

    ![Collection tab of details page with Add Guest Collection button.](../tutorial/images/go-create-collection/002-add-guest-collection.png)

1. Fill out the form.

    - **(1) You Are Sharing**: Shows which Collection you will be sharing all or part of. Helpful to verify you are sharing the right Collection
    - **(2) Path**: Which path you wish to share. By default, the "/" path is the root of the original Collection. This may not be appropriate for your use case. Generally, when creating one Collection from another, you will want to pick a subfolder of the original Collection. Do this with the "Browse" button.
    - **(3) Display Name**: The name people will see when accessing this Collection, and what they will search for when looking for the Collection.
    - **(4) Description**: An optional description for the Collection.
    - **(5) Keywords**: Optional keywords to help locating the Collection. May be useful for broadly or publicly shared data.

    ![Collection creation form.](../tutorial/images/go-create-collection/003-form.png)

1. Click the "Create Guest Collection" button to create the Collection. You will be taken to the details page of the new Collection, on the Permissions tab.

    ![Permissions tab of new Collection details page.](../tutorial/images/go-create-collection/004-completion.png)

When you have created a Collection, you are ready to [share the Collection with others](#how-do-i-share-a-collection-with-others).

## How Do I Share a Collection With Others?

Before sharing a Collection with others, you will need to first [create a Collection](#how-do-i-create-a-collection) you administer. If the Collection is a [Globus Connect Personal Collection](./install_gcp.md#how-to-install-globus-connect-personal-gcp), then you will also need to [enable Collection sharing for your Globus account](#how-do-i-enable-collection-sharing-for-my-globus-account). If these prerequisites have been met, then you are ready to setup a Collection to be shared with others. Please follow the instructions below.

1. [Get onto the Globus Web App](../tutorial/globus_individual_tutorial.md#how-do-i-get-onto-the-globus-web-app).
1. [Find the Collection](../tutorial/globus_organization_tutorial.md#how-do-i-find-collections-i-created-or-own) you wish to share. In this case we are looking for the "customer-share" Collection.
1. On the "customer-share" Collection details page, click the Permissions tab.

    ![Collection details page overview tab.](../tutorial/images/go-share-collection/001-collection-details-overview.png)

1. Click the "Add Permissions &ndash; Share With" button.

    ![Collection details page permissions tab.](../tutorial/images/go-share-collection/002-collection-details-permissions-before.png)

1. Fill in the form.

    - **Path** defaults to the root of the Collection. This may or may not be acceptable for your use case. Be sure to limit access to only the data that needs to be shared. Use the file browser available in the form to find the correct level of access. For now grant permission to the default.
    - **Share With**: radio buttons to provide control over who to share with. In almost all cases, you will want to share with a single user, which is what we will show here.
        - **User**: Use the "User" search bar to find the specific user you wish to share with. If they have never accessed Globus before, they will not appear in the search results. You can safely enter their email address to add them anyway. For now grant permission to yourself for the purposes of experimenting.
    - **Email Notification** checkbox. We recommend sending an email notification as a convenience.
        - **To** entry field: who to send the email to. We recommend the same person as the "User" selected earlier. There may be future cases where you want to notify others, such as a supervisor, as well.
        - **Message** text entry field: the optional content to send in the email message.
    - **Permissions** The "read" permission must be granted, as that is the point of sharing the Collection. You may additionally give "write" permission to create a two-way collaboration. We recommend Research Cores not grant "write" permission. If you are using a Globus Connect Personal Collection, then "write" permission requires you to correctly [configure your Collection](#how-do-i-choose-specific-folders-to-share-using-globus-connect-personal) to make your shared folder writable.

    ![Add permissions form.](../tutorial/images/go-share-collection/003-add-permissions-form.png)

1. Click the "Add Permission" button to grant permission. You should see a notification confirming the permissions granted. At this point permissions have been granted and the Collection is shared with another person. If you need to add more people, click the "Add another Permision" button and repeat the process. Otherwise click "Done". For now click "Done".

    ![Permission confirmation notification.](../tutorial/images/go-share-collection/004-permissions-confirmation.png)

1. When you click "Done" you should be taken back to the Permissions tab of the Customer Share page. You should see a new entry with "Path: /". If you click the drop-down arrow you will see yourself listed with "Read" permission. If you need to revoke permissions, return to this page and click the icon that looks like a trash can.

    ![Collection details page permissions tab showing new entry.](../tutorial/images/go-share-collection/005-colection-details-permissions-after.png)
