# Connect to instance from a Linux machine

### In this approach, we will connect to a Linux instance using SSH and the public IP address that is provided by OCI to connect directly to the instance using the Linux (macOS) terminal.


1. Open Terminal.
    
    ![drawing](../SS/ssh_cloud_shell/.png)

2. Use the command line interface (CLI) to navigate to the folder where the public and private keys are stored. 
    <br><br>
    ``ds sd ``
    
    ![drawing](../SS/ssh_cloud_shell/.png)

3. Restrict permissions of the private key and make sure the access is restricted, before it can be used.
    <br><br>
    ``chmod 600 ssh-key-2024-01-31.key``
    
    ![drawing](../SS/ssh_cloud_shell/.png)

4. 
