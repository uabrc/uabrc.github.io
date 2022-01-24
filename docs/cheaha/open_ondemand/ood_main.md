---
title: HomePage
---

Navigating to <https://rc.uab.edu> will take you to the OOD homepage:

<img src="images/ood_homepage.png" class="align-center" alt="Landing page for Open OnDemand" />

You will find system-wide messages from admins at the tope of the page
(red outline). These will always include links to the Research Computing
Office Hours on Zoom. This will also be the place to see information
about ongoing maintenance.

In the middle of the page (green outline), you will see a Message of the
Day containing the email address for support if you are having any
issues with Cheaha. There are also links to our Acceptable Use Policy as
well as links to our documentation.

Lastly, there is a table with a list of available SLURM partitions on
Cheaha with their max runtime and number of compute nodes per job as
well as their priority. Use this table to plan job requests based on
your needed computational resources.

# Toolbar

To access all of the features OOD has to offer, use the toolbar at the
top of the page that looks like:

<figure>
<img src="images/ood_toolbar.png" class="align-center" />
</figure>

In it, you will find options to:

1.  `Directly access your files on Cheaha <ood_files.rst>`
2.  `View currently running jobs <ood_jobs.rst>`
3.  Interface with Cheaha via a shell terminal
4.  `Request interactive sessions <ood_interactive.rst>`

To use a shell terminal in Cheaha through OOD, click
`Clusters >> >_Cheaha Shell Access`. You can use this exactly like a
standard `ssh` tunnel.

<div class="warning">

<div class="title">

Warning

</div>

Using the shell terminal in this way puts you on the login node. Do not
run any compute tasks on the login node. Request a compute node first!

</div>
