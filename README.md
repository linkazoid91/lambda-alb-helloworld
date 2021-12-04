# lambda-alb-helloworld

## Required Github secrets
```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
AWS_VPC_ID
AWS_PUBLIC_SUBNET_1
AWS_PUBLIC_SUBNET_2
AWS_BUCKET_NAME
TIMEOUT_PERIOD
```

## What does this do?

This project will create a lambda in AWS via cloudformation, and serve its responses via HTTP using an Application Load Balancer.

Some projects will require an API to have a timeout period exceeding 60 seconds, in cases like this API Gateway is not suitable and you must use either Cloudfront, or ALB.
