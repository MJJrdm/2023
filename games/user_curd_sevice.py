from django.db.models.query import QuerySet
from django.contrib.auth.models import User

from django.db import transaction
import logging

LOGGER = logging.getLogger(__name__)


# TODO: 'get' method not found handel


class UserInfoCRUDService():
    @transaction.atomic
    def create(self, user_name: str,
               password: str) -> None:
        User.objects.create_user(username=user_name, password=password)

    def put(self, user_name: str,
            password: str) -> None:
        # User.objects.filter(username=user_name).update(password=password)
        user = User.objects.get(username=user_name)
        user.set_password(password)
        user.save()

    def delete(self, user_name: str) -> None:
        User.objects.filter(username=user_name).delete()

    def get(self, user_name: str) -> QuerySet:
        return User.objects.filter(username=user_name).values("password")
