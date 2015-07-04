from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget
from django.db import models
import markdown_deux
from aboutme.models import *

# Register your models here.
class PagesAdmin(admin.ModelAdmin):
	fieldsets = (
		('Title', {'fields': ('title','uri',)}),
		('Text', {'fields': ('text','text_html', )}),
	)
	readonly_fields=('text_html',)
	list_display = ('title', 'uri',)

	formfield_overrides = {
		models.TextField: {'widget': AdminPagedownWidget },
	}
	def save_model(self, request, obj, form, change):
		obj.text_html = markdown_deux.markdown(obj.text)
		obj.save()

admin.site.register(Pages, PagesAdmin)