ARG VARIANT=ubuntu-24.04
FROM mcr.microsoft.com/vscode/devcontainers/base:${VARIANT}


ENV TZ=UTC
ENV DEBIAN_FRONTEND=noninteractive
ENV DEVCONTAINER=true

RUN apt-get update
RUN apt-get -y upgrade

RUN apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    git \
    make \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev

# Install Pyenv
RUN curl https://pyenv.run | bash
RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
RUN echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc

RUN /root/.pyenv/bin/pyenv install 3.12
RUN /root/.pyenv/bin/pyenv global 3.12
RUN apt-get install -y --no-install-recommends postgresql postgresql-contrib libpq-dev
RUN ls /root/.pyenv/bin
RUN /root/.pyenv/shims/python -m pip install --upgrade pip
RUN /root/.pyenv/shims/python -m pip install psycopg2


# __DEVCONTAINER_SNIPPET_INSERT__ (control where snippets get inserted using the devcontainer CLI)


# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog