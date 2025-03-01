# Connecting to a Linux Instance from a MacOS or Linux System
### Use the OCI generated key pair or the key pair used to create the instance. Then use the following steps to connect to an OCI Linux instance.


1. Open a terminal.
    <br>
2. Locate the private key file for your key pair. The default directory location for SSH keys is *`<your-home-directory>/.ssh`* . 
    <br>

3. Use the following command to set the file permissions so that only you can read the file:
    <br>
    ```
    chmod 400 <private_key_file>
    ```
    <br>

    > ``<private_key_file>`` is the full path and name of the file that contains the private key associated with the instance you want to access.
    <br>
4. Use the following SSH command to access the instance:
    <br>
    ```
    ssh -i <private_key_file> <username>@<public-ip-address>
    ```
    <br>

    >`<private_key_file>` is the full path and name of the file that contains the private key associated with the instance you want to access.    <br>
    `<username>` is the default username for the instance. For Oracle Linux and Redhat Enterprise Linux compatible images, the default username is `opc`. For Ubuntu images, the default username is `ubuntu`. <br>
    `<public-ip-address>` is the instance's IP address that you retrieved from the Console.
    <br>
6. If you're connecting to this instance for the first time, you need to accept the fingerprint of the key. To accept the fingerprint, type **yes** and press **Enter**.
    <br>
7. You are connected to the default shell for the instance.
    <br>
8. When you have finished your session, type `exit` at the shell prompt to end the session.




