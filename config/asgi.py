"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()

"""
The early life of one Jalal Belsifar

was frought with wild adventures 

as a boy who lived his life growing up 

on the African Savanna, conferring with

birds and wrestling crocodiles.
"""