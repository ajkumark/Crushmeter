from django.contrib import admin
from crushapp.models import Crush

class RatingAdmin(admin.ModelAdmin):
	readonly_fields = ('time',)

admin.site.register(Crush, RatingAdmin)