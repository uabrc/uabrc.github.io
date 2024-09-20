# Globus Tutorials for Research Groups

This tutorial is designed to guide UAB research managers, such as Lab PIs, Core Directors, and their management staff, to help them set up and use Globus Connect Personal (GCP) for secure data sharing on their local/personal computers. GCP allows you to share data with collaborators efficiently meeting security and compliance standards for file sharing.

**What You Will Learn:**

1. [What is Globus?](#what-is-globus)
1. [Why Use Globus?](#why-use-globus)
1. [How Does Globus Work?](#how-does-globus-work)
1. [How Do I Get onto the Globus Web App?](#how-do-i-get-onto-the-globus-web-app)
1. [How Do I Install Globus Connect Personal?](#how-do-i-install-globus-connect-personal)
    - [Windows](#installing-gcp-on-windows)
    - [MacOS](#installing-gcp-on-macos)
1. [How Do I Share Specific Folders Using Globus Connect Personal?](#how-do-i-share-specific-folders-using-globus-connect-personal)
1. [How Do I Share a Collection with Others?](#how-do-i-share-a-collection-with-others)

If you are new to Globus, we recommend starting with our [Globus Tutorials for Individual Researchers](./globus_individual_tutorial.md) first to familiarize yourself with how Globus is used. When those are complete, we then recommend following the tutorials on this page in order from start to finish, as later tutorials assume the previous tutorials have been completed.

## Prerequisites

For these tutorials, you will need your BlazerID or [XIAS ID](../../account_management/xias/index.md) and password to authenticate using UAB Single Sign-On (SSO).

## What is Globus?

Globus is a data transfer ecosystem that simplifies the process of transferring, sharing, and managing large datasets. It is used by research institutions around the world to move research data between different storage devices, computer systems, and institutions.

## Why Use Globus?

Globus has many research data oriented features, making it ideal for many research data transfer scenarios. Below is a list of features.

- Straight-forward, browser-based interface.
- Compatible with [Long-Term Storage](../lts/index.md).
- Can be used to share data with Research Core customers.
- Can be used to transfer data between lab workstations, servers, and Cheaha.
- Transfers are automatically retried in the event of network or computer system outages.
- Transfers are encrypted end-to-end. Globus never sees your data.
- Suitable for transferring PHI and HIPAA data. Note: a UAB Enterprise IT risk assessment is required.

## How Does Globus Work?

Globus is an ecosystem of software intended to make research data transfer simpler. The Globus web application at <https://app.globus.org> allows you to initiate transfers between any two endpoints you have authorization to access. The Globus Connect Personal (GCP) and Globus Connect Server (GCS) software let you turn any computer into a Globus endpoint. At no point do Globus servers touch your research data. Instead, when you initiate a transfer between two endpoints, the Globus application tells the two endpoints that they need to talk to each other and data is sent directly between them. The endpoints update the application with information you may need to know, such as how much data has transferred so far, how fast the transfer is proceeding, and any errors that occur. If the connection between endpoints is interrupted for any reason, the Globus application will attempt to restart the transfer from where it left off.

## How Do I Get Onto the Globus Web App?

Our [Globus Tutorials for Individual Researchers Page](./globus_individual_tutorial.md#how-do-i-get-onto-the-globus-web-app). Please visit that link and then return here when you have finished.

## How Do I Install Globus Connect Personal?

Globus Connect Personal (GCP) is available on the following Operating Systems, Linux, MacOS and Windows. The steps in this tutorial are curated from the Globus docs showing how to install Globus on the following operating systems.

- [Windows](#installing-gcp-on-windows)
- [MacOS](#installing-gcp-on-macos).

### Installing GCP On Windows

The following steps will guide you to install Globus Connect Personal (GCP) on your computer running Windows OS.

1. Navigate to the [Globus Connect Personal official page](https://www.globus.org/globus-connect-personal) and scroll down to find the GCP Windows version. Click on the "INSTALL NOW" button in the red box in the image below to be taken to the official installation instructions and download link for GCP for Windows.

    ![!Globus Connect Personal official page showing operating system options with links. Windows is in the center of the three.](./images/gg-gcp-install/win/001-select.png)

1. Click the `Download Globus Connect Personal` link on the instructions page, as shown below. This will redirect you to the GCP for Windows installer.

    ![!Globus Connect Personal for Windows official instructions page with link to download GCP for Windows.](./images/gg-gcp-install/win/002-instructions.png)

1. As shown in the image below, click the "Download Globus Connect Personal for Windows" button to download the installer to download the installer to your computer.

    ![!Download GCP Installer for Windows](./images/gg-gcp-install/win/003-download.png)

1. Find the installer on your computer and open it. Select where you would prefer to have your GCP installed and click the "Install" button.

    ![GCP installer window showing selected path and install button.](./images/gg-gcp-install/win/004-select-path.png)

    Please note you must have administrator permissions, to do this. If you are unable to do so, you will need to contact the IT group managing your computer.

1. When the installation is complete, click the "Finish" button to complete the GCP installation.

    ![!Completing GCP Setup highlighting Finish button.](./images/gg-gcp-install/win/005-finish.png)

1. Following installation, GCP will launch in a new window. If it does not, look for it in your Start Menu.

    When GCP has started, click on "Log In" to authenticate with Globus to begin the Collection setup process. This is a one-time setup to configure GCP to allow your machine to act as an endpoint, enabling research data transfer with your computer.

    ![!GCP Setup window with Log In button.](./images/gg-gcp-install/win/006-authenticate.png)

    Note that if you uninstall and reinstall GCP, you will need to complete this process again. You should not need to repeat this process otherwise.

1. Grant the required consents. This is required to set up your computer as an endpoint. Also provide a name for your endpoint. We recommend choosing a name that is short, memorable, and related to the purpose for the endpoint.

    ![!GCP Setup form with required consents and endpoint name field.](./images/gg-gcp-install/common/007-consents.png)

1. Enter the details for your GCP Collection, and click save to continue. The following list describes the fields in the form shown below.

    - **Owner Identity:** is the person responsible for this endpoint. This field should already be filled with UAB Campus or XIAS email address. If not, please that email address here.
    - **Collection Name:** is the name for the endpoint. This should be filled with the name of the endpoint from the previous step.
    - **Description:** Feel free to enter descriptive information about the endpoint here. This information will be displayed in the Globus Web App when the endpoint is viewed by others.
    - **High Assurance:** Only check this box if the endpoint has or will have PHI, HIPAA, or other protected data. If this is the case, please ensure that you have already completed a risk assessment with UAB Enterprise IT.

    ![!GCP Setup collection details](./images/gg-gcp-install/common/008-collection-details.png)

1. GCP Setup is now complete on your computer. Your computer is now a Globus endpoint and may be used to transfer data. Click "Exit Setup" to close the window.

1. After installation, you should see a lowercase letter "g" in a circle in your Windows system tray, typically at the bottom-right of the display. If you do not, try finding the Globus Connect Personal application in your start menu and starting the application.

    ![!GCP Icon in Windows system tray.](./images/gg-gcp-install/win/009-system-tray-icon.png)

Continue on with [How Do I Share Specific Folders Using Globus Connect Personal?](#how-do-i-share-specific-folders-using-globus-connect-personal) or return to the [Top of the Page](#globus-tutorials-for-research-groups).

### Installing GCP On MacOS

The following steps will guide you to install Globus Connect Personal (GCP) on your computer running MacOS.

1. Navigate to the [Globus Connect Personal official page](https://www.globus.org/globus-connect-personal) and scroll down to find the GCP MacOS version. Click on the "INSTALL NOW" button in the red box in the image below to be taken to the official installation instructions and download link for GCP for MacOS.

    ![!Globus Connect Personal official page showing operating system options with links. MacOS is the left of the three.](./images/gg-gcp-install/mac/001-select.png)

1. Click the `Download Globus Connect Personal` link on the instructions page, as shown below. This will redirect you to the GCP for MacOS installer.

    ![!Globus Connect Personal for MacOS official instructions page with link to download GCP for MacOS.](./images/gg-gcp-install/mac/002-instructions.png)

1. As shown in the image below, click the "Download Globus Connect Personal for MacOS" button to download the installer to download the installer to your computer.

    ![!Download GCP Installer for Windows](./images/gg-gcp-install/mac/003-download.png)

1. Find the installer on your computer and open it. A new window will pop-up asking you to drag the Globus Connect Personal app into the Application folder on your computer. Do so to install GCP.

    ![!Copy Mac GCP App into the Applications Folder](./images/gg-gcp-install/mac/004-install.png)

1. When the above step is completed navigate to your Application folder and look for the "Globus Connect Personal" application. Open it to proceed.

    ![!GCP application in the Applications Folder](./images/gg-gcp-install/mac/005-application.png)

1. When GCP has started, click on "Log In" to authenticate with Globus to begin the Collection setup process. This is a one-time setup to configure GCP to allow your machine to act as an endpoint, enabling research data transfer with your computer.

    ![GCP Setup window with Log In button.](./images/gg-gcp-install/mac/006-authenticate.png)

    Note that if you uninstall and reinstall GCP, you will need to complete this process again. You should not need to repeat this process otherwise.

1. Grant the required consents. This is required to set up your computer as an endpoint. Also provide a name for your endpoint. We recommend choosing a name that is short, memorable, and related to the purpose for the endpoint.

    ![!GCP Setup form with required consents and endpoint name field.](./images/gg-gcp-install/common/007-consents.png)

1. Enter the details for your GCP Collection, and click save to continue. The following list describes the fields in the form shown below.

    - **Owner Identity:** is the person responsible for this endpoint. This field should already be filled with UAB Campus or XIAS email address. If not, please that email address here.
    - **Collection Name:** is the name for the endpoint. This should be filled with the name of the endpoint from the previous step.
    - **Description:** Feel free to enter descriptive information about the endpoint here. This information will be displayed in the Globus Web App when the endpoint is viewed by others.
    - **High Assurance:** Only check this box if the endpoint has or will have PHI, HIPAA, or other protected data. If this is the case, please ensure that you have already completed a risk assessment with UAB Enterprise IT.

    ![!GCP Setup collection details](./images/gg-gcp-install/common/008-collection-details.png)

1. GCP Setup is now complete on your computer. Your computer is now a Globus endpoint and may be used to transfer data. Click "Exit Setup" to close the window.

1. After installation, you should see a lowercase letter "g" in a circle in your MacOS notification area, typically at the top-right of the display.

    ![!GCP Icon in MacOS notification area.](./images/gg-gcp-install/mac/009-notification-area-icon.png)

## How Do I Share Specific Folders Using Globus Connect Personal?

### On Windows

1. Open Globus Connect Personal: Open the GCP App, and/or click on the Globus icon in your taskbar.

    <!--![!GCP Logo shown in Taskbar](./images/gcp_logo_menu.png)-->

1. A drop-down menu containing a list of menu options would now be visible, click on "Options...":

    <!--![!GCP Options Menu](./images/gcp_collection_options.png)-->

1. A new window will appear showing a tab labelled "Access". In that window you would see an interface that requires configuration, the image has been labelled with numbers to provide details.
   - **(1).** Shows a list of filepath(s)/directory (or directories) you would like to share on Globus as a "Collection".
   - **(2).** and **(3).** Show the "Shareable" and "Writable" options to choose as you desire. The "Shareable" option will allow you to share this path on your local computer as an "Endpoint" that other users can access (This should be ticked, as you intend to share the "Collection"). The "Writable" option gives users permissions to upload, edit, or delete files, dependent on the level of access you grant individual users. These options can be selected for each file, folder or directory selected.
   - **(4).** Gives you the option to add several filepaths or directories to Globus as a Collection.
   - **(5).** Saves your preferred options.

    ![!GCP Access tab from the Options Menu](./images/gcp_collection_access.png)

1. The "General" tab should also be configured as shown in the image below.

   - **(1).** This allows you to specify whether you want Globus Connect Personal to run when Windows starts and allows you set, whether the software should automatically check for updates. Globus recommends that you leave the "Automatically check for updates" box checked, to ensure that you are running the most stable and secure version of Globus Connect Personal at all times.
   - **(2).** Allows you set what your "Collections" Home Folder would be.
   - **(3).** saves your selected preferred options.

    ![!GCP Web App showing search option in Collection](./images/gcp_collections_general.png)

### On MacOS

1. Click the Globus Connect Personal icon "g" in the menu bar at the top right of your screen and select "Preferences…​" to configure Globus Connect Personal.

    ![!GCP Mac Preferences Menu](./images/gcp_collection_preference.png)

    If you do not see the icon, go to your Applications folder and click on the Globus Connect Personal App. And repeat the above instructions.

    <!--![!GCP Mac App in the Applications Folder](./images/gcp_mac_app.png)-->

1. The "General" preferences tab shows a couple of options on how the GCP works on your local Mac computer. You can change the color of the Globus Connect Personal status icon in the menu bar by ticking the "Use black and white menu bar icons". You can also select the appropriate options for "Automatically check for updates" and "Automatically download updates", this way Globus Connect Personal would always run on the newest version. Globus recommends leaving the "Automatically check for update" option selected to automatically make important security updates.

    ![!General Preferences Tab in GCP Mac App](./images/gcp_mac_collection_general.png)

1. The "Access" preferences tab shows a list of folders that are accessible for file transfer and sharing via Globus Connect Personal. This provides more control over what information is accessible on your Globus Connect Personal endpoint. By default, your home directory (e.g.: /Users/`username`) is read/write accessible. The "Deny access to hidden (e.g. security) files in your home directory" option controls whether or not you can access hidden files (i.e. filenames beginning with "."") in your home directory. By default, Globus Connect Personal does not allow access to files like: `~/.globusonline` and `~/.ssh.`

    ![!Access Preferences Tab in GCP Mac App](./images/gcp_mac_collection_access.png)

### Accessing your Endpoint from the Web

The below steps apply to all GCP applications on all platforms (Linux, MacOS, and Windows).

1. Navigate to the Globus webpage, and authenticate if you have to. You would see the below image, showing the Globus web app, with all of its options. Click on the "Search" button in front of "Collection" from the "FILE MANAGER" menu option.

    ![!GCP Web App showing Collections](./images/gcp_web_collections_search.png)

1. This would open up a new interface, please select the "Your Collections" option, and you should see the `Endpoint` you created for your local machine.

    ![!GCP Web App showing created Endpoint](./images/gcp_web_endpoint.png)

As you begin to use Globus, your recently used "Collections" would appear in the "Recent" tab.

![!GCP Web App showing recently used Collections](./images/gcp_web_collections_recent.png)

1. Clicking on your `Endpoint` would open a new window showing you content from the `Collection` associated with the `Endpoint`. These will be the folders, directories or files you configured to be accessible to Globus from your local machine.

    ![!GCP Web App showing files in a Collection](./images/gcp_web_local_machine.png)

## What do I need to Share a GCP Endpoint?

Before you can share a GCP endpoint, ensure the you have the following:

1. **A Globus Account**: You must have a Globus account associated with UAB. There is a guide on how to do this here(./globus_individual_tutorial.md#how-do-you-get-on-globus)
1. **Membership of UAB High Assurance (HA) Subscription**: You must be added to the UAB High Assurance (HA) subscription group. Send an email to UAB IT support: <askIT@uab.edu> to approve and verify your inclusion in UAB's HA subscription group.

## How Do I Share a Collection with Others?

1. Navigate to the Globus Web App, and authenticate with your credentials. When you are logged in, click on "Collections".

    ![!GCP Web App showing Collection](./images/gcp_web_collection.png)

1. Click on the ">" button to the right of your screen.

    ![!GCP Web App highlighting button to configure Endpoint](./images/gcp_web_collection_share.png)

1. This would open an "Overview" page, that contains information specific to your `Endpoint`. You should also see a "Collections" tab, click on this.

    ![!GCP Web App showing Endpoint details](./images/gcp_web_endpoint_details.png)

1. Click on the "Add Guest Collection" button in the new window.

    ![!GCP Web App showing how to add a Shared Collection](./images/gcp_web_guest_collection.png)

1. Configure the "Collection" in the new window. Leave the path as is, you will include the specific filepath (folder/director or file) for this `Collection` in the next step. Fill out the optional information to properly label the `Collection`.

    ![!GCP Web App showing how to configure a Shared Collection](./images/gcp_web_config_collection.png)

1. In this step, include the filepath in the textbox provided (you can use the browse button to navigate to the appropriate folder), you should also see content for that folder/directory. Name your `Collection` and provide a description. Click on "Create Guest Collection".

    ![!GCP Web App showing how to configure a Shared Collection for the specific folder](./images/gcp_web_config_collection_name.png)

1. Now we have to set and grant permissions to our collaborators. Click the "Add Permissions - Share With" to configure the permissions for your just created `Collection`.

    ![!GCP Web App showing how to set permissions for a specific folder on a shared Collection](./images/gcp_web_config_permission.png)

    You can have different permissions for different collaborators accessing the same `Collection`. In the image below,
    - **(1).** Highlights how you can enter the filepath or use the "Browse" button to navigate your local machine to the folder or directory you would like to share.
    - **(2).** Gives you the option for which entities you would like to share your `Collection` with.
    - **(3).** This is where you would enter the Identity details for your collaborators (email address, Globus ID).
    - **(4).** These options grant the collaborator(s) `read` or `write` permissions access to your collection.
    - **(5).** Click the "Add Permission" button to complete the process or press cancel to restart configuration process.

    ![!GCP Web App showing each step to set permissions for a specific folder on a shared Collection](./images/gcp_web_collection_permission.png)
