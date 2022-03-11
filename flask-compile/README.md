# Flask-Pythonfile Compile and Docker push


# Edit Part

## buildspec.yml
- "<aws_region>" => Your AWS ECR Repository Region
- "<access_id>" => Your AWS Acount id 
- "<ecr_name>" => Your ECR Repository Name

## appspec.yml

None

# Setup IAM

## codebuild 

The basic permission section is not covered, and the permission to be added 
in the current code are as follows.

codebuild role policy in ecr full Permission
