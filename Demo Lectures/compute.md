# Create Compute Intance
1. Open the navigation menu and click **Compute** &rarr; **Instances**

2. In the Compartment dropdown, choose **demo**, then click **Create Instance**

    ![drawing](../SS/compute/1.png)

3. Enter a name for the instance

    ![drawing](../SS/compute/2.png)

4. Under **Image and Shape** section, keep the default **Oracle Linux** image

    ![drawing](../SS/compute/3.png)

5. In the **Shape** section, click **Change Shape**

6. Choose  **AMD** -> **VM.Standard.E4.Flex** with **1 OCPU** and **8 GB of Memory**

![drawing](../SS/compute/4.png)

7. Click on **Advanced options** and scroll down until you reach **Oracle Cloud Agent**. Add the following to your stack:

![drawing](../SS/compute/5.png)

8. Click **Next** to reach **Networking**

9. For **Primary Network**, select the VCN we created earlier today. Under **Subnet**, choose its Public Subnet.

     ![drawing](../SS/compute/6.png)

10. Scroll down and Click **Download Private Key** (required) to save it on your computer. Optionally, **Download Public Key** if you plan to reuse it later.

    ![drawing](../SS/compute/7.png)

11. Click **Next** to reach **Create**. Review and click

12. Once done. Find and copy the **Public IPv4 address** and save it for later use

    ![drawing](../SS/compute/8.png)

13. To connect to the instance, use one of the following guides based on your environment:<br>
        - [Using Cloud Shell](../SSH/cloud_shell.md) <br>
        - [Using Windows](../SSH/windows.md) <br>
        - [Using Linux](../SSH/linux.md) <br>

