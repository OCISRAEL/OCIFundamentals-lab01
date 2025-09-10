# OCI Fundamentals Workshop


<ins>**Lab 1 – DEMO LECTURES** </ins>

* **FOLLOW Those Steps First:**

    1. OCI Account [(Click here to SignUp)](https://www.oracle.com/il-en/cloud/free/) / [(Click Here to Login)](https://www.oracle.com/cloud/sign-in.html)
    2. Compartment [(Click here to create)](Demo%20Lectures/compartment.md)
    3. IAM User, Group and Policy [(Click here to create)](Demo%20Lectures/iam_user_group_policy.md)
    4. VCN [(Click here to create)](Demo%20Lectures/VCN.md)
    5. Instance [(Click here to create)](Demo%20Lectures/compute.md)
    6. Block Volume [(Click here to create)](Demo%20Lectures/block_volume.md)


<ins>**Lab 2 – CREATE YOUR APPLICATION** </ins>

**STEP 1 : Create Dynamic Group and Policies**

1. First, make sure you're using the right region - Israel Central (Jerusalem)

   ![drawing](./SS/lab2/1.png)

2. Open the navigation menu and click **Identity & Security** → **Identity** → **Compartments**

3. Select **demo** compartment

4. Copy the full OCID string of **demo** compartment. ⚠️ Save it - you'll need it later ⚠️

    ![drawing](./SS/lab2/2.png)

5. Open the navigation menu and click **Identity & Security**. Under **Identity**, click **Domains**

6. Select **root** compartment, then select the **Default** domain

   ![drawing](./SS/lab2/3.png)

7. Move to **Dynamic groups** tab, then click **Create dynamic group**

   ![drawing](./SS/lab2/4.png)

8. Enter the following:

   1. **Name:** DG-demo  
   2. **Description (optional):** Dynamic Group for demo compartment  
   3. Under **Matching rules** click **Rule Builder** and follow:  

      1. **Include instances that match:** Any of the following  
      2. **Match instances with:** Compartment OCID  
      3. **Value:** Enter your compartment OCID  
      4. Click **Add Rule**  

      ![drawing](./SS/lab2/5.png)

   4. The rule should look similar to the following:

      ```
      Any {instance.compartment.id = '<your_compartment_ocid>'}
      ```

    5. Click **Create**

9. Next, we need to give the dynamic group IAM permissions. 
        
10. Select **Policies** on the left menu, then click **Create Policy**

    ![drawing](./SS/lab2/6.png)

11. Enter the following:

    1. **Name:** dg-policy-demo
    2. **Description (optional):** Dynamic Group IAM policy
    3. **Compartment:** root
    4. Switch the **Show manual editor** and add the following policies:

            Allow dynamic-group <your_dg_name> to manage object-family in compartment <your_compartment_name>
    
    5. Click **Create**

    ```⚠️Note: The new policies will go into effect typically within 10 seconds ⚠️```

    ![drawing](./SS/lab2/7.png)

**STEP 2 : Create Bucket**

1. Click **Storage** &rarr; **Object Storage & Archive Storage** &rarr; **Buckets**

2. Select **demo** compartment, then click **Create Bucket**

    ![drawing](./SS/lab2/8.png)

3. Enter a name for your bucket,then click **Create bucket** <br>

```⚠️Note: Save the bucket's name, you'll need it later⚠️```
    ![drawing](./SS/lab2/9.png)
   
 **STEP 3 : Create ADB (Autonomous Database)**

1. Open the navigation menu and click **Oracle Database** &rarr; **Autonomous Database** 

2. Click **Create Autonomous Database** (make sure you're in the right compartment)

    ![drawing](./SS/lab2/10.png)

3. Enter the following:
    
    1. **Display name:** adb-demo
    2. **Database name:** adbdbdemo
    3. **Compartment:** demo
    4. For the workload type, choose **JSON**
    5. Leave **Database Configuration** with default values
    6. Set the password for the ADMIN database user in your new database - ⚠️**Don't use @ in password**⚠️
    7. **Access type:** Secure access from allowed IPs and VCNs only
    8. Set **IP notation type:** CIDR block & **Value:** 0.0.0.0/0 - ⚠️**For testing purpose only**⚠️
    9. Skip on the **Contacts** section and click **Create**

4. Wait until your new Autonomous Database's status changes from **Provisioning** to **Available**

5.  Select the **Tool configuration** tab on the Autonomous Database details page

    ![drawing](./SS/lab2/11.png)

6. Scroll down the Tool configuration page until you find the **MongoDB API**

8. Copy the connection string under **Public access URL** and edit it as follow: 

    Instead of **[user:password@]** enter your database username and password **(Without the '[]'. With the @)**

    Instead of **[user]** enter your database admin user

    It should looks like: *mongodb://**ADMIN**:**password**@G0D09E...F.adb.il-jerusalem-1.oraclecloudapps.com:27017/**ADMIN**?authMechanism...true*

    ```⚠️Note: Your string name may differ depending on your setup⚠️```

    ![drawing](./SS/lab2/12.png)

9. ⚠️ Save the full string - you'll need it later ⚠️

10. Scroll up & Click **Database actions** and then **View all database actions**.

    ![drawing](./SS/lab2/13.png)

11. Now, let's add a new collection to your database by clicking &nbsp; **{ } JSON** &nbsp; under the Development section and then **Open**.

    ![drawing](./SS/lab2/14.png)

8. Click **Create Collection**

    ![drawing](./SS/lab2/15.png)

8. Enter the following:
    
    1. **Collection Name:** collection-demo - ⚠️Save it. You'll need it later⚠️
    2. Click **Create**

    ![drawing](./SS/lab2/16.png)


**STEP 4 : Open Port 5000 in VCN**

1. Open the navigation menu and click **Networking** &rarr; **Virtual Cloud Networks**

2. Select the VCN we created earlier **VCN-demo**

3. In the **Subnets** tab, click **Public Subnet-<your_vcn_name>**

    ![drawing](./SS/lab2/17.png)

4. In the **Security** tab, click Default **Security List for <your_vcn_name>**

    ![drawing](./SS/lab2/18.png)

5. Select **Security rules** tab

6. Click **Add Ingress Rules** to save

7. Enter the following:
    
    1. **Source Type:** CIDR
    2. **Source CIDR:** 0.0.0.0/0
    3. **IP Protocol:** TCP
    4. **Destination Port Range:** 5000
    5. Click **Add Ingress Rules**

    ![drawing](./SS/lab2/19.png)

8. The newly created rule will be added to the list

    ![drawing](./SS/lab2/20.png)

**STEP 5 : Git Clone**

Use one of below methods to connect to the compute instance you've created earlier today:
    - [Using Cloud Shell](./SSH/cloud_shell.md)
    - [Using Windows](./SSH/windows.md)
    - [Using Linux](./SSH/linux.md)

1. [LINUX/MACOS/Windows] Open your terminal and run:

        ssh  -i <your_ssh_key_full_path>.key opc@<instance_ip>

2. Switch to root user by running the following command:    

        sudo su

3. After you connected to your machine, install git by running the following command:    

        yum install git

4. Now, clone the git repository by running the following command:    

        git clone https://github.com/OCISRAEL/OCIFundamentals-lab01


**STEP 6 : Edit The Config File**

1. Change directory to the cloned folder "OCIFundamentals-lab-01" by running the following command:    

        cd OCIFundamentals-lab-01

2. Run the following command to edit the config file:

        vi flask/config.txt

3. The file will look like that:

        {
        "CONNECTION_STRING": "<DB_CONNECTION_STRING>",
        "bucketName": "<BUCKET_NAME>",
        "coll_name": "<COLLECTION_NAME>"
        }

4. Press on "**i**" key to edit the file and change the following:
    
    1. **"CONNECTION_STRING":** Replace <DB_CONNECTION_STRING> with your **Mongo DB's** connection string (inside the quotation marks)
    2. **"bucketName":** Replace <BUCKET_NAME> with your bucket's name (inside the quotation marks)
    3. **"coll_name":** Replace <COLLECTION_NAME> with your collection's name (inside the quotation marks)

5. After you've finished editing, press the "**esc**" key, then **"shift" + ":"** , then write **:wq** and finally press the "**enter**" key to save your changes


**STEP 7 : Running The Application**

1. Install pip

        sudo yum install -y python3-pip

2. Install all of the packages listed in the "requirements.txt" file:

        pip3 install -r requirements.txt

3. Run the following commands to open port 5000 in the Linux firewall:

    1.      sudo firewall-cmd --permanent --zone=public --add-port=5000/tcp
    2.      sudo firewall-cmd --reload

you should get **sucess** on both times

3. Run the following command to run the application:

        python3 flask/OCIFundamentalWorkshop-Instance.py

4. Navigate to the address **http://<your_instance_public_ip>:5000** in your browser and start uploading!


* **If you get the errors "address already in use" or "the server couldnt be started, because another server runs on that port", simply run the following command:**

        sudo kill -9 $(sudo lsof -t -i:5000)


**STEP 8 : Review The Application**

1. Once you have successfully completed all these steps, your web application should look like this:

   ![drawing](./SS/app_ss.png)

2. Upload a test file to the app and confirm it was successful.

3. Check your **bucket**. Do you see the uploaded file?

4. Check your **Autonomous Database** JSON collection. Do you see a new entry?