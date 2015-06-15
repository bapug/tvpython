#!/usr/bin/env python

import os
import sys

def local_exists():
    """
    Check for a local_config.py file. If it exists, we will use this file to
    bootstrap the settings. Look at local_config.py.sample for an examle version.
    """
    for p in sys.path:
        lc = os.path.join(p,'local_config.py')
        if os.path.exists(lc):
            print("Found local_config.py here:{}".format(lc))
            return True

    return False

if __name__ == "__main__":
    if local_exists():
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "local_config")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tvpython.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
