FROM node:20-bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        python3 python3-venv python3-pip \
        git ca-certificates curl unzip xz-utils ripgrep \
 && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 -s /bin/bash dev \
 && mkdir -p /workspace /etc/opencode \
 && chown dev:dev /workspace

# Project dependencies are resolved at BUILD time (the build has network).
# At runtime the container has no route to the internet, so it cannot install anything.
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m venv /opt/venv \
 && /opt/venv/bin/pip install --upgrade pip \
 && /opt/venv/bin/pip install -r /tmp/requirements.txt pytest \
 && rm -f /tmp/requirements.txt

USER dev
ENV HOME=/home/dev \
    XDG_CONFIG_HOME=/home/dev/.config \
    XDG_CACHE_HOME=/home/dev/.cache \
    XDG_DATA_HOME=/home/dev/.local/share \
    PATH=/home/dev/.opencode/bin:/opt/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    OPENCODE_DISABLE_PROJECT_CONFIG=1 \
    OPENCODE_DISABLE_EXTERNAL_SKILLS=1 \
    OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1

# Install opencode, pinned, into the dev user's home.
RUN curl -fsSL https://opencode.ai/install \
      | bash -s -- --version 1.18.35 --no-modify-path

# Bake the models.dev registry + cache dir so opencode works fully offline.
RUN mkdir -p /home/dev/.cache/opencode /home/dev/.local/share/opencode /home/dev/.config/opencode \
 && curl -fsSL https://models.dev/api.json -o /home/dev/.cache/opencode/models.json

WORKDIR /workspace
ENTRYPOINT ["opencode"]
CMD ["--help"]
