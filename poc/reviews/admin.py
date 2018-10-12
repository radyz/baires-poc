from django.contrib import admin

from reviews.models import Review, Company


admin.site.register(Review)
admin.site.register(Company)
