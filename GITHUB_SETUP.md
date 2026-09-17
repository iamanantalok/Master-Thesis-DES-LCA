# One-time GitHub setup

## 1. Create the repo

On GitHub: **New repository** → name it (e.g. `thesis-simpy`) → choose
public or private → **do not** initialize with a README (you already have
one here) → Create.

## 2. Push this starter to it

From a terminal, inside this folder:

```bash
git init
git add -A
git commit -m "Initial repo structure"
git branch -M main
git remote add origin https://github.com/<your-username>/thesis-simpy.git
git push -u origin main
```

## 3. Create a GitHub token for Colab

Colab needs a token to push on your behalf (your GitHub password won't work
for git operations anymore).

1. GitHub → Settings → Developer settings → Personal access tokens →
   Fine-grained tokens → Generate new token.
2. Scope it to just this repo, with **Contents: Read and write** permission.
3. Copy the token — GitHub only shows it once.

## 4. Store the token in Colab

In any Colab notebook, click the key icon (🔑) in the left sidebar →
**Secrets** → add a new secret named `GITHUB_TOKEN` with the token as its
value → toggle "Notebook access" on.

You can now use the clone/push commands from the README in any Colab
session without pasting the token into a cell.
