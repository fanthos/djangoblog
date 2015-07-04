from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget
from django.db import models
import markdown_deux
from aboutme.models import *

from markdown_deux.conf.settings import MARKDOWN_DEUX_STYLES
from markdown_deux.conf import settings
MARKDOWN_DEUX_STYLES.update ({
    "trusted": {
        "extras": {
            "code-friendly": None,
        },
        # Allow raw HTML (WARNING: don't use this for user-generated
        # Markdown for your site!).
        "safe_mode": False,
    },
})
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
		obj.text_html = markdown_deux.markdown(obj.text, "trusted")
		obj.save()

admin.site.register(Pages, PagesAdmin)