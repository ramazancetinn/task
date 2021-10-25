## Requirements

* python3
* cdk
* aws cli
* kubectl

aws and aws cli `CDKDeployUser` credentials shared with e-mail.

## How to Run

### Deploy Serverless Application
1. Go to `serverless-application` folder
2. `python3 -m pip install -r requirements.txt ` 
3. Run
    ```
        cdk bootstrap
        cdk deploy
    ```

### Create EKS and ECR
1. Go to `iaac` folder
2. `python3 -m pip install -r requirements.txt ` 
3. Run 
    ```
        cdk bootstrap
        cdk deploy
    ```
4. After ECR created you can login to ECR vai following commands (for MacOs/Linux)
    ```
        aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 050884211926.dkr.ecr.eu-west-1.amazonaws.com
    ```
5. After EKS created copy the ConfigCommand from your terminal output and execute it, it should look something like this:
    ```
    aws eks update-kubeconfig --name EKSStack-cluster --region eu-west-1 --role-arn arn:aws:iam::050884211926:role/EKSStack-iam
    ```

### Build Web Application && Deploy Kubernetes
1. Go to `web-app` folder
2. Run docker build command with ecr repository tag
    ```
        docker build -t 050884211926.dkr.ecr.eu-west-1.amazonaws.com/web-app:latest .
    ```
3. Push docker image to ECR
    ```
        docker push 050884211926.dkr.ecr.eu-west-1.amazonaws.com/web-app:latest
    ```
4. Deploy k8s yaml
    ```
        kubectl create -f k8s/deployment.yaml
        kubectl create -f k8s/service.yaml
    ```
5. Run following to get web-app url
    ```
    kubectl get svc
    ```
    You should see something like:
    ```
        xxxxxxxxxxxxxx.eu-west-1.elb.amazonaws.com
    ```



## Technologies & Languages

### 1. CDK (Cloud Development Kit)
#### Reasons
* Plus for task 
* Documentation is really simple and understandable.
#### References
* https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_s3/README.html
* https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_eks/README.html
* https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ecr/README.html
* https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_lambda/README.html
* https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_dynamodb/README.html

### EKS
#### Reasons
* Easy to use
* Want to try EKS service
#### References
* https://aws.amazon.com/getting-started/guides/deploy-webapp-eks/

### Next.js
#### Reasons
* Worked on a project before
* Faster development for me

### Python
#### Reasons
* Easy to use 
* Easy to find resource

    
    