from fabric import Connection


def cleanup(host):
    username = "vannia"
    port = 22
    with Connection(
        f"{username}@{host}:{port}", connect_kwargs={"password": "pw"}
    ) as conn:
        output = conn.run("docker images")
        print.output.stdout
