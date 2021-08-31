# Goal

Setup infrastrcture to delivery cloudvelum cloudformation template to s3, so users can just use that s3 url and create a stack from it


- Will eventually have this in a public/prod bucket , but for now just run in sandbox
- Need a bucket to hold the cloudvelum versions
- Needs a bucket to hold the cloudvelum 'media artifacts' - these are images that are used by cloudvelum to display on a dashboard or as an icon in a slack message - basically these just need to be synced up to the bucket and then we can reference the urls
- the cloudvelum versions and the medias assets can be in the same bucket unless we can find a reason why not
- Gitlab script! set this up to just run

`/scripts` folder has some scripts i have been workiing on that has basically a POC of this done

`/scripts/build.sh` - intended to build the sam tempalte and create the cloudformation template (a little bit of trickery going on to get the lambda layer packaged, this might not be needed, i cant remember exactly the issue i was having that made me want to do that)

`/scripts/publish.sh` - intended to take the build output template yaml and upload to our target s3 location (considering the version in the s3 object name) - it also runs the sync on the media folder (potential for jsut deploying this to aws's Serverless applicaiton repository too, which could be better than doing it to s3? - however, i don thtink the SAR would be able to handle the multiaccount hub/spoke model we will eventually use)

`/scipts/deploy.sh` - intended to be used for local dev only, this is what i use to actually deploy my appliation changes to sandbox account so i can see if its working,


p.s.

> thanks Jameson

<p align="center">
  <img width="100%" src="https://avatars2.githubusercontent.com/u/9866096?s=460&u=213f29de261b87d34174f1cf13554cd0da8c9046&v=4">
</p>