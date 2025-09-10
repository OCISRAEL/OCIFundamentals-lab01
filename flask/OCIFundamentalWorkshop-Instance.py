from flask import Flask, render_template, request
from pymongo import MongoClient
from datetime import datetime
import oci
import requests
import os
import json


#############################################################################################
# Need to get from user :
#   1. Connection string - API for MongoDB with port 27017 (CONNECTION_STRING)
#   2. Bucket name (bucketName)
#   3. Collection name (coll_name)
#############################################################################################

#############################################################################################
# Need to install on instance :
#   1. pymongo (pip3 install pymongo)
#   2. flask (pip3 install flask)
#   2. requests (pip3 install requests)
#############################################################################################


### | Read configuration file 
path = os.path.dirname(os.path.abspath(__file__))
content = ''
with open(os.path.join(path, "config.txt"), "r") as f:
    content = f.read()
    print(content)
    f.close()

json_content = json.loads(content)
CONNECTION_STRING = json_content["CONNECTION_STRING"]
bucketName = json_content["bucketName"]
coll_name = json_content["coll_name"]

### Read configuration file - End



### | Getting instance metadata 
headers = {
        'Authorization': 'Bearer Oracle',
    }

response = requests.get('http://169.254.169.254/opc/v2/instance/', headers=headers)
compId = response.json()['compartmentId']
namespace = ""
region = response.json()['regionInfo']['regionIdentifier']

signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()

### Getting instance metadata - End



### | ADB connection
client = MongoClient(CONNECTION_STRING)
db_name = 'admin'

### ADB connection - End



### | Get db & collection
db = client.get_database(name=db_name)
coll = db.get_collection(name=coll_name) # Use coll.insert_one to add documents to the collection

### Get db & collection - End



### | Read from db all documents from the collection
list = []

def read_from_db():
    list.clear()
    for doc in coll.find():
        ahref = "<a href='" + doc['link'] + "' target='_blank'>"+ doc['name'] + "</a>"
        list.append({'Name': ahref, 'Date': doc['date'], 'Link':  doc['link']})

### Read from db all documents from the collection - End



### | Object Storage 
object_storage_client = oci.object_storage.ObjectStorageClient(config={}, signer=signer)
namespace = object_storage_client.get_namespace().data

def upload_to_object_storage(file,file_name:str,bucket_name:str,object_storage_client,namespace): 
    object_storage_client.put_object(namespace,bucket_name,file_name,file) 
    print("Finished uploading {}".format(file_name)) 

### Object Storage - End


### | Generate object link
def get_object_link(os_region, os_namespace, bucket_name, file_name):
    return 'https://objectstorage.' + os_region + '.oraclecloud.com/n/' + os_namespace + '/b/' + bucket_name + '/o/' + file_name

### Generate object link - End



### | Write to db
def write_to_db(collection, file_name, object_link):
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    result = collection.insert_one(     # to insert data
    {
        'name': file_name,
        'date': date,
        'link': object_link
    }
    )

##### Write to db - End



### | Flask
app = Flask(__name__)

@app.route('/')
def index():
    read_from_db()
    return render_template('FundHTML.html', data=list, name='Ido')


@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
    f=request.files['myFile']
    upload_to_object_storage(file=f, file_name=f.filename, bucket_name=bucketName, object_storage_client=object_storage_client, namespace=namespace)
    object_link = get_object_link(os_region=region, os_namespace=namespace, bucket_name=bucketName, file_name=f.filename)
    write_to_db(collection=coll, file_name=f.filename, object_link=object_link)
    # return 'file ' + f.filename + ' uploaded successfully'
    print('file ' + f.filename + ' uploaded successfully')
    return render_template('UploadHTML.html', name=f.filename)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

### | Flask - End