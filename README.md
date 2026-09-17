# Thesis SimPy — Learning Log & Simulation Model

This repo documents my process of learning [SimPy](https://simpy.readthedocs.io/)
(a discrete-event simulation library for Python) and building the simulation
model for my thesis.

## Structure

- `learning-log/` — SimPy tutorial notebooks, numbered in the order I worked
  through them. Exploratory and messy on purpose — this is where I try things.
- `thesis-model/` — the actual thesis simulation code, kept clean and runnable.
- `docs/` — longer-form notes: design decisions, references, assumptions.
- `LOG.md` — a dated journal of what I did, what I learned, and what's next.

## Setup

```bash
pip install -r requirements.txt
```

## Running in Google Colab

Each session, clone this repo into the Colab VM and work from there so changes
can be pushed back:

```python
from google.colab import userdata
TOKEN = userdata.get('GITHUB_TOKEN')  # stored as a Colab secret
!git clone https://{TOKEN}@github.com/<your-username>/thesis-simpy.git
%cd thesis-simpy
```

After making changes:

```python
!git add -A
!git commit -m "Describe what changed"
!git push
```

## Thesis context

*(Add a short paragraph here once the thesis topic/scope is settled — what
the simulation is modeling and why SimPy was chosen for it.)*
