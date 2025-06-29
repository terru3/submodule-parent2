from submodule.models import Repository, Env

bruh = Repository(repo_name="yuh", repo_function="type sh")

env = Env.DEV
print(f"Env: {env}")
