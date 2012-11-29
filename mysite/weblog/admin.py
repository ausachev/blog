from django.contrib import admin
from mysite.weblog.models import BolgPost,Category


class PostAdmin(admin.ModelAdmin):
	"""docstring for PostAdmin"""
	list_display = ('title','author','timestamp','status')
	search_fields = ('title',)

		
admin.site.register(BolgPost,PostAdmin)
admin.site.register(Category)

