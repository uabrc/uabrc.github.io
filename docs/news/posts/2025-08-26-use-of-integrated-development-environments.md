---
date: 2025-08-26T09:00:00-05:00
categories:
    - Known Issues
---

# Use of Integrated Development Environments (IDEs)

Please do not use IDEs like VSCode "Remote - SSH" or Cursor Server to connect to Cheaha. These methods run all of their processes on the login node, which are automatically terminated.

<!-- more -->

Instead, use "Remote - Tunnel" as described in the [VSCode Tunnel](./cheaha/open_ondemand/hpc_desktop.md#visual-studio-code-remote-tunnel) section. See [additional information](../getting_started.md#why-you-should-avoid-running-jobs-on-login-nodes) about running jobs on the Login node.
