"""
Thesis simulation model — SimPy.

Keep this file as the clean, current version of the model. Exploratory
variants belong in experiments.ipynb or in learning-log/, not here.
"""

import simpy


def example_process(env, name):
    """Placeholder process — replace with the thesis model's actual logic."""
    print(f"{name} starting at {env.now}")
    yield env.timeout(1)
    print(f"{name} finished at {env.now}")


def run():
    env = simpy.Environment()
    env.process(example_process(env, "process-1"))
    env.run(until=10)


if __name__ == "__main__":
    run()
