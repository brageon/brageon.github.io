This should be a text-to-float translator with repo rest as backend. This is my testimonial for ETL. Goal: Redirect user to S3 after prompt input. Why: (1) Flask endpoint with Lambda is replacing the need for manually updating FURL (CI). (2) Main advantage of API Gateway over FURL is throttling and quotas for preventing uncontrolled expenses inside usage plans.

```
Codespace is (1) track record without PRs: git stash for temporary git commit, git rev-list --count --all,
git rebase -i HEAD~122, sed -i 's/pick/drop/g' .git/rebase-merge/*-todo, git add ., git commit -m "Setup", git push -u origin 
(2) branch: git checkout -b "main", git push origin main, git log, git reset --hard "commit-SHA" to discard all commits after a certain date. 
(3) wrap it up: git pull origin main, git config pull.rebase true, git push -u origin, git push origin gh-pages --force.
```

Provisioned concurrency is discrete distribution of auto scaling. Rate for lambda quotas is 1 MB/s * 75 * 1.1 = 66-83 MB. Feature: media catalog updates. Testing: npx localtunnel --port 8000, flask run -p 8000. No need for CDN. This proxy folder use Jinja2 for serving static files. Make sure to store npx url inside JS file. Benchmark of loading time without ECS: gh-pages 75 s, proxy 60 s. Users must wait and reload to see their metrics. Env vars is used inside Nextjs. Store url inside GH repo secrets. Not your .env file. Learn more from MERN boilerplate. Cost: API Gateway charges for the number of requests processed and data transferred, while Lambda charges for the duration your code executes and memory consumed. Lambda saves money over Fargate when it runs a quarter or less of the day.

```
To delete cached files: git reset --soft HEAD~ && git commit --amend, git checkout --orphan newBranch, git add -A,
git commit -m "Ok", git branch -D main, git branch -m main, git push -f origin main, git gc --aggressive --prune=all 
```

Proxy for Oauth inside ScrewFast template: Forward is Mockoon used to cloned JSON files. Reverse is ngrok for original APIs. AWS overview: Use SQS for UX transparency. RDS for CRUD caching server of S3. CB/CP to be triggered by S3 updates. SNS or gh webhook to collaborate with other devs. EventBridge to DLQ actions for unit testing. Step Functions to orchestrate ETL. Terraform is CD of SFW (CI). Optionally: 1) UID from browser (e.g. cookies) to write separate S3 files like oak_{n}.txt with provisioned concurrency **or** 2) Batch job of serverless worker pool with asynch modules (e.g. promise).  
