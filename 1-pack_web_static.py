#!/usr/bin/python3
"""
Fabric script to generate a zip archive file for web_static directory
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """pack function to generate a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        filename = "versions/web_static_{}.tgz".format(date)
        local("tar -czvf {} web_static/".format(filename))
        return filename
    except Exception:
        return None