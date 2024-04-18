#!/usr/bin/python3
"""
This module distributes an archive to web servers
"""

from fabric.api import local
from datetime import datetime
from fabric import Connection
from fabric.api import env
import os
from fabric.api import task

env.hosts = ['100.25.24.173', '54.237.54.104']
env.user = "ubuntu"

@task
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
@task
def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if os.path.exists(archive_path):
        
        archive_filename = os.path.basename(archive_path)
        filename_without_extension = os.path.splitext(archive_filename)[0]
        # Individual connection
        try:
            for host in hosts:
                with Connection(host=f"{host}", user=env.user, connect_kwargs={"key_filename": "/home/chigow/.ssh/school",}) as c:
                    c.put(archive_path, '/tmp/')
                    c.run(f'tar -xvzf /tmp/{archive_filename} -C /data/web_static/releases/{filename_without_extension}')
                    c.run(f'rm /tmp/{archive_filename}')
                    c.run(f'ln -sf /data/web_static/current /data/web_static/releases/{filename_without_extension}')
            return True
        except Exception as e:
           print(f'Something failed here!{e}')
           return False

if __name__ == '__main__':
    archive_path = do_pack()
    if archive_path:
        do_deploy(archive_path)
