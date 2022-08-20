This document explains the steps that need to create a new AWS Glue Job.

#### Step 1: Create s3 bucket for the glue job. Two sub-folders "read" and "write" will be created
#### Step 2: Create Policy that has necessary permission for Glue and S3 bucket
#### Step 3: Create Crawler that takes input data set (csv file) and create a metadata table inside newly created database "db_google_scholar"
#### Step 4: Create a Glue Job. Script [glue_job_google_scholar.py](./glue_job_google_scholar.py) that runs in the job.

------------------------------------------------------------------------------------

#### Step 1: Create s3 bucket for the glue job. Two sub-folders "read" and "write" will be created


![](./s3_glue_images/s3_7.png)

![](./s3_glue_images/s3_6.png)

![](./s3_glue_images/s3_5.png)

![](./s3_glue_images/s3_4.png)

![](./s3_glue_images/s3_3.png)

![](./s3_glue_images/s3_2.png)

![](./s3_glue_images/s3_1.png)

#### Step 2: Create Policy that has necessary permission for Glue and S3 bucket

- Create a policy that have access to the S3 buckets. You may select to give permission to all buckets (see below) or specific buckets.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "glue:*"
            ],
            "Resource": "*"
        }
    ]
}
```

- Create a new IAM role (say: AmazonSageMakerServiceCatalogProductsUseRole) and attach the policy created in the above step.

#### Step 3: Create Crawler that takes input data set (csv file) and create a metadata table inside newly created database "db_google_scholar" 

Go to [Glue](https://us-east-2.console.aws.amazon.com/glue/home?region=us-east-2#)

![](./glue_crawler_images/glue_crawler_19.png)

![](./glue_crawler_images/glue_crawler_17.png)

![](./glue_crawler_images/glue_crawler_16.png)

![](./glue_crawler_images/glue_crawler_15.png)

![](./glue_crawler_images/glue_crawler_14.png)

![](./glue_crawler_images/glue_crawler_13.png)

![](./glue_crawler_images/glue_crawler_12.png)

![](./glue_crawler_images/glue_crawler_11.png)

![](./glue_crawler_images/glue_crawler_9.png)

![](./glue_crawler_images/glue_crawler_8.png)

![](./glue_crawler_images/glue_crawler_7.png)

![](./glue_crawler_images/glue_crawler_6.png)

![](./glue_crawler_images/glue_crawler_5.png)

![](./glue_crawler_images/glue_crawler_4.png)

![](./glue_crawler_images/glue_crawler_3.png)

![](./glue_crawler_images/glue_crawler_2.png)

![](./glue_crawler_images/glue_crawler_1.png)

#### Step 4: Create a Glue Job. Script [glue_job_google_scholar.py](./glue_job_google_scholar.py) that runs in the job. 

![](./glue_job_create/glue_job_create_29.png)

![](./glue_job_create/glue_job_create_27.png)

![](./glue_job_create/glue_job_create_26.png)

![](./glue_job_create/glue_job_create_25.png)

![](./glue_job_create/glue_job_create_24.png)

![](./glue_job_create/glue_job_create_23.png)

![](./glue_job_create/glue_job_create_22.png)

![](./glue_job_create/glue_job_create_21.png)

![](./glue_job_create/glue_job_create_20.png)

![](./glue_job_create/glue_job_create_19.png)

![](./glue_job_create/glue_job_create_17.png)

![](./glue_job_create/glue_job_create_16.png)

![](./glue_job_create/glue_job_create_15.png)

![](./glue_job_create/glue_job_create_14.png)

![](./glue_job_create/glue_job_create_13.png)

![](./glue_job_create/glue_job_create_12.png)

![](./glue_job_create/glue_job_create_11.png)

![](./glue_job_create/glue_job_create_9.png)

![](./glue_job_create/glue_job_create_8.png)

![](./glue_job_create/glue_job_create_7.png)

![](./glue_job_create/glue_job_create_6.png)

![](./glue_job_create/glue_job_create_5.png)

![](./glue_job_create/glue_job_create_4.png)

![](./glue_job_create/glue_job_create_3.png)

The downloaded csv file showing the glue job writen CSV content

![](./glue_job_create/glue_job_create_2.png)

Monitor
![](./glue_job_create/glue_job_create_1.png)
