
# Globus

In this tutorial, we will guide you on how to effectively use Globus for managing and transferring research data. We will explore what Globus is, why you might use it, and walk you through the essential steps to get started. You will also learn how to set up your Globus account, access the platform, find collections shared with you, and search for collections by name.

## Prerequisites

For this tutorial, you will need your BlazerID and password to authenticate using Single Sign-On (SSO).

## What is Globus, and Why Would You Use It?

Globus is a service that simplifies the process of transferring, sharing, and managing large datasets. It is widely used in research environments where data needs to be moved between different systems, institutions, or storage types.

### Key Features of Globus

- It ensures that your data is protected during transfers with encryption.
- It automatically retries failed transfers, and report the status of your data transfer.
- It simplifies complex transfer tasks with an intuitive web interface.
- It handles transfers of all sizes, from small files to multi-terabyte datasets.

## How Do I Get Onto the Globus Web App?

- To get to the Globus web app navigate to <https://app.globus.org>. You should see a page like below.

    ![Globus web app login page.](./images/gi-web-app-001-login.png)

- Type "UAB" or "University of Alabama at Birmingham" into the search bar to locate UAB in the list. The image below shows the correct choice in a red box.

    ![Globus web app login search bar with UAB entered and University of Alabama at Birmingham in a red box.](./images/gi-web-app-002-search.png)

- Select "University of Alabama at Birmingham" from the drop-down menu and click "Continue" to be taken to the UAB Single Sign-On (SSO) form.

    ![Globus web app with University of Alabama at Birmingham selected showing activated Continue button.](./images/gi-web-app-003-continue.png)

- Enter your BlazerID and password in the SSO form, then click "Log In".

    ![UAB Single Sign-On form.](./images/gi-web-app-004-sso.png)

- After logging in, you will be directed to the Globus file manager.

    ![Globus web app file manager single-panel view.](./images/gi-web-app-005-file-manager-single-panel.png)

- Enable two-panel view mode by clicking the button located near the top right corner, as shown in the red box below. Of the three available view mode buttons, the two-panel view button is in the center. This is an optional step, but highly recommended. This step will make your life much simpler while using Globus, now and in the future.

    ![Globus web app file manager two-panel view.](./images/gi-web-app-006-view-buttons.png)

- On the file transfer page, you will see two file browser windows: one on the left and one on the right. Each window will have an Endpoint field representing the two systems between which you wish to transfer files. Once set up, you can transfer files in either direction.

    ![Globus web app file manager two-panel view.](./images/gi-web-app-007-file-manager-two-panel.png)

The file manager will be your most frequently-visited page when using Globus for data transfers. It is central to usage of the Globus web application.Please take some time to familiarize yourself with its look and feel. As you progress in the tutorials, please take time to experiment with transferring data to better understand how the interface works.

## How to Find Collections Shared with You

Globus allows users to share collections with others and also view what is shared with you. To view collections shared with you, please follow these steps:

- Log in to Globus using your credentials.

- From the Globus dashboard, on the left sidebar of the Globus Web App, click on the "Collections" menu.

<!--
 ![file-manager-page-search](/image/collection-search-menu.png)
-->

- Then, click the "Shared with You" button located in the top-right corner. This filter will display all collections that have been shared specifically with your account.

<!--
![shared-with-you](/image/collection-shared-with-you.png)
-->
## How to Search for Collections by Name

To find a specific collection by name, follow these steps:

- Log in to Globus and click on the "File Manager" from the dashboard, as shown below.

<!--
 ![file-manager](/image/file-manager-globus.png)
-->

- In the File Manager, click the collection search window, as shown below.

<!--
 ![click-search-field](/image/click-on-search-bar.png)
-->

- Enter the name (or part of the name) of the collection you are looking for in the search bar.

<!--
 ![collection-search-bar](/image/collection-search-bar.png)
-->

- Once the search results appear, click on the desired collection to access or transfer files.

<!--
  ![collection-results](/image/collection-results.png)
-->

## How to transfer data from a shared collection to my project directory on Cheaha?

To transfer data from a shared collection to a project directory on Cheaha, you may follow these steps:

1. Select the Shared Collection:  Click on the Collection tab, then go to the "Shared With You" section and choose the appropriate collection name, for instance, "test collection cheaha". Once selected, you will see the data shared with you.

1. On the other side of the Collection tab, select the UAB Cheaha collection. Authenticate your account if prompted, and navigate to your project directory, e.g., `/data/project/xxx`, where you want to transfer the data.

1. Start the Transfer: Click the "Start" button on the shared collection side. The data, such as the folder `test`, will then be transferred to your specified project directory.

<!--
![!Globus Shared Collection](./images/globus-shared-collection.png)
-->

<!--
![!Globus Transfer Shared Collection To Cheaha Projdir](./images/globus-transfer-shared-collection-to-cheaha-projdir.png)
-->

## How to transfer data from a shared collection to my group's LTS allocation?

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
