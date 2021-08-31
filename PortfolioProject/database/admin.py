from django.contrib import admin
from database.models import Testimonial

# @admin.register(Testimonial)
# class TestimonialAdmin(admin.ModelAdmin):
#     list_display=('name','address','ocupation')
#     class Meta:
#         model=Testimonial

class TestimonialAdmin(admin.ModelAdmin):
    list_display=('name','address','ocupation')
    search_fields=('name',)
    

admin.site.register(Testimonial,TestimonialAdmin)

