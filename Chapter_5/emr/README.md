### Setting up an EMR Cluster for ETL

In this file, we will show how to create a new cluster step-by-step. 

#### Prerequisite:

1. Home page of `Security Groups`. It can be found by searching for "Security groups" in the search bar on the top of the console.
![](./images_emr/emr_5.png)
2. Visit [this](https://whatismyipaddress.com/) website to note down your `ip address`
Use `whatismyipaddress.com` to get your ipv4 address.
![](./images_emr/emr_19.png)

#### Creating a new EMR cluster
Open the Amazon EMR service to start creating a new cluster. 

Search and open the EMR service
![](./images_emr/search_for_emr.png)
The landing page of EMR service shows this quick option page, just hit the button `Go to advanced options`
which will take you to the next page
![](./images_emr/emr_quick_options.png)

Step 1: Cluster Creation -> Software Configuration
![](./images_emr/emr_22.png)
Step 1: Cluster Creation -> Software Configuration
![](./images_emr/emr_21.png)


Step 2: Hardware configuration
![](./images_emr/emr_1.png)
Step 2: Choose Cluster Nodes and Instances
![](./images_emr/emr_23.png)
Step 3: General Cluster Settings
![](./images_emr/emr_4.png)
Step 4: Security. Fill in the details (Ec2 key pair, security groups etc.) and hit `Create cluster`
![](./images_emr/emr_3.png)

Cluster creation will start with `Starting` status
![](./images_emr/emr_24.png)

After some time, the cluster goes to `Running` status. Now, you can open JupyterHub as explained in the following steps.
![](./images_emr/emr_11.png)

#### JupyterHub
In the Application interface, get the `User Interface URL` for `JupyterHub`
![](./images_emr/emr_20.png)

Put the jupyterHub in the browser and click `Advanced` 
![](./images_emr/emr_18.png)
Hit 'Accept the Risk and Continue'
![](./images_emr/emr_17.png)
Provide username and password for JupyterHub.
![](./images_emr/emr_16.png)
Jupterhub application showing a list of notebooks. Click `New` and hit `PySpark`
![](./images_emr/emr_15.png)

In the newly created Jupyter notebook, below example shows importing `pyspark` and `tensorflow`
![](./images_emr/emr_12.png)


#### Terminating cluster
Terminate cluster pop-up.
![](./images_emr/emr_14.png)
Terminate the cluster with the `Terminate` button
![](./images_emr/emr_13.png)

#### Adding inbound rules under Security Group
We need to add rule for inbound rule opening 9443 port (`Custom TCP`). 

Find and open the `Security Groups` service.
![](./images_emr/find_security_groups.png)

The landing page shows the list of security groups and choose the security group which is used while
creating your EMR cluster in order to edit its inbound rules.
![](./images_emr/find_security_groups.png)

For the remaining, follow the steps under **"Create Security Group that has access to ec2 from your laptop"**
in ![ec2.md](../ec2/README.md)