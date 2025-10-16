from crum import get_current_request
from django.forms import model_to_dict

from config.settings import MEDIA_URL, STATIC_URL
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    groups = models.ManyToManyField(
        Group,
        related_name='user_groups',
        blank=True,
        verbose_name='Grupos'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_permissions',
        blank=True,
        verbose_name='Permisos de usuario'
    )

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'assets/img/user2-160x160.jpg')

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'user_permissions'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['image'] = self.get_image()
        item['full_name'] = self.get_full_name()
        item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
        return item

    def get_group_session(self):
        try:
            request = get_current_request()
            groups = self.groups.all()
            if groups.exists():
                if 'group' not in request.session:
                    request.session['group'] = groups[0]
        except:
            pass

    @property
    def fullname(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}".strip()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['id']