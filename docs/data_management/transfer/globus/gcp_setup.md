# How to Use Globus Connect Personal (GCP)

Globus Connect Personal (GCP) is a tool that allows you to connect your local (personal) computer to a Globus ecosystem as a collection, enabling you to transfer data to and from your local computer.

To set up a collection on your local (personal) computer using GCP, you must first install GCP by following the instructions on our [GCP installation](./gcp_install.md) page.

## How Do I Configure GCP to Access Specific Folders or Drives on My Local Computer?

After installing GCP, you can configure specific folders or drives to be accessible through the Globus web interface. Follow the instructions for your operating system below.

<!-- markdownlint-disable MD046 -->

=== "Choose Specific Folders on Windows"
    1. In your Windows system tray, locate the icon that looks like a small letter "g" in a circle. This is the icon for Globus Connect Personal. If you cannot locate the icon in the system tray, then open the Globus Connect Personal app on your computer and look for it again.

        ![Expanded system tray showing icon of a small letter "g" in a circle.](../images/go-choose-folder/win/001-sys-tray.png)

    1. Right-click the icon to open the context menu and click "Options..."
        ![Context menu of Globus system tray icon showing options.](../images/go-choose-folder/win/002-context-menu.png)

    1. A new window will appear with a tab labelled Access. In the Access tab is an interface to configure folders available on your GCP Collection. For most use cases, you should not check the writeable checkbox. Below is a summary of what each part of the menu does.

    - **(1) Accessible Folders** table with Folder, Shareable and Writeable columns. Any folder listed here will appear on your GCP Collection. Your research data folder or directories must be listed here to be shareable.
    - **(2) Shareable** column checkboxes controlling which folders can be shared with other users. Each of your research data directories must have this checkbox ticked to be shareable from the Collection. **Check this box only if you want to share your data with others.**
    - **(3) Writeable** column checkboxes controlling which folders can be written to by other users. If a folder is shared with other users, then they will be able to add, delete, or change the contents. We recommend against ticking these boxes for Research Cores serving data to customers. **Check this box only if you want others to be able to change your data.**
    - **(4) Plus `+` and minus `-` buttons** that allow you to add or remove folders from the list.
    - **(5) Save** button which saves changes made to this tab of the options.

        ![Access tab of GCP options menu showing the default settings.](../images/go-choose-folder/win/003-access-tab-default.png)

    1. Use the plus `+` and minus `-` buttons to add your research data folders and remove other folders, as needed. Click the "Shareable" checkbox next to each research data folder. Click "Save" when finished.

        In this example, we removed the default `C:/Users/%username%/Documents` folder with the minus `-` button and added the `D:/data` folder with the `+` button and check the "Shareable" box. You will want to pick the folder where your research data is stored.

        ![Access tab of GCP options menu showing new settings.](../images/go-choose-folder/win/004-access-tab-changed.png)

    1. Click the "General" tab. The "General" tab enables you to control some settings for the application itself and which folder is the default folder. The default folder will be the first one shown when accessing the Collection.

    - **(1) Run when Windows starts** checkbox enabling starting Globus Connect Personal when you start Windows. **Check this box if GCP should always be on when the computer is on.**
    - **(2) Home Folder** text field that lets you choose which folder will be the default folder for your Collection. We recommend setting this to your primary shared folder from the previous step to simplify navigating your Collection in the Globus Web App.
    - **(3) Save** button which saves changes made to this tab of the options. Be sure to click "Save" if you make changes here.

        ![General tab of GCP options menu showing default settings.](../images/go-choose-folder/win/005-general-tab-default.png)

    1. Check "Run when Windows starts" if needed. Change the "Home Folder" to match your research data folder. Click "Save" when done.

        In this example, we set the "Home Folder" to match the research data folder, `D:/data` we added in a previous step. If you have multiple research directories to share, you will need to choose just one for this field. Be sure to click save when you are done.

        ![General tab of GCP options menu](../images/go-choose-folder/win/006-general-tab-changed.png)

=== "Choose Specific Folders on MacOS"

    1. In your MacOS notification area, locate the icon that looks like a small letter "g" in a circle. This is the icon for Globus Connect Personal. If you cannot locate the icon in the notification area, then open the Globus Connect Personal app on your computer and look for it again.

        ![Notification area showing icon of a small letter "g" in a circle.](../images/go-choose-folder/mac/001-notification-area.png)

    1. Right-click or command-click the icon to open the context menu. Click "Preferences…​".

        ![Context menu of Globus system tray icon showing preferences.](../images/go-choose-folder/mac/002-context-menu.png)

    1. A new window will appear with a tab labelled "Access". Click the "Access" tab if it is not already selected. In this "Access" tab is an interface to configure folders available on your GCP Collection. For most use cases, you should not check the writeable checkbox. Below is a summary of what each part of the menu does.

        - **(1) Accessible Directories and Files** table with "Directory or File", Shareable and Writeable columns. Any folder listed here will appear on your GCP Collection. Your research data folder or directories must be listed here to be shareable.

            <!-- markdownlint-disable MD046 -->
            !!! note

                The terms Directories and Folders are synonyms here.

            <!-- markdownlint-enable MD046 -->

        - **(2) Shareable** column checkboxes controlling which folders can be shared with other users. Each of your research data directories must have this checkbox ticked to be shareable. **Check this box only if you want to share your data with others.**
        - **(3) Writeable** column checkboxes controlling which folders can be written to by other users. If a folder is shared with other users, then they will be able to add, delete, or change the contents. We recommend against ticking these boxes for Research Cores serving data to customers. **Check this box only if you want others to be able to change your data.**
        - **(4) Plus `+` and minus `-`** buttons that allow you to add or remove folders from the list.

        ![Access tab of GCP options menu showing the default settings.](../images/go-choose-folder/mac/003-access-tab.png)

    1. Use the plus `+` and minus `-` buttons to add your research data folders and remove other folders, as needed. Click the "Shareable" checkbox next to each research data folder. Click "Save" when finished.
<!-- markdownlint-enable MD046 -->

To verify that your personal collection exists and view the files you previously configured to be accessible through GCP, start GCP on your local computer following the steps in [GCP installation](./gcp_install.md) page. Then, click "Web: Transfer Files" to open your collection in the Globus web interface. You will see your collection name in the collection search bar, along with a list of the files you previously configured for sharing.

You can also find your collection under the "Your Collections" tab by following the steps in [How Do I Find Collections I Created or Own?](../globus/globus_organization_tutorial.md#how-do-i-find-collections-i-created-or-own).

## How Do I Share Data With Other Users From My Local Computer?

Making folders or drives accessible through GCP does not automatically make them available to other users. To share your data, you must create a Guest Collection and configure the appropriate permissions. GCP must also be running on your local computer for users to access or transfer files through the Guest Collection created from your local collection.

To create and share a Guest Collection from a collection on your local computer, you must be a member of the "University of Alabama at Birmingham (HA)" subscription group. Please see [How Do I Enable Collection Sharing for My Globus Account?](../globus/globus_organization_tutorial.md#how-do-i-enable-collection-sharing-for-my-globus-account) page for instructions on how to request the UAB HA subscription group membership.

If you have any questions, please [Contact US](../../../help/support.md#how-to-request-support).
