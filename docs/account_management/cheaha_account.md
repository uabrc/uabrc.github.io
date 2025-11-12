---
toc_depth: 3
---

# Cheaha Account Management

These instructions are intended to guide researchers on creating new accounts and managing existing accounts.

## Creating a New Account

Creating a new account is a simple, automated, self-service process. To start, navigate to <https://rc.uab.edu>, our [Open OnDemand](../cheaha/open_ondemand/index.md) web portal, and authenticate. The authentication process differs depending on your affiliation. Accounts are available to researchers with the following situations.

- If you are affiliated with UAB and have a BlazerID, please authenticate using Single Sign-On (SSO).
- If you are affiliated with UAB Medicine, you will need to use your BlazerID to authenticate via Single Sign-On (SSO) instead of your UABMC authentication process.
- If you are an external collaborator and have a XIAS account with access to Cheaha, please authenticate using your XIAS email address as the ID, not automatically generated `xias-XXXXXX-1` ID.
- If you are an external collaborator and do not have a XIAS account, you will need a UAB-affiliated sponsor and will need to follow our [XIAS Guest Account Instructions](xias/guest_instructions.md). Your sponsor will need to follow our [XIAS Site Management](xias/pi_site_management.md) and [XIAS Guest Management](xias/pi_guest_management.md) documentation pages.

Once you have authenticated, you should see a page that looks like the following.

![!UAB self registration page.](./images/uab_self_register_001.png)

The form should be prefilled with your BlazerID or XIAS ID, full name, and email address. If any of these details are incorrect please [Contact Support](../help/support.md). Please also fill out the reason you wish to create an account. To create a Cheaha account, you must check both boxes affirming your acceptance of relevant UAB IT policies. Until both boxes are checked, the "Create Account" button will not be usable.

When you are ready, click "Create Account" to start the account creation process. You should see a popup notification that looks like the following. After a few moments you should be redirected to our [Open OnDemand](../cheaha/open_ondemand/index.md) web portal. If not, please [Contact Support](../help/support.md).

![!Account creation notification popup](images/uab_self_register_002.png)

Welcome to Cheaha and to Research Computing!

## Managing an Existing Account

If you already have an account and wish to check it's status, please visit your account status page at <https://rc.uab.edu/account>.

### Account in Good Standing

If your account is in good standing you should see a page like the following.

![!Account in good standing page.](images/uab_good_standing.png)

### Account Requires Certification

