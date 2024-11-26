# Connecting to a Linux Instance from a Windows System
### Using the OCI generated key pair or your own generated key pair used to create the instance, connect to the Linux instance.

### Set the Permissions for the Private Key File
Set the file permissions for the private key file so that only the current user has read-only access. Do the following:

1. Locate the SSH key files you created by or created for your instance

2. In Windows Explorer, navigate to the private key file, right-click the file

3. Click **Properties**

4. On the **Security** tab, click **Advanced**

5. On the **Permissions** tab, for **Permission entries**, under **Principal**, ensure that your user account is listed

6. Click **Disable Inheritance**, and then select **Convert inherited permissions into explicit permissions on this object**

7. For **Permission entries**, select each permission entry that isn't your user account and click **Remove**

8. Ensure that the access permission for your user account is **Full control**

9. Save your changes


### Connect to the Instance with PowerShell
Next, connect to the instance with PowerShell.

1. Open Windows PowerShell and run the following command:
    ```
    ssh -i <private_key_file> <username>@<public-ip-address>
    ```
    >`<private_key_file>` is the full path and name of the .key file that contains the private key associated with the instance you want to access.<br>
    `<username>` is the default username for the instance. For Oracle Linux and Redhat Enterprise Linux compatible images, the default username is `opc`. For Ubuntu images, the default username is `ubuntu` <br>
    `<public-ip-address>` is the instance's IP address that you retrieved from the Console.

2. If you're connecting to this instance for the first time, you need to accept the fingerprint of the key. To accept the fingerprint, type **yes** and press **Enter**.

3. You are connected to the default shell for the instance.

4. When you have finished your session, type `exit` at the shell prompt to end the session.

