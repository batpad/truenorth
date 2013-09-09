#this is a fabfile, use it with fab from http://fabfile.org/
#
# initial setup:
# fab production setup
#
# deploy changes:
# fab production deploy
#

from os.path import join 
from fabric.api import run, local, sudo, put, env

env.project_name = 'truenorth'


def production():
    env.hosts = ['%(project_name)s@marlon.in'%env, ]
    env.project_root = '/srv/%(project_name)s'%env

def git_push():
    local('git push'%env)

def git_update():
    run('cd %(project_root)s;git pull'%env)

def virtual_run(cmd, *a, **kw):
    cmd = 'cd %s; source bin/activate; %s' % (env.project_root, cmd)
    run(cmd, *a, **kw)

def update_requirements():
    run('pip -E %(project_root)s install -r %(project_root)s/requirements.txt'%env)

def setup():
    """
    Setup a fresh virtualenv
    """
    local('bzr push --use-existing-dir bzr+ssh://%(project_name)s@%(host)s%(project_root)s'%env)
    run('cd %(project_root)s; test -e .bzr/checkout || bzr checkout'%env)
    run('virtualenv %(project_root)s'%env)
    put(join('settings', '%(host)s.py'%env), join(env.project_root, env.project_name, 'local_settings.py'))
    update_requirements()

def deploy():
    git_push()
    git_update()
    virtual_run('python %(project_root)s/manage.py collectstatic --noinput'%env)
    # virtual_run('python %(project_root)s/%(project_name)s/manage.py syncdb;python %(project_root)s/%(project_name)s/manage.py migrate'%env)
    run('touch %(project_root)s/wsgi/django.wsgi'%env)
