## Creating a Glue Job for ETL

We will show with step-by-step on how to create a glue job for ETL. 

#### Prerequisite:
- Create a bucket in S3
- Create Policy that has necessary permission for Glue and S3 bucket

Refer the screenshots [here](./glue_create_job.md) for these steps.

#### Steps for Data Processing in Glue:

Python Script used in the glue python script editor located [here](./glue_job_google_scholar.py)
that covers the steps 2-5 listed-out as following.

  1. Creating a glue data catalog (screenshot at [here](./glue_create_job.md))
  2. Setup glue context
  3. Reading data
  4. Basic transformation
  5. Writing data

