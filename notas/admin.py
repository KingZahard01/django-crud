from django.contrib import admin

# Username: juan
# Email: juan@email.com
# Password: password

# Register your models here.

from notas.models import Nota

admin.site.register(Nota)
