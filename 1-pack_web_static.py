#!/usr/bin/python3
"""
This module creates a tgz file of the web_static directory
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    try:
        # Create the versions folder if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Get the current date and time
        now = datetime.now()

        # Format the current date and time
        date_time = now.strftime("%Y%m%d%H%M%S")

        # Name of the archive
        archive_name = "web_static_" + date_time + ".tgz"

        # Path to the archive
        archive_path = "versions/" + archive_name

        # Create the .tgz archive
        local("tar -czvf {} web_static".format(archive_path))

        return archive_path
    except Exception as e:
        return None


if __name__ == '__main__':
    do_pack()
