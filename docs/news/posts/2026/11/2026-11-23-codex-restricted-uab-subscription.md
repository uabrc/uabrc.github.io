---
date: 2026-11-23T18:00:00-05:00
categories:
    - Maintenance
    - Security Issues
---

# Codex CLI on Cheaha Restricted to UAB OpenAI Workspace

Use of Codex CLI on Cheaha is now restricted to members of UAB's OpenAI workspace. Personal ChatGPT and Codex workspaces may no longer be used with Codex CLI on Cheaha.

<!-- more -->

## Why access is restricted

Cheaha supports research involving protected health information (PHI) and other sensitive or restricted data. Codex can read files available to a local session and send their contents to OpenAI's servers. Depending on the account and its settings or agreements, data sent to OpenAI may be used to train models. UAB's agreement with OpenAI provides that data made available through its subscription are not used to train OpenAI models. Restricting Codex to the UAB workspace helps align its use on Cheaha with UAB's data security requirements.

Membership in the UAB workspace does not by itself authorize sending PHI or other restricted data to Codex. Use an AI tool only for data and purposes for which the tool and environment are approved, and obtain any required review before use.

We also considered the impact of generative AI tools on the shared GPFS filesystem. Cheaha has experienced intermittent filesystem sluggishness associated with excessive I/O requests from user jobs. We believe filesystem scanning by a variety of generative AI tools is contributing to this load and are taking steps to limit its impact.

## Requesting access

UAB users can request access to the UAB OpenAI subscription at cost through the [subscription request form](https://uabprod.service-now.com/service_portal?id=sc_cat_item&sys_id=f3fb19c5877a47105cbaca6e0ebb354e). Select the desired access tier. Once added to the workspace, sign in using your BlazerID to use Codex on Cheaha.

## API keys

API key authentication for Codex CLI is not currently allowed on Cheaha. API keys authenticate through OpenAI API projects, and we have not established a way to restrict their use on Cheaha to keys associated with an approved UAB account. Until we can verify and enforce that restriction, please sign in through the UAB OpenAI workspace instead. We will revisit this restriction as available controls change.

## Approval for AI tools

All AI tools must be approved by UAB before they are used on Cheaha. Consult UAB's [list of generally approved AI tools](https://www.uab.edu/ai/tools) and its [practical guidance for using AI](https://www.uab.edu/ai/responsible-ai/practical-guidance). General approval does not cover every data type or use case; follow UAB's guidance and seek review where required.

Other standalone generative AI tools such as Anthropic Claude and Gemini, at present, remain prohibited on Cheaha pending future agreements between UAB and their parent corporations.
