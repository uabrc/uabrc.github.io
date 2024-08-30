# Setting up Globus as a Research Manager

This tutorial is designed to guide UAB research managers, such as Lab PIs, Core Directors, and their management staff, to help them set up and use Globus Connect Personal (GCP) for secure data sharing on their local/personal computers. GCP allows you to share data with collaborators efficiently meeting security and compliance standards for file sharing.

**What You Will Learn:**

1. [What is Globus, and why you should use it?](globus_group_tutorial.md#what-is-globus-and-why-you-should-use-it)
1. [How do you get onto Globus?](globus_group_tutorial.md#how-do-you-get-onto-globus)
1. [Installing Globus Connect Personal on Windows](globus_group_tutorial.md#installing-gcp-on-windows)
1. [Installing Globus Connect Personal on MacOS](globus_group_tutorial.md#installing-gcp-on-macos)
1. [Configuring the GCP endpoint to share specific folders](globus_group_tutorial.md#configuring-the-gcp-endpoint-to-share-specific-folders)
1. [Configuring a shared collection on your GCP endpoint](globus_group_tutorial.md#configuring-a-shared-collection-on-your-gcp-endpoint)
1. [Sharing a collection with a collaborator](globus_group_tutorial.md#sharing-a-collection-with-a-collaborator)

## What is Globus, and why you should use it?

We have a guide here(./globus_individual_tutorial.md#what-is-globus) that explains Globus, and its features.

## How do you get onto Globus?

We have a guide here(./globus_individual_tutorial.md#how-do-you-get-on-globus) that shows how to access Globus.

## Installing Globus Connect Personal

Globus Connect Personal is available on the following Operating Systems, Linux, MacOS and Windows. The steps in this tutorial are curated from the Globus docs showing how to install Globus on [Windows](https://docs.globus.org/globus-connect-personal/install/windows/) and [MacOS](https://docs.globus.org/globus-connect-personal/install/mac/).

### Installing GCP On Windows

The following steps will guide you to install `GCP` on your local machine running the `Windows OS`.

1. Navigate to the [Globus Connect Personal page](https://www.globus.org/globus-connect-personal), scroll to look for the GCP Windows version. Click on the `**INSTALL NOW**` button highlighted red in the image below.

    ![!Install GCP for Windows](./images/gcp_install_windows.png)

1. Click the `Download Globus Connect Personal` link on this page, it would redirect you to download the GCP Installer.

    ![!Download GCP for Windows](./images/gcp_dl_installer_windows.png)

1. As shown in the image below,  click the `Download Globus Connect Personal for Windows` button preceded by the Microsoft/Windows logo to download the installer. This would download the application installer into your local computer.

    ![!Download GCP Installer for Windows](./images/gcp_download_button.png)

1. Navigate to where the file is downloaded on your local computer. Double click to open the downloaded file named **globusconnectpersonal-latest.exe**

    ![!Downloaded GCP Installer for Windows file](./images/gcp_installer_file.png)

1. Select where you would prefer to have your GCP installed (by default it installs into your C:\ drive), and click the **Install** button.

    ![!Completing GCP Setup for Windows file highlighting Install button](./images/gcp_click_install.png)

    Please note you must have administrator permissions, to do this. If you see the below image, please contact your local computer's administrator to complete the installation.

    ![!Administrator privileges for GCP Installer](./images/gcp_admin_install.png)

1. Allow the installation to complete, and click on **Finish**. This will complete the GCP installation.

    ![!Completing GCP Setup highlighting Finish button](./images/gcp_click_finish.png)

1. Following installation, GCP will launch in a new window, click on **Log In** to authenticate with Globus, to begin the Collection Setup process.

    ![!Authenticating GCP Setup highlighting Login button](./images/gcp_globus_login.png)

1. Grant the required consents to GCP setup. And include a name of your liking in the highlighted area.

    ![!Granting GCP Setup required permissions](./images/gcp_consent.png)

1. Enter the details for your GCP Collection, and click save to continue. In the image below, **1** should contain your preferred identity, if using a UAB Computer, please insert your `BlazerID@uab.edu` email address here. **2** Should contain the name for your Collection, already named in the previous step. **3** Should contain optional information to describe the collection, you can include the purpose for which the collection has been created. **4** If your collection would contain Protected Health Information (PHI) or sensitive information, please tick this box. You would need to be part of UAB's subscription to complete this, please send an email to support, so we can complete that process on your behalf.

    ![!GCP Setup Details](./images/gcp_details.png)

1. We have now completed set up of our GCP for a local computer operating the Windows OS. Exit the setup process, and open the Globus Web App to view collection details or move data to or from your collection.

    ![!GCP Exit Setup](./images/gcp_exit_setup.png)

1. After installation, you should now see a **g** Globus icon in the menu bar at the bottom of your screen. This indicates that Globus Connect Personal is running and your new collection is ready to be used.

    ![!GCP Logo in Menu](./images/gcp_logo_menu.png)

### Installing GCP On MacOS

Download the Installer:

Go to the Globus Connect Personal download page.
Click on "Download for MacOS."
Install the Application:

Open the downloaded .dmg file and drag the Globus Connect Personal icon into the Applications folder.
Launch and Login:

Open the Globus Connect Personal app from your Applications folder.
Log in using your Globus account credentials.

## Configuring the GCP endpoint to share specific folders

### On Windows

1. Open Globus Connect Personal:

1. Click on the Globus icon in your taskbar.
1. Select Folders to Share:

1. Go to the “Folders” tab.
1. Click “Add Folder” and navigate to the folder you want to share.
1. Select the folder and click “OK.”
1. Set Permissions:

1. Adjust the sharing permissions as needed for each folder.

### On MacOS

1. Open Globus Connect Personal:

1. Click on the Globus icon in your menu bar.
1. Add Folders for Sharing:

1. In the “Folders” tab, click “Add Folder.”
1. Navigate to the folder you wish to share and select it.
1. Click “Open” to add it to the list of shared folders.
1. Configure Permissions:

1. Set the permissions as per your requirements.

**Prerequisites for Sharing a GCP Endpoint**

1. Before you can share a GCP endpoint, ensure the following:

1. Globus Account: You must have a Globus account associated with your institution.
1. Institutional Subscription: You must join the UAB (HA) subscription group. Contact your institution’s IT department to verify your inclusion in the appropriate subscription group.
1. Network Access: Ensure that your network firewall settings allow Globus traffic.

## Configuring a Shared Collection on Your GCP Endpoint

1. Navigate to the Globus Web App:

1. Go to app.globus.org and log in with your credentials.
1. Create a New Shared Collection:

1. Locate your GCP endpoint under "Endpoints."
1. Click on the endpoint and select “Create a New Shared Collection.”
1. Configure Collection Settings:

1. Name your collection and provide a description.
1. Select the folder you want to share.
1. Set the appropriate access permissions.

## Sharing a Collection with a Collaborator

1. Find Your Collection:

1. In the Globus Web App, locate the collection you created.
1. Invite Collaborators:

1. Click on the “Share” button next to your collection.
1. Enter the email addresses of your collaborators.
1. Set the desired permissions (read, write, etc.).
1. Send the Invitation:

1. Click “Save” to share the collection with your collaborators.
1. Your collaborators will receive an email invitation to access the collection.
