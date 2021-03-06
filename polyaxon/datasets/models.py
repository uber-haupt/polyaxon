import os

from django.conf import settings
from django.core.validators import validate_slug
from django.db import models

from libs.blacklist import validate_blacklist_name
from libs.models import DiffModel, DescribableModel


class Dataset(DiffModel, DescribableModel):
    """A model that represents a dataset."""
    name = models.CharField(
        max_length=256,
        validators=[validate_slug, validate_blacklist_name])
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='datasets')
    version = models.PositiveSmallIntegerField(default=1)
    is_public = models.BooleanField(
        default=True,
        help_text='If the dataset is public or private.')

    @property
    def user_path(self):
        return os.path.join(settings.DATA_ROOT, self.user.username)

    @property
    def path(self):
        return os.path.join(self.user_path, self.name, str(self.version))

    def get_tmp_tar_path(self):
        return os.path.join(self.path, '{}_new.tar.gz'.format(self.name))
