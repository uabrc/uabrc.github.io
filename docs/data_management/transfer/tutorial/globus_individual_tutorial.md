
# Globus Tutorials for Individual Researchers

Do you have data and need to move it to a different computer system? Want to use a graphical interface to do it? Want a service that will attempt to resume interrupted transfers? Want enforced encryption for your transfers? Then Globus is right for you.

If you are new to Globus, you are in the right place. If you represent a group looking to share data with others we recommend following these tutorials with our [Globus Tutorials for Research Groups](./globus_organization_tutorial.md).

These tutorials are intended for individual researchers who need to move data from one location to another. If you manage a Research Core or lab and have never used Globus before, you'll want to start on this page. Then you will want to proceed to [Globus Tutorials for Research Groups](./globus_organization_tutorial.md).

The tutorials below will teach you how to effectively use Globus for managing and transferring research data. We will explore what Globus is, why you might use it, how it works, and we'll walk you through the essential steps to get started. You will learn how to set up your Globus account, access the Globus application, find Collections shared with you, and search for Collections by name.

Topics covered:

1. [Why Globus?](#why-globus)
1. [How Does Globus Work?](#how-does-globus-work)
1. [Tutorial Prerequisites](#tutorial-prerequisites)
1. [How Do I Get Onto the Globus Web App?](#how-do-i-get-onto-the-globus-web-app)
1. [How Do I Search for Collections by Name?](#how-do-i-search-for-collections-by-name)
1. [How Do I Find UAB Storage Collections?](#how-do-i-find-uab-storage-collections)
1. [How Do I Find Collections Shared with Me?](#how-do-i-find-collections-shared-with-me)
1. [How Do I Transfer between a Collection and Cheaha?](#how-do-i-transfer-between-a-collection-and-cheaha)
1. [How Do I Transfer between a Collection and LTS?](#how-do-i-transfer-between-a-collection-and-lts)
1. [How Do I Transfer between LTS and Cheaha?](#how-do-i-transfer-between-lts-and-cheaha)
1. [How Do I Check Transfer Status?](#how-do-i-check-transfer-status)

## Why Globus?

Globus is a data transfer ecosystem that simplifies the process of transferring, sharing, and managing large datasets. It is used by research institutions around the world to move research data between different storage devices, computer systems, and institutions. Globus has many research data oriented features, making it ideal for many research data transfer scenarios. Below is a list of features.

- Straight-forward, browser-based, graphical interface.
- Compatible with [UAB Box](https://www.uab.edu/it/home/tech-solutions/file-storage/box).
- Compatible with [Long-Term Storage](../../lts/index.md).
- Can be used with your laptop, desktop, or lab workstation via Globus Connect Personal (GCP).
- Transfers are automatically retried in the event of network or computer system outages.
- Transfers are encrypted end-to-end. Globus never sees your data.
- Suitable for transferring PHI and HIPAA data. Note: a UAB Enterprise IT risk assessment is required.

## How Does Globus Work?

Globus is an ecosystem of software intended to make research data transfer simpler. The Globus Web Application (Web App) at <https://app.globus.org> allows you to initiate transfers between any two Collections you have authorization to access. The Globus Connect Personal (GCP) software lets you turn any computer into a Globus Collection. At no point do Globus servers touch your research data. Instead, when you initiate a transfer between two Collections, the Globus application tells the two Collections that they need to talk to each other and data is sent directly between them. The Collections update the application with information you may need to know, such as how much data has transferred so far, how fast the transfer is proceeding, and any errors that occur. If the connection between Collections is interrupted for any reason, the Globus application will attempt to restart the transfer from where it left off.

## Tutorial Prerequisites

For these tutorials, you will need your BlazerID or [XIAS ID](../../../account_management/xias/index.md) and password to authenticate using UAB Single Sign-On (SSO).

## How Do I Get Onto the Globus Web App?

1. Use your browser to navigate to <https://app.globus.org>. You should see a login page like below.

    ![Globus Web App login page.](./images/gi-web-app/001-login.png)

1. To login, first you must find and select our institution. Type "UAB" or "University of Alabama at Birmingham" into the search bar to locate UAB in the list. The image below shows the correct choice in a red box.

    <!-- markdownlint-disable MD046 -->
    !!! note

        If you are an external collaborator using a [XIAS account](../../../account_management/xias/index.md) (this is uncommon) to interact with UAB-owned storage you will still need to search for "UAB". Do not use your home institution login to access UAB storage systems, as you will only have access to UAB storage with your XIAS credentials.
    <!-- markdownlint-enable MD046 -->

    ![Globus Web App login search bar with UAB entered and University of Alabama at Birmingham in a red box.](./images/gi-web-app/002-search.png)

1. Select "University of Alabama at Birmingham" from the drop-down menu.

    ![Globus Web App with University of Alabama at Birmingham selected showing activated Continue button.](./images/gi-web-app/003-select.png)

1. Click "Continue" to be taken to the UAB Single Sign-On (SSO) form. Enter your BlazerID and password in the SSO form, then click "Log In". Complete the login process as usual.

    ![UAB Single Sign-On form.](./images/gi-web-app/004-sso.png)

1. You should be taken to the File Manager page of the Globus Web App. We will be revisiting this page frequently throughout the tutorials. We highly recommend taking some time to familiarize yourself with the page as you proceed. The next few steps outline the important features of the File Manager page and its purpose.

    ![Globus Web App file manager single-panel view.](./images/gi-web-app/005-file-manager-single-panel.png)

1. Recall that Globus is a data transfer application. A data transfer means moving data between two computers: source and destination. As we learn more about Globus, data stored on the source and destination will be visible on the File Manager page in the panels in the screenshot above.

    By default, only one panel is visible. We recommend selecting two-panel view mode for improved ease of use. Select two-panel view mode by clicking the button located near the top right corner, as shown in the red box below. Of the three available view mode buttons, the two-panel view mode button is in the center.

    From here on, tutorials will assume you are using two-panel view mode when we refer to the File Manager page.

    ![Globus Web App file manager two-panel view.](./images/gi-web-app/006-view-buttons.png)

1. Now that two-panel view mode has been selected, you will see two sets of features and panels side-by-side. Most of these features will be used extensively when using Globus.

    - **(1) Collection Search bar**: Clicking here will open the Collection Search page, allowing you to find Collections of data shared by others, or find your own Collections. The next step will demonstrate features of the Collection Search page.
    - **(2) Path text field**: After a Collection has been selected using (1), this text field allows you to enter the path to a specific folder, updating the files and folders shown in (5).
    - **(3) Start Transfer button**: When you have selected files and folders in (5), use this button to start transferring.
    - **(4) Transfer Options drop down menu**: Various options for the transfer are available in this menu. These options are not commonly needed and are not used in the tutorials.
    - **(5) File Browser panel**: After a Collection has been selected in (1), a list of files and folders will appear here for the path shown in (2). You may navigate the Collection here like you would on your operating system.
    - **(6) Navigation panel**: The blue bar at the left hand side of the Globus Web App is the navigation panel. It will be referred to and used many times throughout these tutorials.

    ![Globus Web App file manager two-panel view.](./images/gi-web-app/007-file-manager-two-panel.png)

1. To better prepare you for what to expect, the screenshot below shows the File Manager page with an example Collection selected, called "my-gcp-collection". This example shows a path in the Path text field and contents in the File Browser panel.

    - **(1) Select All checkbox**: Select or unselect all files in the currently displayed folder.
    - **(2) Go Up One Level button**: Go to the folder containing the currently displayed folder.
    - **(3) Refresh button**: Refreshes the view of the currently displayed folder.
    - **(4) File Selection checkbox**: If checked, then the file is selected for transfer. This file is selected.
    - **(5) Folder Selection checkbox**: If checked, then the folder is currently selected for transfer. This folder is not selected.

    ![Globus Web App file manager two-panel view with Collection selected showing a file and folder.](./images/gi-web-app/008-file-manager-two-panel-example.png)

The File Manager page will be your most frequently-visited page when using Globus for data transfers. It is central to usage of the Globus Web Application. Please take some time to familiarize yourself with its look and feel. As you progress in the tutorials, please take time to experiment with transferring data to better understand how the interface works. Feel free to return here for guidance.

From here you can proceed to [How Do I Search for Collections by Name?](#how-do-i-search-for-collections-by-name)

[Return to the top](#globus-tutorials-for-individual-researchers).

## How Do I Search For Collections By Name?

Please follow these instructions to search for a specific Collection by name.

1. [Get onto the Globus Web App](#how-do-i-get-onto-the-globus-web-app).
1. You should see the File Manager page. If not click File Manager in the left-hand navigation panel.

    ![File Manager page.](./images/common/file-manager.png)

1. Click the Collection Search bar to open the Collection Search page.

    ![Collection search page](./images/common/collection-search-page.png)

1. In the example below, we typed "uab box" to search for the UAB Box Collection, which connects to UAB's Box.com service.

    ![Globus Collection search page showing results of searching for "UAB Box".](./images/gi-search-collections/003-results.png)

1. Click the name of the Collection to be taken back to the file manager page with the Collection filled in.

    ![File Manager page of the Globus Web App. One of the Collection Search bars is filled in with the previously selected Collection.](./images/gi-find-shared-collections/004-selected.png)

If you can't find a particular Collection this way, but know it was shared with you, try [finding Collections shared with me](#how-do-i-find-collections-shared-with-me). Proceed on to learn [how to find UAB storage Collections](#how-do-i-find-uab-storage-collections).

[Return to the top](#globus-tutorials-for-individual-researchers).

## How Do I Find UAB Storage Collections?

UAB offers [multiple storage resources](../../storage.md). The following resources may be accessed through Globus Collections.

- Cheaha file system (GPFS) including [individual directories](../../storage.md#what-individual-storage-solutions-are-available) and [project directories](../../storage.md#project-directory).
- [Long-Term Storage (LTS)](../../lts/index.md).
- [UAB Box](https://www.uab.edu/it/home/tech-solutions/file-storage/box).

To find these resources on Globus, use the following steps.

1. [Get onto the Globus Web App](#how-do-i-get-onto-the-globus-web-app).
1. You should see the File Manager page. If not click File Manager in the left-hand navigation panel.

    ![File Manager page.](./images/common/file-manager.png)

1. Click the Collection Search bar to open the Collection Search page.

    ![Collection search page](./images/common/collection-search-page.png)

1. In the search bar, type one of the following, depending on which resource you need, and select the appropriate entry.

    - **Cheaha Filesystem (GPFS)**: Type "UAB Cheaha". There are two Collections, choose one based on where the other computer is located.
        - **(1)** Transferring with a computer on the UAB Campus Network or UAB Wifi? Select "Cheaha cluster **on**-campus (UAB Science DMZ)".
        - **(2)** Transferring with a computer on other networks? select "Cheaha cluster **off**-campus (UAB Science DMZ)".

        ![UAB Box search results.](./images/gi-uab-collections/001-cheaha.png)

    - **Long-Term Storage (LTS)**: Type "UAB LTS" and select the entry labeled "UAB Research Computing LTS (Long Term Storage aka S3)".

        ![UAB Box search results.](./images/gi-uab-collections/002-lts.png)

    - **UAB Box**: Type "UAB Box" and select the entry labeled "UAB Box".

        ![UAB Box search results.](./images/gi-uab-collections/003-box.png)

Proceed on to learn [how to find Collections shared with you](#how-do-i-find-uab-storage-collections).

[Return to the top](#globus-tutorials-for-individual-researchers).

## How Do I Find Collections Shared with Me?

Globus allows users to share Collections with others. Other researchers, labs, and Research Cores on campus may invite you to their Collections to share data with you. The following instructions let you view Collections shared with you.

1. [Log in to Globus using your credentials](#how-do-i-get-onto-the-globus-web-app)
1. You should see the File Manager page. If not click File Manager in the left-hand navigation panel.

    ![File Manager page.](./images/common/file-manager.png)

1. Click the Collection Search bar to open the Collection Search page.

    ![Collection search page](./images/common/collection-search-page.png)

1. Click the Shared With You tab. The list of Collections will be filtered down to all Collections others have granted you access to, which should help you find the Collections you need.

    ![Collection Search page of Globus Web App. Shared With You tab is selected and the list of Collections has been filtered down.](./images/gi-find-shared-collections/003-list.png)

1. Click the name of the Collection to be taken back to the file manager page with the Collection filled in.

    ![File Manager page of the Globus Web App. One of the Collection Search bars is filled in with the previously selected Collection.](./images/gi-find-shared-collections/004-selected.png)

If you can't find a particular Collection this way, but know its name, try [searching for Collections](#how-do-i-search-for-collections-by-name).

Proceed on to learn how to transfer between Collections.

- [Between a Collection and Cheaha](#how-do-i-transfer-between-a-collection-and-cheaha)
- [Between a Collection and LTS](#how-do-i-transfer-between-a-collection-and-lts)
- [Between LTS and Cheaha](#how-do-i-transfer-between-lts-and-cheaha)

[Return to the top](#globus-tutorials-for-individual-researchers).

## How Do I Transfer between a Collection and Cheaha?

Please use the following instructions to transfer data from a shared Collection to [Cheaha GPFS](../../storage.md#what-type-of-storage-do-i-need). These instructions may also be used for other buckets on LTS, provided you have access and know their file path.

The direction of transfer may also be reversed to transfer data from Cheaha to the shared Collection. Note that some shared Collections may not allow you to transfer data back, such as some of those provided by Research Cores.

These instructions can be generalized to any two Collections you have access to on Globus.

1. [Log in to Globus using your credentials](#how-do-i-get-onto-the-globus-web-app).

1. Find a shared Collection [by filtering](#how-do-i-find-collections-shared-with-me) or [by searching](#how-do-i-search-for-collections-by-name) in the left side Collection Search bar.

1. Once you have selected the shared Collection you wish to transfer data from, repeat the process to [search](#how-do-i-search-for-collections-by-name) for a Cheaha Collection in the Collection Search bar on the right side of the file manager page. Search for "Cheaha cluster" to find them.

    Pay close attention in choosing which of the two you need. Choosing incorrectly could lead to slow transfers. Answer the following questions to help you decide. Is the first Collection you selected...

    - ...part of a lab or Research Core on campus? Select "on-campus".
    - ...on a computer on the UAB Campus Network or UAB Wifi or the UAB VPN? Select "on-campus".
    - ...at a different institution? Select "off-campus".
    - ...on a computer on a home network? Select "off-campus".

1. When you select a Cheaha Collection, or any other High Assurance (HA) Collection or Collection, you will be prompted to re-authenticate. Click the Continue button to do so, then select your UAB email address.

    ![High Assurance request for reauthentication.](./images/common/ha-authenticate.png)

    ![Identity selection showing a UAB email address.](./images/common/select-identity.png)

1. At this point, your file manager page should look something like the following image. At this point, both Collection Search bars should have a Collection or Collection filled in. The left side should be the Collection you wish to transfer from. The right side should be a Cheaha Collection. You should see files and folders on both sides.

    ![File Manager page showing a shared Collection and Cheaha Collection.](./images/gi-transfer-collection-to-cheaha/005-ready-to-select.png)

1. Locate the source path on the shared Collection side. Either type the path into the Path field manually, or use the graphical selection field to click on folder names to navigate the filesystem.

1. Repeat the process on the Cheaha Collection side to locate the destination path on the Cheaha Collection side.

1. Select the file and folders you wish to transfer on the shared Collection side. Do so by clicking the checkboxes next to the file and folder names.

    ![File Manager page with a file selected in the left selection area. The start button is boxed in red.](./images/gi-transfer-collection-to-cheaha/008-selection.png)

1. To start the transfer, click the "Start" button on the side you made your selections. A transfer will be started and you should see a green toast notification at the upper-right corner of the web page. Press the "X" button to dismiss the notification or click "View Details" to be taken to the Activity page to see more details about the transfer.

    ![File Manager page with a toast notification indicating the file transfer started successfully.](./images/gi-transfer-collection-to-cheaha/009-transfer-started.png)

From here you can proceed to other related tutorials to initiate other transfers or
[return to the index](#globus-tutorials-for-individual-researchers).

- [How Do I check transfer status?](#how-do-i-check-transfer-status)
- [How Do I Transfer Between a Collection and LTS?](#how-do-i-transfer-between-a-collection-and-lts)
- [How Do I Transfer Between LTS and Cheaha?](#how-do-i-transfer-between-lts-and-cheaha)

[Return to the top](#globus-tutorials-for-individual-researchers).

## How Do I Transfer between a Collection and LTS?

Please use the following instructions to transfer data from a shared Collection to a [bucket on LTS](../../lts/index.md). These instructions may also be used for other directories on Cheaha, provided you have access and know their file path.

The direction of transfer may also be reversed to transfer data from LTS to the shared Collection. Note that some shared Collections may not allow you to transfer data back, such as some of those provided by Research Cores.

These instructions can be generalized to any two Collections or Collections you have access to on Globus.

1. [Log in to Globus using your credentials](#how-do-i-get-onto-the-globus-web-app).

1. Find a shared Collection [by filtering](#how-do-i-find-collections-shared-with-me) or [by searching](#how-do-i-search-for-collections-by-name) in the left side Collection Search bar.

1. Once you have selected the shared Collection you wish to transfer data from, repeat the process to [search](#how-do-i-search-for-collections-by-name) for the LTS Collection in the Collection Search bar on the right side of the file manager page. Search for "UAB LTS" to find it.

1. When you select the LTS Collection, or any other High Assurance (HA) Collection or Collection, you will be prompted to re-authenticate. Click the "Continue" button to do so, then select your UAB email address.

    ![High Assurance request for reauthentication.](./images/common/ha-authenticate.png)

    ![Identity selection showing a UAB email address.](./images/common/select-identity.png)

1. At this point, your file manager page should look something like the following image. Both Collection Search bars should have a Collection or Collection filled in. The left side should be the Collection you wish to transfer from. The right side should be the Cheaha Collection. You should see files and folders on both sides.

    ![File Manager page showing a shared Collection and LTS Collection.](./images/gi-transfer-collection-to-lts/005-ready-to-select.png)

1. Locate the source path on the shared Collection side. Either type the path into the Path field manually, or use the graphical selection field to click on folder names to navigate the filesystem.

1. Repeat the process on the LTS Collection side to locate the destination path on the LTS Collection side.

1. Select the file and folders you wish to transfer on the shared Collection side. Do so by clicking the checkboxes next to the file and folder names.

    ![File Manager page with a file selected in the left selection area. The start button is boxed in red.](./images/gi-transfer-collection-to-lts/008-selection.png)

1. To start the transfer, click the "Start" button on the side you made your selections. A transfer will be started and you should see a green toast notification at the upper-right corner of the web page. Press the "X" button to dismiss the notification or click "View Details" to be taken to the Activity page to see more details about the transfer.

    ![File Manager page with a toast notification indicating the file transfer started successfully.](./images/gi-transfer-collection-to-lts/009-transfer-started.png)

From here you can proceed to other related tutorials to initiate other transfers or
[return to the index](#globus-tutorials-for-individual-researchers).

- [How do I check transfer status?](#how-do-i-check-transfer-status)
- [How Do I Transfer Between a Collection and Cheaha?](#how-do-i-transfer-between-a-collection-and-cheaha)
- [How Do I Transfer Between LTS and Cheaha?](#how-do-i-transfer-between-lts-and-cheaha)

[Return to the top](#globus-tutorials-for-individual-researchers).

## How Do I Transfer between LTS and Cheaha?

Please use the following instructions to transfer data from a [bucket on LTS](../../lts/index.md) to a project directory on Cheaha. These instructions may also be used for other buckets on LTS and directories on Cheaha, provided you have access and know their file paths.

The direction of transfer may also be reversed to transfer data from Cheaha to LTS.

These instructions can be generalized to any two Collections or Collections you have access to on Globus.

1. [Log in to Globus using your credentials](#how-do-i-get-onto-the-globus-web-app).

1. Find the LTS Collection by [searching](#how-do-i-search-for-collections-by-name) in the Collection Search bar on the left side of the file manager page. Search for "UAB LTS" to find it.

1. Once you have selected the LTS Collection, repeat the process to [search](#how-do-i-search-for-collections-by-name) for a Cheaha Collection in the Collection Search bar on the right side of the file manager page. Search for "Cheaha cluster" to find it.

    Pay close attention in choosing which of the two you need. Choosing incorrectly could lead to slow transfers. Answer the following questions to help you decide. Is the first Collection you selected...

    - ...part of a lab or Research Core on campus? Select "on-campus".
    - ...on a computer on the UAB Campus Network or UAB Wifi or the UAB VPN? Select "on-campus".
    - ...at a different institution? Select "off-campus".
    - ...on a computer on a home network? Select "off-campus".

1. Both the LTS and Cheaha Collections are High Assurance (HA) Collections and you will be prompted to re-authenticate. Click the "Continue" button to do so, then select your UAB email address.

    ![High Assurance request for reauthentication.](./images/common/ha-authenticate.png)

    ![Identity selection showing a UAB email address.](./images/common/select-identity.png)

1. At this point, your file manager page should look something like the following image. Both Collection Search bars should have a Collection or Collection filled in. The left side should be the LTS Collection. The right side should be a Cheaha Collection. You should see files and folders on both sides.

    ![File Manager page showing a shared Collection and LTS Collection.](./images/gi-transfer-lts-to-cheaha/005-ready-to-select.png)

1. Locate the source path on the LTS Collection side. Either type the path into the Path field manually, or use the graphical selection field to click on folder names to navigate the filesystem.

1. Repeat the process on the Cheaha Collection side to locate the destination path on the Cheaha Collection side.

1. Select the file and folders you wish to transfer on the shared Collection side. Do so by clicking the checkboxes next to the file and folder names.

    ![File Manager page with a file selected in the left selection area. The start button is boxed in red.](./images/gi-transfer-lts-to-cheaha/008-selection.png)

1. To start the transfer, click the "Start" button on the side you made your selections. A transfer will be started and you should see a green toast notification at the upper-right corner of the web page. Press the "X" button to dismiss the notification or click "View Details" to be taken to the Activity page to see more details about the transfer.

    ![File Manager page with a toast notification indicating the file transfer started successfully.](./images/gi-transfer-lts-to-cheaha/009-transfer-started.png)

From here you can proceed to other related tutorials to initiate other transfers or
[return to the index](#globus-tutorials-for-individual-researchers).

- [How do I check transfer status?](#how-do-i-check-transfer-status)
- [How Do I Transfer Between a Collection and Cheaha?](#how-do-i-transfer-between-a-collection-and-cheaha)
- [How Do I Transfer Between a Collection and LTS?](#how-do-i-transfer-between-a-collection-and-lts)

[Return to the top](#globus-tutorials-for-individual-researchers).

## How Do I Check Transfer Status?

To check the status of your transfers, please follow the instructions below.

1. [Log in to Globus using your credentials](#how-do-i-get-onto-the-globus-web-app).

1. In the Globus Web App, click "Activity" in the left navigation panel to go to the Activity page. There will be a list overview of transfers, with the most recent at the top.

    ![Globus Web App Activity page showing a successful transfer and failed transfer.](./images/gi-check-transfer-status/001-activity.png)

1. To see more details about a transfer, click the transfer title. There will be two tabs. The Overview tab will have information and statistics about the transfer. The Event Log tab will have information about events that occurred during transfer, including start, stop, and any errors. The Event Log is useful for diagnosing issues with failed transfers.

    ![Overview page for unsuccessful transfer.](./images/gi-check-transfer-status/002-status.png)

[Return to the top](#globus-tutorials-for-individual-researchers).
