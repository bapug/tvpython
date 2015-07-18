import re
import os

from fabric.api import *
from fabric.contrib.files import *
from fabric.network import ssh

env.use_ssh_config = True
env.disable_known_hosts = True
env.skip_bad_hosts = True

env.key_filename = [os.path.join(os.environ['HOME'], '.ssh', 'gardenbuzz.pem')]

ssh.util.log_to_file("paramiko.log", 10)

@hosts('django@tvpython.org')
def release():
    with cd("/home/django/sites/tvpython"):
        run("./siteupdate.sh")


