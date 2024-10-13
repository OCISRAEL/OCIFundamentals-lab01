# Connect to instance using the OCI Cloud Shell

### In this approach, we will connect to the Linux instance using the OCI Cloud Shell provided by OCI and connect to the instance using the Public IP address.


1. Log in to the OCI Console and click on the **OCI Cloud Shell** icon to open the Cloud Shell console.
    
    ![drawing](./SS/vcn/2.png)

2. Click **Cloud Shell**.

    ![drawing](./SS/vcn/2.png)

3. Make sure that the Cloud Shell window opens.

    ![drawing](./SS/vcn/2.png)

4. Enter *N* to skip the tutorial for now.

    ![drawing](./SS/vcn/2.png)

5. Run the *ls-l* command and see that we do not have the private key in the home folder.

    ![drawing](./SS/vcn/2.png)

6. To upload the private key, click the wheel.

    ![drawing](./SS/vcn/2.png)

7. Click **Upload**.

    ![drawing](./SS/vcn/2.png)

8. Click **Select from your computer**.

    ![drawing](./SS/vcn/2.png)

9. Select the private key from the local computer and then click **Open**.

    ![drawing](./SS/vcn/2.png)

10. Review the key selected in the previous step and then click **Upload**.

    ![drawing](./SS/vcn/2.png)

11. Make sure the upload is completed and then click **Hide**.

    ![drawing](./SS/vcn/2.png)

12. Run the *ls-l* command to check the private key.

    ![drawing](./SS/vcn/2.png)

13. For connecting to the instance:

    (1) Restrict permissions of the private key and make sure the access is restricted before it can be used.
            *chmod 600 ~/ssh-key.key*
    (2) Connect to the instance using the SSH command and specify the public key
            *ssh -i ~/ssh-key.key opc@<PUBLIC_IP_ADDRESS>*

    ![drawing](./SS/vcn/2.png)
