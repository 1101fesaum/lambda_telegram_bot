# lambda_telegram_bot
A simple telegram bot that works trough aws lambda

Virtual Env variables needed:

TELEGRAM_TOKEN: (this is your bot token)  
BOT_ID: (this is your telegram user id)  
AWS credentials can be set as per documentation [recomendation](https://docs.aws.amazon.com/es_es/cli/latest/userguide/cli-chap-configure.html)  

To set the url of the webhook run:
``` 
curl --request POST --url https://api.telegram.org/<YOOUR TOKEN>/setWebhook --header 'content-type: application/json' --data '{"url": "https://u3ir5tjcsf.execute-api.us-east-1.amazonaws.com/dev/my-custom-url"}'
``` 

To get more information about the required api gateway permissions go to: [api gateway docs](https://github.com/awsdocs/amazon-api-gateway-developer-guide/blob/master/doc_source/api-gateway-control-access-using-iam-policies-to-create-and-manage-api.md)

To install the requirements and generate the requirements file run:  
```  
$ pipenv install   
$ pipenv lock --requirements > requirements.txt  
```  

This lambda is deployed with: [Python-lambda](https://github.com/nficano/python-lambda)  

to execute a test the function head to pylambda/ dir and run:  

```  
$ lambda invoke -v  
```
to deploy it to aws run:  
```
$ lambda deploy --requirements requirements.txt  
```
