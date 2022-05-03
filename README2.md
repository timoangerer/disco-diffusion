### Publish to ECR
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/c7b2u5o4

docker build -t disco-diffusion:lastest -f docker/main/Dockerfile .

docker tag disco-diffusion:latest public.ecr.aws/c7b2u5o4/disco-diffusion:latest

docker push public.ecr.aws/c7b2u5o4/disco-diffusion:latest

### Run the container

docker build -t disco-diffusion:latest -f docker/main/Dockerfile .

docker run --rm --gpus all --ipc host disco-diffusion:latest python disco.py steps=15 n_batches=1 text_prompts='{0: ["A Dog"]}'