### EMR Setup

// ToDo: Rearrange sequence

- Visit [this](https://whatismyipaddress.com/) website to note down your `ip address`

[//]: # (![]&#40;./images_emr/emr_28.png&#41;  not needed &#40;new cluster page again&#41;)
[//]: # (![]&#40;./images_emr/emr_27.png&#41;)  not with Advanced option for cluster creation
[//]: # (![]&#40;./images_emr/emr_26.png&#41;) not with Advanced option for cluster creation
[//]: # (![]&#40;./images_emr/emr_25.png&#41;) not with Advanced option for cluster creation
Cluster creation in `Starting` status
![](./images_emr/emr_24.png)
Choose Cluster Nodes and Instances
![](./images_emr/emr_23.png)
Step 1: Cluster Creation -> Software Configuration
![](./images_emr/emr_22.png)
Step 1: Cluster Creation -> Software Configuration
![](./images_emr/emr_21.png)
In the Application interface, get the `User Interface URL` for `JupyterHub`
![](./images_emr/emr_20.png)
Use `whatismyipaddress.com` to get your ipv4 address.
![](./images_emr/emr_19.png)
Put the jupyterHub in the browser and click `Advanced` 
![](./images_emr/emr_18.png)
Hit 'Accept the Risk and Continue'
![](./images_emr/emr_17.png)
Provide username and password for JupyterHub.
![](./images_emr/emr_16.png)
Jupterhub application showing a list of notebooks. Click `New` and hit `PySpark`
![](./images_emr/emr_15.png)
Terminate cluster pop-up.
![](./images_emr/emr_14.png)
Terminate the cluster with the `Terminate` button
![](./images_emr/emr_13.png)
In the newly created Jupyter notebook, below example shows importing `pyspark` and `tensorflow`
![](./images_emr/emr_12.png)
New cluster created with `Running` status.
![](./images_emr/emr_11.png)

We need to add rule for inbound rule opening 9443 port (`Custom TCP`). See below two images having an 
already list of rules.
![](./images_emr/emr_9.png)
![](./images_emr/emr_10.png)
Contiuation from last image, put your ip address with /32 added.
![](./images_emr/emr_8.png)
Choose the security group used for EMR master.
![](./images_emr/emr_7.png)

[//]: # (![]&#40;./images_emr/emr_6.png&#41; # AWS security hub &#40;not needed&#41;)
Home page of `Security Groups`. It can be found by searching for "Security groups" in the search bar on the top of the console.
![](./images_emr/emr_5.png)
Step 3: General Cluster Settings
![](./images_emr/emr_4.png)
Step 4: Security
![](./images_emr/emr_3.png)
Home page for Amazon Cluster. Hit `Create Cluster` button
![](./images_emr/emr_2.png)
Step 2: Hardware configuration
![](./images_emr/emr_1.png)