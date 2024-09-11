
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

## Why You Use Globus?

- Globus is optimized for high-performance environments, reducing transfer times.
- It has a GUI and is accessible via a web browser, making it easy to initiate transfers from anywhere.
- Globus allows you to easily share data with collaborators, regardless of their institution.

## How Do You Get Onto Globus?

Getting started with Globus involves a few steps. Here is how you can set up your account and start using the platform:

- To get to the Globus Web App, navigate to [https://app.globus.org](https://app.globus.org), and you will land on a page as shown below.

<!--
    ![first-page-globus](/image/first-page-globus.png)
-->

- Type your institution's name or a part of it in the search bar. For example,  if you type "UAB", it will match entries like "University of Alabama at Birmingham", as shown below.

<!--
  ![login-page-globus](/image/enter-institution-page-globus.png)
-->

- Select your institution from the drop-down menu and click "Continue" as shown below.

<!--
  ![login-page-globus](/image/continue-button-page-globus.png)
-->

- Enter your BlazerID and password, then click "Log in".

<!--
![login-page-uab](/image/authentication-page-uab.png)
-->

- After logging in, you will be directed to the Globus file manager.

<!--
  ![file-manager-page-globus](/image/file-manager-page-globus.png)
-->

- Enable two-panel mode by toggling the switch located near the top right corner, as shown below.

<!--
  ![two-panel-mode-toggle](/image/two-panel-mode-toggle.png)
-->

- Then, on the file transfer page, you will see two file browser windows: one on the left and one on the right. Each window will have an Endpoint field representing the two systems between which you wish to transfer files. Once set up, you can transfer files in either direction.

<!--
  ![two-file-browser-windows](/image/two-file-browser-windows.png)
-->

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
