import docker

COMMANDS = {
    "ubuntu": {
        "update-index": "DEBIAN_FRONTEND=noninteractive apt update",
        "install": "DEBIAN_FRONTEND=noninteractive apt install",
        "remove": "DEBIAN_FRONTEND=noninteractive apt remove",
        "upgrade": "DEBIAN_FRONTEND=noninteractive apt upgrade"
    },
    "alpine": {
        "update-index": "apk update",
        "install": "apk add",
        "remove": "apk del",
        "upgrade": "apk add -u"
    },
    "fedora": {
        "update-index": "dnf upgrade --refresh -y",
        "install": "dnf install -y",
        "remove": "dnf remove -y",
        "upgrade": "dnf upgrade -y"
    }
}

client = docker.from_env()

def update_index(container):
    client.containers.get(f"containerpkg_managed_{container}").start()
    client.containers.get(f"containerpkg_managed_{container}").exec_run(COMMANDS[container]["update-index"], tty=True)

def install(container, package):
    client.containers.get(f"containerpkg_managed_{container}").start()
    client.containers.get(f"containerpkg_managed_{container}").exec_run(COMMANDS[container]["install"] + " " + package, tty=True)

def remove(container, package):
    client.containers.get(f"containerpkg_managed_{container}").start()
    client.containers.get(f"containerpkg_managed_{container}").exec_run(COMMANDS[container]["remove"] + " " + package, tty=True)

def upgrade(container, package):
    client.containers.get(f"containerpkg_managed_{container}").start()
    client.containers.get(f"containerpkg_managed_{container}").exec_run(COMMANDS[container]["upgrade"] + " " + package, tty=True)

def run(container, command):
    client.containers.get(f"containerpkg_managed_{container}").start()
    client.containers.get(f"containerpkg_managed_{container}").exec_run(command, tty=True)