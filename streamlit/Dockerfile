FROM python:3.12-slim

ARG user
ARG uid

# Buat user dan group
RUN groupadd -g $uid $user && \
    useradd -r -u $uid -g $user $user && \
    mkdir /app && \
    mkdir /home/$user && \
    chown -R $user:$user /app && \
    chown -R $user:$user /home/$user

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV PATH=/home/$user/.local/bin:$PATH
ENV HOME=/home/$user

RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Tambahkan timeout
RUN pip install \
    --user \
    --no-cache-dir \
    --default-timeout=100 \
    -r requirements.txt

USER $user

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]