from django.apps import AppConfig


class ParametersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'level_up.parameters'

    def ready(self) -> None:
        from . import signals
        return super().ready()
