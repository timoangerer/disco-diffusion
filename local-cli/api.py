from operator import concat
import sys
import os
import re
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import boto3

client = boto3.client('batch')
import uuid

def create_job(job_dto: dict):
    if "batch_name" in job_dto:
        job_dto["batch_name"] = f"{job_dto['batch_name']}-{uuid.uuid4()}"
    else:
        job_dto["batch_name"] = str(uuid.uuid4())

    print("job_dto: ", job_dto)
    
    send_aws_batch_job(job_dto)

def send_aws_batch_job(job_dto):
    container_command = generate_container_cmd(job_dto)

    tags = {str(k): "".join(re.findall("[a-zA-Z0-9_/+\-\=. ]*", str(v))) for (k,v) in job_dto.items()}
    print("Tags: ", tags)

    response = client.submit_job(
        jobName=job_dto["batch_name"],
        jobQueue='job-queue-dd1',
        jobDefinition='job-definition-dd1',
        containerOverrides={
            'command': container_command
        },
        propagateTags=False,
        tags=tags
    )

    print("Submit job response: ", response)

def generate_container_cmd(paramters):
    params_list = [f'{k}={json.dumps(v)}' for (k,v) in paramters.items()]
    params_list = concat(["python", "disco.py"], params_list)
    return params_list