# Globus Tutorials for UAB Research Organizations

This tutorial is designed to guide UAB research managers, such as Lab PIs, Core Directors, and their management staff, to help them set up and use Globus Connect Personal (GCP) for secure data sharing on their local/personal computers. GCP allows you to share data with collaborators efficiently meeting security and compliance standards for file sharing.

If you are new to Globus, we recommend starting with our [Globus Tutorials for Individual Researchers](../globus/globus_individual_tutorial.md) first to familiarize yourself with how Globus is used. When those are complete, we then recommend following the tutorials on this page in order from start to finish, as later tutorials assume the previous tutorials have been completed.

Topics covered:

1. [Why Globus?](#why-globus)
1. [How Does Globus Work?](#how-does-globus-work)
1. [Tutorial Prerequisites](#tutorial-prerequisites)
1. [How Do I Get onto the Globus Web App?](#how-do-i-get-onto-the-globus-web-app)
1. [How Do I Find Collections I Created or Own?](#how-do-i-find-collections-i-created-or-own)
1. [How Do I Enable Sharing for My Globus Account?](#how-do-i-enable-collection-sharing-for-my-globus-account)
1. [How Do I Create a Collection?](#how-do-i-create-a-collection)
1. [How Do I Share a Collection with Others?](#how-do-i-share-a-collection-with-others)
1. [How Do I Share Data with a Research Core Customer?](#how-do-i-share-data-with-a-research-core-customer)

## Why Globus?

Globus is a data transfer ecosystem that simplifies the process of transferring, sharing, and managing large datasets. It is used by research institutions around the world to move research data between different storage devices, computer systems, and institutions. Globus has many research data oriented features, making it ideal for many research data transfer scenarios. Below is a list of features.

- Straight-forward, browser-based interface.
- Compatible with [Long-Term Storage](../../storage/lts/index.md).
- Can be used to share data with Research Core customers.
- Can be used to transfer data between lab workstations, servers, and Cheaha.
- Transfers are automatically retried in the event of network or computer system outages.
- Transfers are encrypted end-to-end. Globus never sees your data.
- Suitable for transferring PHI and HIPAA data. Note: a UAB Enterprise IT risk assessment is required.

## How Does Globus Work?

Globus is an ecosystem of software intended to make research data transfer simpler. The Globus Web Application (Web App) at <https://app.globus.org> allows you to initiate transfers between any two Collections you have authorization to access. The Globus Connect Personal (GCP) and Globus Connect Server (GCS) software let you turn any computer into a Globus Collection. At no point do Globus servers touch your research data. Instead, when you initiate a transfer between two Collections, the Globus application tells the two Collections that they need to talk to each other and data is sent directly between them. The Collections update the application with information you may need to know, such as how much data has transferred so far, how fast the transfer is proceeding, and any errors that occur. If the connection between Collections is interrupted for any reason, the Globus application will attempt to restart the transfer from where it left off.

## Tutorial Prerequisites

For these tutorials, you will need your BlazerID or [XIAS ID](../../../account_management/xias/index.md) and password to authenticate using UAB Single Sign-On (SSO).

## How Do I Get Onto the Globus Web App?

To learn how to get onto the Globus Web App [Globus Tutorials for Individual Researchers Page](../globus/login_to_globus.md#how-do-i-get-onto-the-globus-web-app). Please visit that link and then return here when you have finished.

[Return to the top](#globus-tutorials-for-uab-research-organizations).

## How Do I Find Collections I Created or Own?

To find a Collection you own, use the following steps.

1. Navigate to the [Globus Web App](#how-do-i-get-onto-the-globus-web-app) using your browser. You should be at the File Manager page.

    ![File Manager page of the Globus Web App](../images/common/file-manager.png)

1. Click either of the Collection Search bar at the top of the File Manager page. This will take you to the Collection Search page.

    ![Collection Search page of the Globus Web App](../images/common/collection-search-page.png)

1. Click the Your Collections tab to display a list of Collections you have created or own.

    ![Your Collections tab showing a GCP Collection.](../images/go-my-collections/003-your-collections.png)

1. From here there are two options:

    1. Click the name of the Collection to select it for a file transfer and be taken back to the File Manager page.

        ![File Manager page showing selected Collection on left-hand panel.](../images/go-my-collections/004-file-manager-selection-made.png)

    1. Click the three dots icon at the right side of the entry to be taken to the Collection details page.

        ![Collectionm details page with overview tab selected.](../images/go-my-collections/005-collection-details-page.png)

[Return to the top](#globus-tutorials-for-uab-research-organizations).

## How Do I Enable Collection Sharing for My Globus Account?

Before you can share Collections from your Globus Connect Personal (GCP) Collection with others, you must do a one-time setup for your account. You will need to join the "University of Alabama at Birmingham (HA)" (UAB HA) subscription group. Sharing any Collection requires a paid subscription with Globus. UAB Research Computing has a subscription, but Globus does not know your BlazerID is part of our subscription until you join the subscription group. So, Globus also does not know the GCP Collection you created is part of our subscription. By joining our UAB HA group, you and your GCP Collection are confirmed to be part of our subscription, and you can share Collections from the GCP Collection.

To join the UAB HA group, we need to receive both a UAB support request, and a request to join the UAB HA group within the Globus Web App. We need both because we sometimes get spam applications through Globus. Having a Support Request helps us filter the spam. Please use the following steps to join.

1. Submit a [Support Request](../../../help/support.md#how-do-i-create-a-support-ticket). In the request please include the following.

    - Your BlazerID.
    - The text "Please add me to the Globus UAB HA subscription group."
    - The reason you need to be able to share a Collection in Globus. For Research Cores, this would be to share data with your customers.

1. In your browser [get onto the Globus Web App](#how-do-i-get-onto-the-globus-web-app).
1. In the left hand navigation panel click "Groups" to be taken to the Groups page.

    ![Globus groups page with no groups.](../images/go-uab-ha-group-access/001-groups-page.png)

1. Ensure the "MY GROUPS" box is unchecked. In the "Filter groups" search bar enter "University of Alabama at Birmingham" to locate the "University of Alabama at Birmingham (HA)" (UAB HA) group.

    ![Globus group page showing search results with University of Alabama at Birmingham (HA) listed](../images/go-uab-ha-group-access/002-groups-search.png)

1. Click on the UAB HA group name to be taken to the group details page. The Overview tab should be selected.

    ![UAB HA subscription group details page with overview tab selected.](../images/go-uab-ha-group-access/003-uab-ha-overview.png)

1. Click on the "Join this Subscription" button to be taken to the form to submit a request to join.

    ![UAB HA subscription group join request form.](../images/go-uab-ha-group-access/004-join-form.png)

1. Fill in the form fields and click the "Submit Application" button when completed. This will send you to a page notifying you that your membership is pending. A request has been sent to Research Computing, so please wait until you see a reply in the support request.

    ![Notice of pending membership.](../images/go-uab-ha-group-access/005-pending.png)

1. When your membership has been accepted, you can verify by [returning to the Globus Web App](#how-do-i-get-onto-the-globus-web-app) and navigating to the Groups page. Check the "MY GROUPS". You should see "University of Alabama at Birmingham (HA)" listed with a green, circled checkmark and the word "ACTIVE".

    ![Groups page with my groups checked showing UAB HA subscription group](../images/go-uab-ha-group-access/006-my-groups.png.png)

When you have completed the steps in this section, proceed to [creating a Collection](#how-do-i-create-a-collection).

[Return to the top](#globus-tutorials-for-uab-research-organizations).

## How Do I Create a Collection?

There are three ways to create a Collection.

- Start from [an existing Collection you created or own](#how-do-i-find-collections-i-created-or-own).
- [Install Globus Connect Personal](../globus/gcp_install.md#how-to-install-globus-connect-personal-gcp) and [share a folder](../globus/gcp_setup.md#how-do-i-choose-specific-folders-to-share-using-globus-connect-personal) to create a Collection.
- Install and configure one or more Collections with Globus Connect Server. To do this, please [Contact Support](../../../help/support.md#how-do-i-create-a-support-ticket) to start a discussion.

The instructions below assume you are starting from an existing Collection. The instructions will work to create a subset of your Globus Connect Personal Collection.

1. [Get onto the Globus Web App](#how-do-i-get-onto-the-globus-web-app).
1. [Find the existing Collection](#how-do-i-find-collections-i-created-or-own) and access its details page.
1. Click the "Collection" tab.

    ![Overview tab of details page with Collection tab to the right.](../images/go-create-collection/001-collection-tab.png)

1. Click the "+ Add Guest Collection" button to be taken to a form to create the new Collection.

    ![Collection tab of details page with Add Guest Collection button.](../images/go-create-collection/002-add-guest-collection.png)

1. Fill out the form.

    - **(1) You Are Sharing**: Shows which Collection you will be sharing all or part of. Helpful to verify you are sharing the right Collection
    - **(2) Path**: Which path you wish to share. By default, the "/" path is the root of the original Collection. This may not be appropriate for your use case. Generally, when creating one Collection from another, you will want to pick a subfolder of the original Collection. Do this with the "Browse" button.
    - **(3) Display Name**: The name people will see when accessing this Collection, and what they will search for when looking for the Collection.
    - **(4) Description**: An optional description for the Collection.
    - **(5) Keywords**: Optional keywords to help locating the Collection. May be useful for broadly or publicly shared data.

    ![Collection creation form.](../images/go-create-collection/003-form.png)

1. Click the "Create Guest Collection" button to create the Collection. You will be taken to the details page of the new Collection, on the Permissions tab.

    ![Permissions tab of new Collection details page.](../images/go-create-collection/004-completion.png)

When you have created a Collection, you are ready to [share the Collection with others](#how-do-i-share-a-collection-with-others).

[Return to the top](#globus-tutorials-for-uab-research-organizations).

## How Do I Share a Collection With Others?

Before sharing a Collection with others, you will need to first [create a Collection](#how-do-i-create-a-collection) you administer. If the Collection is a [Globus Connect Personal Collection](../globus/gcp_install.md#how-to-install-globus-connect-personal-gcp), then you will also need to [enable Collection sharing for your Globus account](#how-do-i-enable-collection-sharing-for-my-globus-account). If these prerequisites have been met, then you are ready to setup a Collection to be shared with others. Please follow the instructions below.

1. [Get onto the Globus Web App](#how-do-i-get-onto-the-globus-web-app).
1. [Find the Collection](#how-do-i-find-collections-i-created-or-own) you wish to share. In this case we are looking for the "customer-share" Collection.
1. On the "customer-share" Collection details page, click the Permissions tab.

    ![Collection details page overview tab.](../images/go-share-collection/001-collection-details-overview.png)

1. Click the "Add Permissions &ndash; Share With" button.

    ![Collection details page permissions tab.](../images/go-share-collection/002-collection-details-permissions-before.png)

1. Fill in the form.

    - **Path** defaults to the root of the Collection. This may or may not be acceptable for your use case. Be sure to limit access to only the data that needs to be shared. Use the file browser available in the form to find the correct level of access. For now grant permission to the default.
    - **Share With**: radio buttons to provide control over who to share with. In almost all cases, you will want to share with a single user, which is what we will show here.
        - **User**: Use the "User" search bar to find the specific user you wish to share with. If they have never accessed Globus before, they will not appear in the search results. You can safely enter their email address to add them anyway. For now grant permission to yourself for the purposes of experimenting.
    - **Email Notification** checkbox. We recommend sending an email notification as a convenience.
        - **To** entry field: who to send the email to. We recommend the same person as the "User" selected earlier. There may be future cases where you want to notify others, such as a supervisor, as well.
        - **Message** text entry field: the optional content to send in the email message.
    - **Permissions** The "read" permission must be granted, as that is the point of sharing the Collection. You may additionally give "write" permission to create a two-way collaboration. We recommend Research Cores not grant "write" permission. If you are using a Globus Connect Personal Collection, then "write" permission requires you to correctly [configure your Collection](../globus/gcp_setup.md#how-do-i-choose-specific-folders-to-share-using-globus-connect-personal) to make your shared folder writable.

    ![Add permissions form.](../images/go-share-collection/003-add-permissions-form.png)

1. Click the "Add Permission" button to grant permission. You should see a notification confirming the permissions granted. At this point permissions have been granted and the Collection is shared with another person. If you need to add more people, click the "Add another Permision" button and repeat the process. Otherwise click "Done". For now click "Done".

    ![Permission confirmation notification.](../images/go-share-collection/004-permissions-confirmation.png)

1. When you click "Done" you should be taken back to the Permissions tab of the Customer Share page. You should see a new entry with "Path: /". If you click the drop-down arrow you will see yourself listed with "Read" permission. If you need to revoke permissions, return to this page and click the icon that looks like a trash can.

    ![Collection details page permissions tab showing new entry.](../images/go-share-collection/005-colection-details-permissions-after.png)

[Return to the top](#globus-tutorials-for-uab-research-organizations).

## How Do I Share Data With a Research Core Customer?

If you manage data for a Research Core, please [Contact Support](../../../help/support.md#how-to-request-support) to start a conversation. The answer to this question is currently being developed, so we will need to work together to find the ideal solution.

[Return to the top](#globus-tutorials-for-uab-research-organizations).
