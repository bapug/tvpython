from django.apps import AppConfig as BaseAppConfig
from importlib import import_module


class AppConfig(BaseAppConfig):

    name = "bapug"

    def ready(self):
        import_module("bapug.receivers")
