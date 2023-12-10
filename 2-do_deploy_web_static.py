#!/usr/bin/python3
"""
Fabric script for deploying an archive to web servers.
"""

from fabric.api import local, put, run, env
from os.path import exists

env.hosts = ['34.232.70.187', '34.204.101.142']
env.user = 'ubuntu'  # Replace with your SSH username


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.
    :param archive_path: The local path to the archive to be deployed.
    :return: True if all operations have been done correctly, otherwise False.
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        archive_filename = archive_path.split("/")[-1]
        release_folder = '/data/web_static/releases/{}'.format(
            archive_filename.split(".")[0]
        )
        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_filename))

        # Delete the symbolic link /data/web_static/current
        run('rm -f /data/web_static/current')

        # Create a new symbolic link /data/web_static/current
        run('ln -s {} /data/web_static/current'.format(release_folder))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed: {}".format(str(e)))
        return False
