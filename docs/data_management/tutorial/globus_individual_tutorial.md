
# Globus Tutorials for Individual Researchers

These tutorials are intended for individual researchers who want to use Globus to do the following.

- Transfer research data for their own use or for laboratory use.
- Receive data from other individuals, labs, or Research Cores.

If you need tutorials on using Globus for Research Core data management, please see our [Globus Tutorials for Research Groups](./globus_group_tutorial.md).

The tutorials below will teach you how to effectively use Globus for managing and transferring research data. We will explore what Globus is, why you might use it, and walk you through the essential steps to get started. You will learn how to set up your Globus account, access the Globus application, find collections shared with you, and search for collections by name.

## Prerequisites

For these tutorials, you will need your BlazerID or [XIAS ID](../../account_management/xias/index.md) and password to authenticate using UAB Single Sign-On (SSO).

## What is Globus?

Globus is a data transfer ecosystem that simplifies the process of transferring, sharing, and managing large datasets. It is used by research institutions around the world to move research data between different storage devices, computer systems, and institutions.

## Why use Globus?

Globus has many research data oriented features, making it ideal for many research data transfer scenarios. Below is a list of features.

- Straight-forward, browser-based interface.
- Compatible with [UAB Box](https://www.uab.edu/it/home/tech-solutions/file-storage/box).
- Compatible with [Long-Term Storage](../lts/index.md).
- Can be used with your laptop, desktop, or lab workstation via Globus Connect Personal (GCP).
- Transfers are automatically retried in the event of network or computer system outages.
- Transfers are encrypted end-to-end. Globus never sees your data.
- Suitable for transferring PHI and HIPAA data. Note: a UAB Enterprise IT risk assessment is required.

## How Does Globus Work?

Globus is an ecosystem of software intended to make research data transfer simpler. The Globus web application at <https://app.globus.org> allows you to initiate transfers between any two endpoints you have authorization to access. The Globus Connect Personal (GCP) software lets you turn any computer into a Globus endpoint. At no point do Globus servers touch your research data. Instead, when you initiate a transfer between two endpoints, the Globus application tells the two endpoints that they need to talk to each other and data is sent directly between them. The endpoints update the application with information you may need to know, such as how much data has transferred so far, how fast the transfer is proceeding, and any errors that occur. If the connection between endpoints is interrupted for any reason, the Globus application will attempt to restart the transfer from where it left off.

## How Do I Get Onto the Globus Web App?

1. To get to the Globus web app navigate to <https://app.globus.org>. You should see a page like below.

    ![Globus web app login page.](./images/gi-web-app/001-login.png)

1. Type "UAB" or "University of Alabama at Birmingham" into the search bar to locate UAB in the list. The image below shows the correct choice in a red box.

    ![Globus web app login search bar with UAB entered and University of Alabama at Birmingham in a red box.](./images/gi-web-app/002-search.png)

1. Select "University of Alabama at Birmingham" from the drop-down menu and click "Continue" to be taken to the UAB Single Sign-On (SSO) form.

    ![Globus web app with University of Alabama at Birmingham selected showing activated Continue button.](./images/gi-web-app/003-continue.png)

1. Enter your BlazerID and password in the SSO form, then click "Log In".

    ![UAB Single Sign-On form.](./images/gi-web-app/004-sso.png)

1. After logging in, you will be directed to the Globus file manager.

    ![Globus web app file manager single-panel view.](./images/gi-web-app/005-file-manager-single-panel.png)

1. Enable two-panel view mode by clicking the button located near the top right corner, as shown in the red box below. Of the three available view mode buttons, the two-panel view button is in the center. This is an optional step, but highly recommended. This step will make your life much simpler while using Globus, now and in the future.

    ![Globus web app file manager two-panel view.](./images/gi-web-app/006-view-buttons.png)

1. On the file transfer page, you will see two file browser windows: one on the left and one on the right. Each window will have an Endpoint field representing the two systems between which you wish to transfer files. Once set up, you can transfer files in either direction.

    ![Globus web app file manager two-panel view.](./images/gi-web-app/007-file-manager-two-panel.png)

The file manager will be your most frequently-visited page when using Globus for data transfers. It is central to usage of the Globus web application.Please take some time to familiarize yourself with its look and feel. As you progress in the tutorials, please take time to experiment with transferring data to better understand how the interface works.

[Return to the index.](#globus-tutorials-for-individual-researchers)

## How Do I Find Collections Shared with Me?

Globus allows users to share collections with others. Other researchers, labs, and Research Cores on campus may invite you to their collections to share data with you. The following instructions let you view collections shared with you.

1. [Log in to Globus using your credentials.](#how-do-i-get-onto-the-globus-web-app)

1. In the Globus web app, click "Collections" in the left navigation panel to go to the collections page, then click the "Shared With You" button shown in the red box in the image below.

    ![Collections page of Globus web app. "Shared With You" button is boxed in red.](./images/gi-find-collections/001-search.png)

1. The list of collections will be filtered down to all collections others have granted you access to, which should help you find the collections you need.

    ![Collections page of Globus web app. "Shared With You" button is selected and the list of collections has been filtered down.](./images/gi-find-collections/002-list.png)

If you can't find a particular collection this way, but know its name, try [searching for collections](#how-do-i-search-for-collections-by-name) or [return to the index](#globus-tutorials-for-individual-researchers).

## How Do I Search For Collections By Name?

Please follow these instructions to search for a specific collection by name.

1. [Log in to Globus using your credentials.](#how-do-i-get-onto-the-globus-web-app).
1. In the Globus web app, click "File Manager" in the left navigation panel to go to the file manager page, then click the "Collection Search" shown in the red box in the image below.

    ![Globus file manager page showing collection search bar in a red box.](./images/gi-search-collections/001-search-bar.png)

1. You will be taken to a collection search page. Enter part or all of the name of the collection you are searching for in the search box on this new page.

    ![Globus collection search page.](./images/gi-search-collections/002-collection-search.png)

1. Search results should appear. In the example below, we located the UAB Box collection, which connects to UAB's Box.com service.

    ![Globus collection search page showing results of searching for "UAB Box".](./images/gi-search-collections/003-results.png)

If you can't find a particular collection this way, but know it was shared with you, try [finding collections shared with me](#how-do-i-find-collections-shared-with-me) or [return to the index](#globus-tutorials-for-individual-researchers).

## How Do I Transfer from a Collection to Cheaha?

Please use the following instructions to transfer data from a shared collection to a project directory on Cheaha. These instructions may also be used for other directories on Cheaha, provided you have access.

1. [Find a collection shared with me](#how-do-i-find-collections-shared-with-me) or [Search for a collection by name](#how-do-i-search-for-collections-by-name).

1. Select the Shared Collection:  Click on the Collection tab, then go to the "Shared With You" section and choose the appropriate collection name, for instance, "test collection cheaha". Once selected, you will see the data shared with you.

1. On the other side of the Collection tab, select the UAB Cheaha collection. Authenticate your account if prompted, and navigate to your project directory, e.g., `/data/project/xxx`, where you want to transfer the data.

1. Start the Transfer: Click the "Start" button on the shared collection side. The data, such as the folder `test`, will then be transferred to your specified project directory.

<!--
![!Globus Shared Collection](./images/globus-shared-collection.png)
-->

<!--
![!Globus Transfer Shared Collection To Cheaha Projdir](./images/globus-transfer-shared-collection-to-cheaha-projdir.png)
-->

## How Do I Transfer from a Collection to LTS?

To transfer data from a shared collection to the UAB Long Term Storage (LTS) lab space, start by selecting the LTS lab space collection and authenticating your identity. On the other end of the panel, click the collection and go to "Shared With You" tab and select the shared allocation, such as "test_lts_collection." Set the desired source and destination paths for both collections before proceeding with the transfer.

Once everything is set, click the "Start" button on the shared collection panel to begin the transfer process, which will start automatically. You can monitor the progress by clicking the "refresh list" button on the lab space end to verify that the changes have been made.

<!--
![!Globus LTS Shared Collection](./images/globus-lts-shared-collection.png)
-->

<!--
![!Globus LTS Shared Collection Transfer Group Space](./images/globus-lts-shared-collection-transfer-group-space.png)
-->

## How to transfer data between LTS and Cheaha?

You can transfer data between LTS and Cheaha using Globus. To do this, select the LTS collection on one side and the Cheaha collection on the other side in the transfer panel interface, and authenticate the identity.

To transfer data from LTS to Cheaha, make sure the paths are correctly set on both ends by navigating to the appropriate folders. Select the files or folders from the LTS side and click the "Start" button on the left-hand side panel. The data will be transferred and will appear in the right-hand side panel, which corresponds to the Cheaha end.

<!--
![!Globus Transfer Data From LTS To Cheaha](./images/globus-transfer-lts-to-cheaha.png)
-->

Alternatively, to transfer data from Cheaha to LTS, follow the same procedure. Select the files or folders from the Cheaha side and click the "Start" button on the right-hand side panel. The data will then be transferred and will appear in the left-hand side panel, which corresponds to the LTS end.

<!--
![!Globus Transfer Data From Cheaha To LTS](./images/globus-transfer-cheaha-to-lts.png)
-->
