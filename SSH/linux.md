# Connect to instance from a Linux machine

### In this approach, we will connect to a Linux instance using SSH and the public IP address that is provided by OCI to connect directly to the instance using the Linux (macOS) terminal.


1. Open a terminal.
    
    ![drawing](../SS/ssh_cloud_shell/.png)

2. Locate the private key file for your key pair. The default directory location for SSH keys is *`<your-home-directory>/.ssh`* . 
    <br><br>
    ``ds sd ``

3. Use the following command to set the file permissions so that only you can read the file:
    <br><br>
    *``chmod 400 <private_key_file>``*
    <br><br>
    ``<private_key_file>`` is the full path and name of the file that contains the private key associated with the instance you want to access.
    <br><br>
4. Use the following SSH command to access the instance:
    <br><br>
    *``ssh -i <private_key_file> <username>@<public-ip-address>``*
    <br><br>
    `<private_key_file>` is the full path and name of the file that contains the private key associated with the instance you want to access.
    <br>
    `<username>` is the default username for the instance. For Oracle Linux and Redhat Enterprise Linux compatible images, the default username is `opc`. For Ubuntu images, the default username is `ubuntu`.
    <br>
    `<public-ip-address>` is the instance's IP address that you retrieved from the Console.
    <br><br>
6. If you're connecting to this instance for the first time, you need to accept the fingerprint of the key. To accept the fingerprint, type **yes** and press **Enter**.
    <br><br>
7. You are connected to the default shell for the instance.
    <br><br>
8. When you have finished your session, type `exit` at the shell prompt to end the session.




