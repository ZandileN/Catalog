from django.contrib import admin

# Register your models here.
from .models import Author, Genre, book, bookinstance

#admin.site.register(book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(bookinstance)

#Define the admin class 
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

#Register the admin class with the associated models
admin.site.register(Author, AuthorAdmin)

#Register the Aadmin classes for Book using the decorator
class BookInstanceInline(admin.TabularInline):
    model= bookinstance
@admin.register(book)
class BookAdmin (admin.ModelAdmin):
        list_display = ('title', 'author', 'display_genre')
        inlines = [BookInstanceInline]

#Register the Admin classesd for bookinstance using the decorator
@admin.register(bookinstance)
class bookinstanceAdmin(admin.ModelAdmin):
   list_filter = ('status', 'due_back')
   fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


