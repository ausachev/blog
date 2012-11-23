from django.contrib import admin
from mysite.weblog.models import BolgPost


class PostAdmin(admin.ModelAdmin):
	"""docstring for PostAdmin"""
	list_display = ('title','author','timestamp',)
	search_fields = ('title',)

		
admin.site.register(BolgPost,PostAdmin)


