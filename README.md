# AWS ETL Boilerplate

Text-to-float translator with repo *rest* as backend. Oak is *rest* frontend. Task: Redirect user to S3 after prompt input.
* Flask endpoint with Lambda to replace the need for manually updating FURL.  
* API Gateway beats FURL in throttling and quotas for preventing uncontrolled expenses inside usage plans. 

Provisioned concurrency is discrete distribution of auto scaling. 
* Rate for lambda quotas is 1 MB/s * 75 * 1.1 = 66-83 MB.
* Feature: media catalog updates.
* Testing: ```npx localtunnel --port 8000, flask run -p 8000```

This proxy folder use Jinja2 for serving static files. Make sure to store npx url inside JS file. CodeBuild size from installation per invocation is not solved with cache layers. Benchmark of loading time without ECS. 
* gh-pages 75 s, proxy 60 s. No need for CDN.

Users must wait and reload to see their metrics. Env vars is used inside NextJS or CodeBuild. Store furl inside GH repo secrets. Not your .env file. Learn more from MERN boilerplate. 

**Cost:** API Gateway charges for the number of requests processed and data transferred, while Lambda charges for the duration your code executes and memory consumed. L saves money over Fargate when it runs a quarter or less of the day. **Time:** Proxy inside Astro include Mockoon (forward), to clone JSONs, and Ngrok (reverse) to test APIs.

* SNS or gh webhook to collaborate with other devs.
* SQS for UX transparency of loading time.
* EventBridge to DLQ actions for unit testing. EB support MongoDB.
* RDS for CRUD caching server of S3 with SQLite.
* CodeBuild to be triggered by S3 updates.
* Step Functions to orchestrate ETL including ecommerce.
* Terraform is CD of SFW (CI). CircleCI maybe.

**Optionally:** UID from web driver cookies to write separate files with provisioned concurrency hence why *imgo*.
