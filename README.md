# Prebuilt DevContainers with GitHub Actions

## Overview
This repository automates the prebuilding of DevContainers using GitHub Actions. Prebuilt DevContainers speed up development setup by reducing build times, especially when using complex configurations.

## Features
- **Automated DevContainer builds** using GitHub Actions
- **Multi-architecture support** (`amd64` and `arm64`)
- **GitHub Container Registry (GHCR) integration** for storing and retrieving prebuilt images

## Setup
### Prerequisites
- Docker installed locally (optional, for manual builds)
- GitHub account with access to GitHub Actions
- GitHub Container Registry enabled

### Enabling GitHub Container Registry (GHCR)
1. Create a **Personal Access Token (PAT)** with `write:packages` and `read:packages` permissions.
2. Store the token as a **GitHub Actions secret** named `GHCR_PAT`.

## Usage
### Running the GitHub Actions Workflow
The prebuilt DevContainer is automatically built and pushed to GHCR when:
- A commit is pushed to the `main` branch
- The workflow is manually triggered

### Workflow Overview
The GitHub Actions workflow performs the following steps:
1. **Checkout the repository**
2. **Setup QEMU and Buildx** for multi-architecture builds
3. **Login to GitHub Container Registry (GHCR)**
4. **Build and push the DevContainer image**

### Using the Prebuilt DevContainer
To use the prebuilt container in VS Code:
1. Open the repository in VS Code.
2. Ensure the **Dev Containers** extension is installed.
3. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and select `Dev Containers: Rebuild and Reopen in Container`.

## Notes
- Building for multiple architectures (`amd64` and `arm64`) can be slow (~1 hour on GitHub runners).
- Consider using **self-hosted runners** for faster builds.

## License
This repository is licensed under the MIT License.

## Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request.

---
🚀 [**Speed up your DevContainer setup with prebuilt images!**](https://devcontainer.community/20250303-prebuild-devcontainer/)

