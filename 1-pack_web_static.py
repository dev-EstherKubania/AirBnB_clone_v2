#!/usr/bin/python3
"""
This script generates a .tgz archive from the contents of the web_static
folder. The archive is stored in the 'versions' folder with a filename
following the format: web_static_<year><month><day><hour><minute><second>.tgz
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    :return: The path of the generated archive if successful, otherwise None.
    """
    local("mkdir -p versions")

    now = datetime.utcnow()
    date_string = now.strftime("%Y%m%d%H%M%S")

    archive_name = "web_static_{}.tgz".format(date_string)

    result = local("tar -cvzf versions/{} web_static".format(archive_name))

    if result.succeeded:
        print("Archive created: versions/{}".format(archive_name))
        return "versions/{}".format(archive_name)
    else:
        print("Failed to create archive.")
        return None


do_pack()
