
# Register your models here.
from django.contrib import admin
from .models import CentreFormation, Personne, Formation, SessionFormation, Commentaire

admin.site.register(CentreFormation)
admin.site.register(Personne)
admin.site.register(Formation)
admin.site.register(SessionFormation)
admin.site.register(Commentaire)
