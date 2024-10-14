# AWS ETL Boilerplate

Text-to-float translator with repo *rest* as backend. This repo is *rest* frontend. Task: Redirect user to S3 after prompt input.
* Flask endpoint with Lambda to replace the need for manually updating FURL.  
* API Gateway beats FURL in throttling and quotas for preventing uncontrolled expenses inside usage plans. 

Provisioned concurrency is discrete distribution of auto scaling. 
* Rate for lambda quotas is 1 MB/s * 75 * 1.1 = 66-83 MB.
* Feature: media catalog updates.
* Testing: ```npx localtunnel --port 8000, flask run -p 8000```

This proxy folder use Jinja2 for serving static files. Make sure to store npx url inside JS file. CodeBuild size from installation per invocation is not solved with cache layers. Benchmark of loading time without ECS. 
* gh-pages 75 s, proxy 60 s. No need for CDN.

Users must wait and reload to see their metrics. Env vars is used inside NextJS or CodeBuild. Store furl inside GH repo secrets. Not your .env file. Learn more from MERN boilerplate. 

**Cost:** API Gateway charges for the number of requests processed and data transferred, while Lambda charges for the duration your code executes and memory consumed. L saves money over Fargate when it runs a quarter or less of the day.

* Proxy for Oauth inside ScrewFast: Forward is Mockoon used to cloned JSON files. Reverse is ngrok to original APIs.
* AWS overview: Use SQS for UX transparency. RDS for CRUD caching server of S3. CB to be triggered by S3 updates.
* SNS or gh webhook to collaborate with other devs.
* EventBridge to DLQ actions for unit testing. EB support MongoDB.
* Step Functions to orchestrate ETL. Terraform is CD of SFW (CI).

**Optionally:** UID from web driver cookies to write separate oak_{n}.txt files with provisioned concurrency hence why *imgo*.
