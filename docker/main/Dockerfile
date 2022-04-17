# Model prep phase, also cuts down on build context wait time since these models files
# are large and prone to take long to copy...
FROM disco-diffusion-prep:5.1 AS modelprep

FROM nvcr.io/nvidia/pytorch:21.08-py3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set up code directory
RUN mkdir code
WORKDIR /workspace/code

# Install a few dependencies
RUN apt update
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install -y tzdata imagemagick

# Create a disco user
RUN useradd -ms /bin/bash disco
USER disco

# Copy over models used
COPY --from=modelprep /scratch/models /workspace/code/models
COPY --from=modelprep /scratch/pretrained /workspace/code/pretrained

# Precache other big files
COPY --chown=disco --from=modelprep /scratch/clip /home/disco/.cache/clip
COPY --chown=disco --from=modelprep /scratch/model-lpips/vgg16-397923af.pth /home/disco/.cache/torch/hub/checkpoints/vgg16-397923af.pth

# Clone Git repositories
RUN git clone https://github.com/openai/CLIP && \
    git clone https://github.com/assafshocher/ResizeRight.git && \
    git clone https://github.com/MSFTserver/pytorch3d-lite.git && \
    git clone https://github.com/isl-org/MiDaS.git && \
    git clone https://github.com/crowsonkb/guided-diffusion.git && \
    git clone https://github.com/shariqfarooq123/AdaBins.git

USER root
RUN apt-get -y install awscli
USER disco

# Install Python packages
RUN pip install imageio imageio-ffmpeg==0.4.4 pyspng==0.1.0 lpips datetime timm ipywidgets omegaconf>=2.0.0 pytorch-lightning>=1.0.8 torch-fidelity einops wandb pandas ftfy
RUN pip install omegaconf hydra-core
RUN pip install boto3

# Copy default settings file
COPY config/defaults.yaml config/

# Copy disco diffusion source code
COPY disco_xform_utils.py ./
COPY disco.py ./
