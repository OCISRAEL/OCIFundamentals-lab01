# Creating IAM User, Group and Policy

### Creating a User
### Create a user account for a user in an OCI IAM identity domain

1. Open the navigation menu and click **Identity & Security**. Under **Identity**, click **Domains**

2. Click the **Default** identity domain, and then click **Users** and **Create user**

3. Enter the following:
    1. **Name:** User
    2. **Last Name:** Lab
    3. Clear the **Use the email address as the username** checkbox
    4. **Username:** userlab
    5. **Email:**: Enter a valid email address for notifications (your private email)

4. Click **Create**


### Creating a Group
### Create a group in an OCI IAM identity domain

1. Go back to the **Default** identity domain, click on **Groups**, and then on **Create group**

2. Enter the following:
    1. **Name:** LabGroup
    2. **Description:** Lab Group
    3. Leave the **User can request access** checkbox uncheck
    4. **Select users to assign this group:** Select the Lab User you created

3. Click **Create**


### Creating a Policy
### Create IAM policies to manage access to OCI resources

1. Open the navigation menu and click **Identity & Security**. Under **Identity**, click **Policies**

2. Click **Create Policy**

3. Enter the following:
    1. **Name:** LabPolicy
    2. **Description:** Lab Policy
    3. **Compartment:** Select the root compartment
    4. **Policy Builder:** Switch to manual editor and enter the following policy statement:<br>
    ```Allow group LabGroup to manage all-resources in compartment demo```

4. Click **Create**

