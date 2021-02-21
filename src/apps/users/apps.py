from django.apps import AppConfig


# noinspection PyUnresolvedReferences
class AccountsConfig(AppConfig):  # pragma: no cover
    name = 'users'
    app_label = 'users'

    def ready(self):
        import apps.users.signals
