# Create Compute Intance
1. Open the navigation menu and click **Compute** &rarr; **Instances**

    ![drawing](./SS/compute/1.png)

2. Click **Create Instance**

    ![drawing](./SS/compute/2.png)

3. Enter a name for the instance and select the compartment to create the instance in

    ![drawing](./SS/compute/3.png)

4. In the **Image and Shape** section, keep the default **Oracle Linux** image and the **VM.Standard.E4.Flex** shape

    ![drawing](./SS/compute/4.png)

5. Under **Virtual Cloud Network**, select the VCN we created earlier today, and under **Subnet**, select its Public Subnet.

     ![drawing](./SS/compute/5.png)

6. Click **Save Private Key**, and then save the private key on your computer (Optionally, click **Save Public Key** and then save the public key as well)

    ![drawing](./SS/compute/6.png)

7. Click **Show advanced options**

    ![drawing](./SS/compute/7.png)

8. On the **Oracle Cloud Agent** tab, choose **Vulnerability Scanning**, **Block Volume Management** and **Bastion** plugins

    ![drawing](./SS/compute/8.png)

9. Click **Create**

    ![drawing](./SS/compute/9.png)

10. You can connect to the instance by running the following command on your terminal:
        - [Using Cloud Shell](./SSH/cloud_shell.md)
        - [Using Windows](./SSH/windows.md)
        - [Using Linux](./SSH/linux.md)

10. Copy the **Public IP address** and save it for later use

    ![drawing](./SS/compute/10.png)

