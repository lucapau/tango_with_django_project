from django.contrib import admin
from rango.models import Category, Page



class PageAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'category', 'url')


admin.site.register(Page, PageAdmin)


# Add in this class to customize the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

# Update the registration to include this customized interface
admin.site.register(Category, CategoryAdmin)
