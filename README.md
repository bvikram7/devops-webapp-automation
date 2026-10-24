# DevOps Web Application Automation Demo

## Project objective
Demonstrate a basic DevOps workflow using a small Python web application, Git/GitHub, automated tests, GitHub Actions, and Docker.

## Technology stack
- Python and Flask: web application
- Git and GitHub: source control
- GitHub Actions: continuous integration (CI)
- Docker: containerization
- `unittest`: automated tests

## Run locally without Docker
Requires Python 3.10 or later.

```bash
python -m venv .venv
```

Activate the environment:
- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

Then run:

```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in a browser. Health check: `http://127.0.0.1:5000/health`.

Run tests:

```bash
python -m unittest -v
```

## Run with Docker
Install and start Docker Desktop first, then run from this project folder:

```bash
docker build -t devops-demo-web .
docker run --rm -p 5000:5000 devops-demo-web
```

Alternatively, with Docker Compose:

```bash
docker compose up --build
```

Open `http://localhost:5000`. Stop Compose with `Ctrl+C`, then run `docker compose down` if needed.

## Enable the CI workflow
1. Create a GitHub repository.
2. Upload/push all project files, including `.github/workflows/ci.yml`.
3. Open the repository's **Actions** tab.
4. Push a small code change or open a pull request.
5. Show the workflow run: it installs dependencies, runs tests, and builds the Docker image.

## Viva explanation
“When code is pushed to GitHub, GitHub Actions automatically installs the Python dependencies, runs unit tests, and builds a Docker image. Docker packages the application and its dependencies into a portable container. The `/health` endpoint provides a simple health check.”

## Scope and limitations
This is a learning/demo project. The workflow builds a Docker image but does not publish it to a registry or deploy to a cloud/Kubernetes cluster. Add those only if you have time and can explain them accurately. Do not describe a CI run or deployment as completed until you have actually run and verified it.