We review accounts periodically to ensure the system is being used fairly and as intended. Part of this process is to certify that researchers with accounts still wish to make use of Cheaha. Once per year every researcher will be required to certify their account before making use of Cheaha. In addition, all accounts require certification after being placed on hold (see our [Account on Hold section](#account-on-hold)). This way, we ensure users are engaged in the process of reactivating their account to use our resources. If your account requires certification, you will see the below notification page when logging into our [Open OnDemand](../cheaha/open_ondemand/index.md) web portal.

![!Account certification notification page.](images/uab_certify_001.png).

To certify your account, click the button to be taken to the certification form, which should look like the following.

![!Account certification form.](images/uab_certify_002.png)

While the certification form looks similar to the new account creation form, please be sure to review all of the information carefully. To certify your account, you must check both boxes affirming your acceptance of relevant UAB IT policies. Until both boxes are checked, the "Create Account" button will not be usable.

When you are ready, click "Certify Account" to start the account creation process. You should see a popup notification confirming the process is working. After a few moments your account should be certified and you will be free to use Cheaha again. If not, please [Contact Support](../help/support.md).

### Account on Hold

Mistakes happen, and sometimes what we thought we programmed wasn't quite what we actually programmed. When these kinds of mistakes occur, excess resources may get used. If this impacts performance or other users excessively, we may put a hold on your account. We may also put a hold on your account if you do not complete [Account Certification](#account-requires-certification) when required.

Other reasons for holds include, but are not limited to:

- Inactivity: extended account inactivity.
- Affiliation: [end of affiliation with, or employment by, UAB](./leaving_uab.md).
- Subscription: unsubscribing from the `hpc-announce LISTSERV` mailing list.
- Non-compliance:
    - Misuse of Research Computing resources.
    - [IT Policy](https://www.uab.edu/it/home/policies) non-compliance.
    - [HIPAA](https://www.uab.edu/it/home/policies/compliance/hipaa) or [FERPA](https://www.uab.edu/registrar/ferpa) non-compliance related to use of Cheaha.
- Investigation: issues identified as part of a required review of the account.

In rare circumstances, we may also place a hold on your account if you possess the sole copy of data not owned by you.

If your account is on hold, you will see a page like the following.

![!Account on hold page.](images/uab_on_hold.png)

If you SSH into the cluster while your account is on hold you will see the following text in your terminal.

![!Account on hold SSH reply.](images/uab_on_hold_ssh.png)

If your account is on hold and we have not already contacted you, or you believe the hold to be in error, please [Contact Support](../help/support.md).

### Authorization Error

Periodically, we review all researcher accounts to ensure they are authorized to use Cheaha based on affiliation status. If we find a researcher is no longer affiliated with UAB, we may disable the account. If you are not authorized to use Cheaha, you will see a page like the following.

![!Account authorization error page.](images/uab_auth_error.png)

If you believe this to be in error, please [Contact Support](../help/support.md).

## What Can I Do With My Account?

Research Computing offers services addressing a wide range of needs for researchers at UAB, including students, staff, and faculty, as well as for both Labs and research cores.

We're always happy to provide support for your Research Computing needs, you need only [Contact Support](../index.md#how-to-contact-us).

### For Students, Staff, and Faculty

- [Get Started with Open OnDemand](../cheaha/open_ondemand/index.md)
- [Additional Learning Resources](../education/training_resources.md)
- [Data Science Journal Club Course](../education/courses.md#data-science-journal-club-course)

### For Lab PIs and Core Directors

- [No-cost storage offerings](../data_management/index.md#what-type-of-storage-do-i-need)
    - [GPFS](../data_management/index.md#what-shared-storage-solutions-are-available): Hot storage, compute adjacent, directly accessible from Cheaha
    - [LTS](../data_management/lts/index.md): Cool storage, large capacity
    - [Transfer data with Globus](../data_management/transfer/globus.md)
- [Batch computing](../cheaha/slurm/introduction.md)
    - Interactive applications in [Open OnDemand](../cheaha/open_ondemand/index.md)
        - [HPC Desktop](../cheaha/open_ondemand/hpc_desktop.md)
        - [Jupyter Notebook](../cheaha/open_ondemand/ood_jupyter_notebook.md)
        - [JupyterLab](../cheaha/open_ondemand/ood_jupyterlab.md)
        - [RStudio](../cheaha/open_ondemand/ood_rstudio.md)
        - [Matlab](../cheaha/open_ondemand/ood_matlab.md)
    - [GPUs](../cheaha/slurm/gpu.md)
- [On-prem cloud computing](../uab_cloud/index.md)
    - [Tutorial](../uab_cloud/tutorial/index.md)
    - [Web servers](../uab_cloud/remote_access.md#make-instances-publically-accessible-from-the-internet)

  If you are unable to find what you need, please feel free to [Contact Support](../index.md#how-to-contact-us).

## Cheaha Account and Group Membership FAQ

Our Cheaha system is robust, but errors may occur due to general platform connectivity issues or missing components. Below are FAQs for self-service Cheaha account creation and a troubleshooting guide for common issues:

- **Which credentials should I use?** Please visit [How Do I Login to Research Computing Services](../account_management/index.md#how-do-i-login-to-research-computing-services).
- **What do I do if I'm waiting for it to finish for longer than a couple of minutes?**

    - Try closing and restarting your browser, then trying again.
    - Try clearing site data for <https://rc.uab.edu>, then trying again.
    - Try logging in on a Private Browsing window, then trying again.
    - Try waiting a few hours, then trying again.

- **What should I do to access shared storages and recognize my group membership after being added to a group on Cheaha?**

    - **Do you have any processes/connections on `cheaha.rc.uab.edu`**?

        - Please exit and log back in.
        - If you have active Tmux/Screen sessions, you will need to terminate those as well, log out, log back in and start Tmux.

    - **Do you have an active Open OnDemand session?**

        - In Open OnDemand (<https://rc.uab.edu>), navigate to the green navigation bar in the top right corner. Look for the `Help` or `Developer` dropdown menu and click on it. Then, click `Restart Web Server`. Once the restart is complete, please try again.

    - **Do you have one or more OOD HPC Desktops running?**

        - Terminate the desktops and start new ones.

## Leaving UAB

Please see our [Leaving UAB page](./leaving_uab.md).
