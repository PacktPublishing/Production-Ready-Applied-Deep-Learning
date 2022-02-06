This document explains the steps that need to create a new AWS Glue Job.

#### Step 1: Create s3 bucket for the glue job. Two sub-folders "read" and "write" will be created
#### Step 2: Create Policy that has necessary permission for Glue and S3 bucket
#### Step 3: Create Crawler that takes input data set (csv file) and create a metadata table inside newly created database "db_google_scholar"
#### Step 4: Create a Glue Job. Script [glue_job_google_scholar.py](./glue_job_google_scholar.py) that runs in the job.

------------------------------------------------------------------------------------

#### Step 1: Create s3 bucket for the glue job. Two sub-folders "read" and "write" will be created

7.
![](./s3_glue_images/s3_7.png)
6.
![](./s3_glue_images/s3_6.png)
5.
![](./s3_glue_images/s3_5.png)
4.
![](./s3_glue_images/s3_4.png)
3.
![](./s3_glue_images/s3_3.png)
2.
![](./s3_glue_images/s3_2.png)
1.
![](./s3_glue_images/s3_1.png)

#### Step 2: Create Policy that has necessary permission for Glue and S3 bucket

- To be filled.

#### Step 3: Create Crawler that takes input data set (csv file) and create a metadata table inside newly created database "db_google_scholar" 

Go to [Glue](https://us-east-2.console.aws.amazon.com/glue/home?region=us-east-2#)
19.
![](./glue_crawler_images/glue_crawler_19.png)
17.
![](./glue_crawler_images/glue_crawler_17.png)
16.
![](./glue_crawler_images/glue_crawler_16.png)
15.
![](./glue_crawler_images/glue_crawler_15.png)
14.
![](./glue_crawler_images/glue_crawler_14.png)
13.
![](./glue_crawler_images/glue_crawler_13.png)
12.
![](./glue_crawler_images/glue_crawler_12.png)
11.
![](./glue_crawler_images/glue_crawler_11.png)
9.
![](./glue_crawler_images/glue_crawler_9.png)
8.
![](./glue_crawler_images/glue_crawler_8.png)
7.
![](./glue_crawler_images/glue_crawler_7.png)
6.
![](./glue_crawler_images/glue_crawler_6.png)
5.
![](./glue_crawler_images/glue_crawler_5.png)
4.
![](./glue_crawler_images/glue_crawler_4.png)
3.
![](./glue_crawler_images/glue_crawler_3.png)
2.
![](./glue_crawler_images/glue_crawler_2.png)
1.
![](./glue_crawler_images/glue_crawler_1.png)

#### Step 4: Create a Glue Job. Script [glue_job_google_scholar.py](./glue_job_google_scholar.py) that runs in the job. 
29.
![](./glue_job_create/glue_job_create_29.png)

27
![](./glue_job_create/glue_job_create_27.png)
26. 
![](./glue_job_create/glue_job_create_26.png)
25. 
![](./glue_job_create/glue_job_create_25.png)
24. 
![](./glue_job_create/glue_job_create_24.png)
23. 
![](./glue_job_create/glue_job_create_23.png)
22. 
![](./glue_job_create/glue_job_create_22.png)
21. 
![](./glue_job_create/glue_job_create_21.png)
20. 
![](./glue_job_create/glue_job_create_20.png)
19. 
![](./glue_job_create/glue_job_create_19.png)
17. 
![](./glue_job_create/glue_job_create_17.png)
16.
![](./glue_job_create/glue_job_create_16.png)
15.
![](./glue_job_create/glue_job_create_15.png)
14.
![](./glue_job_create/glue_job_create_14.png)
13.
![](./glue_job_create/glue_job_create_13.png)
12. 
![](./glue_job_create/glue_job_create_12.png)
11. 
![](./glue_job_create/glue_job_create_11.png)
9.
![](./glue_job_create/glue_job_create_9.png)
8.
![](./glue_job_create/glue_job_create_8.png)
7.
![](./glue_job_create/glue_job_create_7.png)
6.
![](./glue_job_create/glue_job_create_6.png)
5. 
![](./glue_job_create/glue_job_create_5.png)
4.
![](./glue_job_create/glue_job_create_4.png)

3.
![](./glue_job_create/glue_job_create_3.png)

The downloaded csv file showing the glue job writen CSV content

![](./glue_job_create/glue_job_create_2.png)

Monitor
![](./glue_job_create/glue_job_create_1.png)