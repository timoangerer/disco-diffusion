### Publish to ECR
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/c7b2u5o4

docker build -t disco-diffusion .

docker tag disco-diffusion:latest public.ecr.aws/c7b2u5o4/disco-diffusion:latest

docker push public.ecr.aws/c7b2u5o4/disco-diffusion:latest