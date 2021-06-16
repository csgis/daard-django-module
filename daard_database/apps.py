from django.apps import AppConfig


class DaardDatabaseConfig(AppConfig):
    name = 'daard_database'

    def ready(self):
        import daard_database.signals #noqa
