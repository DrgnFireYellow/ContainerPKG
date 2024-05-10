import docker
import os
client = docker.from_env()

def download(container):
    client.images.pull(container)
    client.containers.create(container, "sleep 10", network="host", environment={"DISPLAY": os.environ.get("DISPLAY")}, volumes={os.path.join(os.path.expanduser("~"), ".Xauthority"): {"bind": os.path.join("/", "root", ".Xauthority"), "mode": "rw"}}, name=f"containerpkg_managed_{container}")

