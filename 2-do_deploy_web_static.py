#!/usr/bin/python3
"""
Fabric script that distrubutes an archive to your web servers,using the
function do_deploy
"""


from fabric.api import env, local, put, run
import os
env.hosts = ['54.90.59.65', '18.235.248.54']


def do_deploy(archive_path):
    """ function that deploys an archive to your web servers"""
    try:
        filename = archive_path.split('/')[-1]
        file_no_ext = filename.split('.')[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, file_no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filename, path, file_no_ext))
        run('rm /tmp/{}'.format(filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_no_ext))
        run('rm -rf {}{}/web_static'.format(path, file_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, file_no_ext))
        return True
    except Exception:
        return False