from django.contrib import admin
# import nested_admin
from blogging.models import Post, Category
# from django.db import models
# Register your models here.


# class CategoryInline(admin.StackedInline):
#     model = Category


# class PostAdmin(admin.ModelAdmin):
#     # pass
#     inlines = [
#         CategoryInline,
#     ]


# class CategoryAdmin(admin.ModelAdmin):
#     exclude = ('posts',)
#     # pass


admin.site.register(Post)#, PostAdmin)
admin.site.register(Category)#, CategoryAdmin)
