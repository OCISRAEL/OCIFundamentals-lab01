# OCI Fundamentals Workshop


<ins>**Lab 1 – OCI Fundamentals** </ins>

* **Prerequisites:**

    1. OCI Account [(Click here to SignUp)](https://www.oracle.com/il-en/cloud/free/) / [(Click Here to Login)](https://www.oracle.com/cloud/sign-in.html)
    2. VCN [(Click here to create)](/VCN.md)
    3. Instance [(Click here to create)](/compute.md)


1. **STEP 1 : Create Dynamic Group and Policies**

   1. First, make sure you're using the right region - Israel Central (Jerusalem)

      ![drawing](./SS/step1/region.png)
      <!-- <img src="./SS/region.png" alt="drawing" width="2000" height="20"/> -->

   2. Open the OCI navigation menu on top left &nbsp; 

        <img src="./SS/step1/nav_bar_logo.png" alt="drawing" width="20"  display="inline-block" />

   3. Click **Identity & Security** &rarr; **Identity** &rarr; **Compartments**

      ![drawing](./SS/step0/nav_bar_compartments.png)

   4. Click the OCID string to view the entire value in a pop-up. Click Copy to copy the OCID to your clipboard. Save it - you'll need it.

      ![drawing](./SS/step0/compartment_ocid.png)

   5. Click **Dynamic Groups** under **Identity** on the left, and then click **Create Dynamic Group** 

        ![drawing](./SS/step0/create_dg_button.png)

   6. Enter the following:

        1. **Name:** A unique name for the dynamic group
        2. **Description (optional):** A friendly description
        3. Click **Rule Builder**

        ![drawing](./SS/step0/create_dg_screen.png)

    7. Enter the following:

        1. **Include instances that match:** Select **Any of the following**
        2. **Match instances with:** Select **Compartment OCID**
        3. **Value:** Enter your compartment OCID
        4. Click **Add Rule**, the rule should look similar to the following:
        
             *Any {instance.compartment.id = '<your_ocid>'}*

        5. Click **Create**

            ![drawing](./SS/step0/create_matching_rule.png)

        6. Next, give the dynamic group permissions by writing one or more policies. To do so, first click **Policies** under **Identity** on the left, and then click **Create Policy**

            ![drawing](./SS/step0/create_policy_button.png)

        7. Enter the following:

            1. **Name:** A unique name for the policy
            2. **Description (optional):** A friendly description
            3. **Compartment:** Select your compartment
            4. Switch the **Show manual editor** toggle on and add the following policies:

                    Allow dynamic-group <your_dg_name> to use buckets in tenancy

                    Allow dynamic-group <your_dg_name> to manage object-family in tenancy
                    
            * ***The new policies will go into effect typically within 10 seconds***

            ![drawing](./SS/step0/create_policy.png)


2. **STEP 2 : Create Bucket**

   1. Click **Storage** &rarr; **Object Storage & Archive Storage** &rarr; **Buckets**

        ![drawing](./SS/step1/nav_bar_buckets.png)

   2. Click **Create Bucket** (make sure you're in the right compartment)

        ![drawing](./SS/step1/create_bucket_button.png)

   3. Enter a name for your bucket and click **Create**
   (save the bucket's name, you'll need it later)

        ![drawing](./SS/step1/create_new_bucket.png)

   4. Before we move ahead, we must change the bucket's visibility to Public so we'll be able to access it without by link without authorization.

        To do so, click the three dots on the right, and then on **Edit Visibility**

        ![drawing](./SS/step1/edit_bucket_visibility_button.png)

   5. Select **Public** and click **Save Changes**

        ![drawing](./SS/step1/change_bucket_visibility.png)

   
3. **STEP 3 : Create ADB (Autonomous Database)**

   1. Open the navigation menu and click **Oracle Database** &rarr; **Autonomous JSON Database** 

        ![drawing](./SS/step2/nav_bar_adb.png)

   2. Click **Create Autonomous Database** (make sure you're in the right compartment)

        ![drawing](./SS/step2/create_adb_button.png)

   3. Enter the following:
        
        1. **Compartment:** Select your compartment
        2. **Display name:** Specify a user-friendly description that helps you easily identify the resource
        3. **Database name:** Specify the database name (it must consist of letters and numbers only)
        4. For the workload type, choose **JSON**
        5. For the deployment type, choose **Shared infrastructure**
        6. Keep the database configuration the same
        7. Set the password for the Admin database user in your new database **Don't use @ in password**
        8. Choose network access **Secure access from allowed IPs and VCNs only** and select IP notation type **CIDR Block** with the Values **0.0.0.0/0**
        9. Choose **License included** license type
        10. Skip on the Provide contacts section and click **Create Autonomous Database**

    4. Wait until your new Autonomous Database's status changes from Provisioning to Available.

    5. Click **Database actions** and wait for the page to finish initializing and to appear.

        ![drawing](./SS/step2/db_actions_button.png)

    6. Scroll down the Database Actions page until you find the Related Services section, then click **ORACLE DATABASE API FOR MONGODB**

        ![drawing](./SS/step2/mongodb_api_button.png)

    7. Copy the connection string for port 27017 and save it - you'll need it later

       Instead of *[user:password@]* enter your database username and password (without the '[]' with the @)

       Instead of *[user]* enter your database user

       It should looks like: *mongodb://**user**:**password**@G0D09E...F.adb.il-jerusalem-1.oraclecloudapps.com:27017/**user**?authMechanism...true*

        ![drawing](./SS/step2/connection_string.png)

    8. Now, let's add a new collection to your database by clicking &nbsp; **{} JSON** &nbsp; under the Development section

        ![drawing](./SS/step2/open_json_db.png)

    8. Click **Create Collection**

        ![drawing](./SS/step2/create_new_collection.png)

    8. Enter the following:
        
        1. **Collection Name:** Specify the collection name and save it - you'll need it later
        2. **MongoDB Compatible:** Select this checkbox
        3. Click **Create**

        ![drawing](./SS/step2/new_collection_window.png)


4. **STEP 4 : Open Port 5000 in VCN**

   1. Go to the VCN you've created earlier by opening the navigation menu and clicking **Networking** &rarr; **Virtual Cloud Networks** and then on your VCN's name.
      If you did't open one please follow the instractions here

   2. Under Resources, select **Subnets** and click **Public Subnet-<your_vcn_name>**

        ![drawing](./SS/step3/vcn_public_subnet.png)
    
   3. Under Resources, select **Security Lists** and click **Default Security List for <your_vcn_name>**

        ![drawing](./SS/step3/public_security_list.png)

    4. Click on **Add Ingress Rules**

    5. Enter the following:
        
        1. **Source Type:** Select CIDR
        2. **Source CIDR:** Enter 0.0.0.0/0
        3. **IP Protocol:** Select TCP
        4. **Destination Port Range:** Enter 5000
        5. Click **Save Changes**

        ![drawing](./SS/step3/open_port_5000.png)


5. **STEP 5 : Git Clone**

   0. Make sure your ssh key is secured

            chmod 700  <your_ssh_key_path>.key

   1. Connect to the compute instance you've created earlier today by running the following command on your shell:
        - [Using Cloud Shell](/ssh/cloud_shell.md)
        - [Using Windows](/ssh/windows.md)
        - [Using Linux](/ssh/linux.md)
    
            sudo ssh  -i <your_ssh_key_path>.key opc@<instance_ip>

    
   2. Switch to root user by running the following command:    

            sudo su

   3. After you connected to your machine, install git by running the following command:    

            yum install git

   4. Now, clone the git repository by running the following command:    

            git clone https://github.com/OCISRAEL/OCIFundamentals-lab01


6. **STEP 6 : Edit The Config File**

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
        
        1. **"CONNECTION_STRING":** Replace <DB_CONNECTION_STRING> with your db's connection string (inside the quotation marks)
        2. **"bucketName":** Replace <BUCKET_NAME> with your bucket's name (inside the quotation marks)
        3. **"coll_name":** Replace <COLLECTION_NAME> with your collection's name (inside the quotation marks)

    5. After you've finished editing, press the "**esc**" key, then **"shift" + ":"** , then write **:wq** and finally press the "**enter**" key to save your changes


7. **STEP 7 : Running The Application**

    1. Run the following command to install all of the packages listed in the "requirements.txt" file:

            pip3 install -r requirements.txt

    2. Run the following commands to open port 5000 in the Linux firewall:

        1.      sudo firewall-cmd --permanent --zone=public --add-port=5000/tcp
        2.      sudo firewall-cmd --reload

    3. Run the following command to run the application:

            python3 flask/OCIFundamentalWorkshop-Instance.py

    4. Navigate to the address **http://<your_instance_public_ip>:5000** in your browser and start uploading!


* **If you get the errors "address already in use" or "the server couldnt be started, because another server runs on that port", simply run the following command:**

        sudo kill -9 $(sudo lsof -t -i:5000)



