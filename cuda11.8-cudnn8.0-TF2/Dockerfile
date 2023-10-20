# Use an NVIDIA CUDA base image
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    libgl1-mesa-glx \
    libglib2.0-0 \
    nano \
    && rm -rf /var/lib/apt/lists/*

# Create symbolic links for python3 and pip3
RUN ln -s -f $(which python3) /usr/bin/python && ln -s -f $(which pip3) /usr/bin/pip

# Install Flask and any other necessary Python packages
RUN pip install Flask Pillow opencv-python gunicorn pandas torch torchvision torchaudio tensorflow
RUN pip install scikit-image scipy matplotlib
RUN pip install pyyaml fastprogress ffmpeg yt_dlp IPython dill dlib

# Create a directory for your application
WORKDIR /app

# Copy your source code into the image
COPY src /app

# Expose the port your Flask app runs on
EXPOSE 5000

# Command to run your Flask app
# gunicorn -w 4 -b 0.0.0.0:5000 server:app
CMD ["gunicorn", "-w 4","-b 0.0.0.0:5000","server:app"]

