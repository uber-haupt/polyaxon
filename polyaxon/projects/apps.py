from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    name = 'projects'
    verbose_name = 'Projects'

    def ready(self):
        from projects.signals import (
            new_experiment_group,
            experiment_group_deleted,
            new_project,
            project_deleted,
        )
