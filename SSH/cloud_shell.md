# Connect to instance using the OCI Cloud Shell

### Using the OCI Cloud Shell to connect to the Linux instance using its public IP address.


1. Log in to the OCI Console and click on the **OCI Cloud Shell** icon to open the Cloud Shell console.
    
    ![drawing](../SS/ssh_cloud_shell/1.png)

2. Click **Cloud Shell**.

    ![drawing](../SS/ssh_cloud_shell/2.png)

3. Make sure that the Cloud Shell window opens.

    ![drawing](../SS/ssh_cloud_shell/3.png)

4. Enter *N* to skip the tutorial for now.

    ![drawing](../SS/ssh_cloud_shell/4.png)

5. Run the *ls-l* command and see that we do not have the private key in the home folder, and then click the wheel to upload it.

    ![drawing](../SS/ssh_cloud_shell/5.png)

6. Click **Upload**.

    ![drawing](../SS/ssh_cloud_shell/6.png)

7. Click **Select from your computer**.

    ![drawing](../SS/ssh_cloud_shell/7.png)

8. Select the private key from the local computer and then click **Open**.

    ![drawing](../SS/ssh_cloud_shell/8.png)

9. Review the key selected in the previous step and then click **Upload**.

    ![drawing](../SS/ssh_cloud_shell/9.png)

10. Make sure the upload is completed and then click **Hide**.

    ![drawing](../SS/ssh_cloud_shell/10.png)

11. Run the *ls-l* command to check the private key.

    ![drawing](../SS/ssh_cloud_shell/11.png)

12. For connecting to the instance:

    &emsp;(1) Restrict permissions of the private key and make sure the access is restricted before it can be used. <br />
            &emsp;&emsp;&emsp;&emsp; *chmod 600 ~/ssh-key.key* <br />
    &emsp;(2) Connect to the instance using the SSH command and specify the public key <br />
            &emsp;&emsp;&emsp;&emsp; *ssh -i ~/ssh-key.key opc@<PUBLIC_IP_ADDRESS>* 

    ![drawing](../SS/ssh_cloud_shell/12.png)
