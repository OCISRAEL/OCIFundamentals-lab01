# Create Compute Intance
1. Open the navigation menu and click **Compute** &rarr; **Instances**

2. Select the **'demo'** compartment, then click **Create Instance**

    ![drawing](../SS/compute/1.png)

3. Enter a name for the instance

    ![drawing](../SS/compute/2.png)

4. Under **Image and Shape** section, keep the default **Oracle Linux** image and the **VM.Standard.E4.Flex** shape

    ![drawing](../SS/compute/3.png)

5. Under **Shape** Click on **Change Shape**. 

6. Choose  **AMD** -> **VM.Standard.E4.Flex** with **1 OCPU** and **8 GB of Memory**

![drawing](../SS/compute/4.png)

7. Click on **Advanced options** and scroll down until you reach **Oracle Cloud Agent**. Add the following to your stack:

![drawing](../SS/compute/5.png)

7. Click **Next** to reach **Networking**

8. For **Primary Network** Select the VCN we created earlier today, and under **Subnet**, select its Public Subnet.

     ![drawing](../SS/compute/6.png)

9. Scroll down and  Click **Download Private Key** to save the private key on your computer (Optionally, click **Download Public Key** to reptetive use in the future)

    ![drawing](../SS/compute/7.png)

9. Click **Next** to reach **Create**. Review and click

10. Once done. Find and copy the **Public IPv4 address** and save it for later use

    ![drawing](../SS/compute/8.png)

11. You can connect to the instance by running the following command on your terminal:<br>
        - [Using Cloud Shell](../SSH/cloud_shell.md) <br>
        - [Using Windows](../SSH/windows.md) <br>
        - [Using Linux](../SSH/linux.md) <br>

