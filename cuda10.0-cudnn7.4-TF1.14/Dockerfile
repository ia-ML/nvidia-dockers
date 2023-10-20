# Start from Ubuntu 18.04 base image
FROM ubuntu:18.04

# Set non-interactive mode for apt-get to run without human intervention
ENV DEBIAN_FRONTEND=noninteractive

# Install basic dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    software-properties-common \
    curl \
    libfreetype6-dev \
    libpng-dev \
    libzmq3-dev \
    pkg-config \
    rsync \
    unzip \
    python3-dev \
    python3-pip \
    python3-wheel \
    python3-setuptools \
    libsm6 \
    libxext6 \
    libxrender-dev \
    git \
    wget \
    gnupg \  
    gnupg2 \ 
    nano \ 
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install CUDA Toolkit 10.0
# first download the file and place it next to this Dockerfile
COPY cuda-repo-ubuntu1804-10-0-local-10.0.130-410.48_1.0-1_amd64.deb /tmp/cuda-repo-ubuntu1804-10-0-local-10.0.130-410.48_1.0-1_amd64.deb
RUN dpkg -i /tmp/cuda-repo-ubuntu1804-10-0-local-10.0.130-410.48_1.0-1_amd64.deb
#RUN ls  /var/cuda-repo-10-0-local-10.0.130-410.48 && false
RUN apt-key add /var/cuda-repo-10-0-local-10.0.130-410.48/7fa2af80.pub
RUN apt-get -y update
RUN apt-get -y install cuda

# first download the file and place it next to this Dockerfile
# Copy the cuDNN runtime library from the host into the container
COPY libcudnn7_7.4.2.24-1+cuda10.0_amd64.deb /tmp/libcudnn7_7.4.2.24-1+cuda10.0_amd64.deb

# Install cuDNN runtime library
RUN dpkg -i /tmp/libcudnn7_7.4.2.24-1+cuda10.0_amd64.deb && \
    rm /tmp/libcudnn7_7.4.2.24-1+cuda10.0_amd64.deb

# first download the file and place it next to this Dockerfile
# Copy the cuDNN developer library from the host into the container
COPY libcudnn7-dev_7.4.2.24-1+cuda10.0_amd64.deb /tmp/libcudnn7-dev_7.4.2.24-1+cuda10.0_amd64.deb

# Install cuDNN developer library
RUN dpkg -i /tmp/libcudnn7-dev_7.4.2.24-1+cuda10.0_amd64.deb && \
    rm /tmp/libcudnn7-dev_7.4.2.24-1+cuda10.0_amd64.deb

ENV PATH /usr/local/cuda-10.0/bin:${PATH}
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install Python libraries for data science
RUN pip3 install --upgrade pip
RUN pip3 install \
    numpy \
    pandas \
    scipy \
    scikit-learn \
    matplotlib \
    seaborn \
    jupyter \
    jupyterlab \
    ipywidgets \
    dlib \
    notebook

# Install TensorFlow GPU 1.14
RUN pip3 install tensorflow-gpu==1.14

# Set up the working directory
WORKDIR /workspace
RUN chmod -R a+w /workspace

# Jupyter Notebook config
EXPOSE 8888
CMD ["jupyter", "notebook", "--ip='0.0.0.0'", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
