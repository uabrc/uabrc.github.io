# Overview

XIAS accounts are limited identities intended only for accessing resources within the University of Alabama at Birmingham (UAB) environment. As a result, XIAS accounts cannot be used to access third-party licensed services such as Globus and Box.com.

External collaborators must access these third-party resources using their institution-approved authentication methods or personal accounts that comply with the service provider's requirements.

Additionally, many third-party services require users to accept Terms of Use or licensing agreements. Collaborators should ensure that any access method they use complies with their institution's policies and procedures regarding such agreement.

## Globus Access Options

External collaborators who need access to Globus should use one of the following authentication methods. UAB-affiliated users should continue using their BlazerID credentials.

### Option 1: Institutional Credentials

If the collaborator's institution participates in Globus and has an approved identity provider, they should sign in using their institutional credentials.

### Option 2: OAuth Identity Providers

Globus uses OpenID Connect (OIDC) and OAuth 2.0 to provide secure authentication through trusted identity providers. Instead of creating a separate Globus username and password, you sign in using an existing identity, such as your university account, Google account, GitHub account, or another supported provider. This approach allows users to securely access Globus services while their credentials remain managed by their chosen identity provider. Collaborators may authenticate using supported Open Authentication (OAuth) providers, including:

- Google
- GitHub
- ORCID

![Screenshot of Chosing Desired Open Authentication Providers](../images/gg-external-user/open_authentication.png)

#### Google

If your institution or organization is not listed as a Globus identity provider, or if you prefer using a personal account, you can sign in to Globus with your Google account. Globus supports Google authentication, allowing external users to securely access shared collections and transfer data.

![Screenshot of Chosing Google Authentication for Login](../images/gg-external-user/google_authentication.png)

On the Globus login page:

- Under Use your organizational login, select Google from the drop-down menu.
Click Continue.
- You will be redirected to the Google sign-in page to authenticate with your Google account.
- After successful authentication, you will be returned to Globus to continue accessing shared resources.

#### Globus ID

![Screenshot of Chosing Globus ID for Login](../images/gg-external-user/Globus_id.png)
