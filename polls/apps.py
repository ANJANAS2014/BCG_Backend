from django.apps import AppConfig


class PollsConfig(AppConfig):
    name = 'polls'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        # Run the code to monitor the filesystem for changes
        print("Common loaded.")
