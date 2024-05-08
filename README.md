This should be a text-to-float translator with repo rest as backend. This is my testimonial for ETL. Goal: Open a new tab after prompt input. Why: (1) Flask endpoint is replacing the need for Lambda URL. It means you can recreate a new Lambda named Darwin without manually updating this repo. (2) Main advantage of API Gateway over Lambda URLs is throttling and quotas for preventing uncontrolled expenses inside usage plans. (3) Use GH Secrets for SDK and EB URL within yml.

```
Codespace is (1) track record without PRs: git stash for temporary git commit, git rev-list --count --all,
git rebase -i HEAD~122, sed -i 's/pick/drop/g' .git/rebase-merge/*-todo, git add ., git commit -m "Setup", git push -u origin 
(2) branch: git checkout -b "main", git push origin main, git log, git reset --hard "commit-SHA" to discard all commits after a certain date. 
(3) wrap it up: git pull origin main, git config pull.rebase true, git push -u origin, git push origin gh-pages --force.
```

Run http.server, copy ~/.aws/credentials for SDK. No need for CDN. Store variables inside AWS Secrets Manager. Not your .env file. File .gitignore is used if you deploy from your computer. Learn more from MERN boilerplate or Wrangler Astro. Cost: API Gateway charges for the number of requests processed and data transferred, while Lambda charges for the duration your code executes and memory consumed. Lambda saves money over Fargate only when it runs a quarter or less of the day. If many API requests then Fargate wins.

```
To delete cached files: git reset --soft HEAD~ && git commit --amend, git checkout --orphan newBranch, git add -A,
git commit -m "Ok", git branch -D main, git branch -m main, git push -f origin main, git gc --aggressive --prune=all 
```

CI/CD Pipeline: Use Elastic Beanstalk for prototyping GitHub Actions workflow with Secrets Manager to handle client-side features (CI). Asynchrous execution is parallel functions. First redirect user to previous output inside S3. Then **L** execute CodeBuild inside rest parsing (CD). User must refresh / reload the webpage to see their output. Feel free to contact me at **support@brageon.com** for pull request or another good-to-know or good-to-have-feature.
