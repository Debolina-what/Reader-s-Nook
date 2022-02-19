from django.contrib import admin
from .models import register1
admin.site.register(register1)

from .models import feed
admin.site.register(feed)

from .models import Upload_Book
admin.site.register( Upload_Book)

from .models import Communication
admin.site.register( Communication)

from .models import Category, Book

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)

from .models import Item
admin.site.register(Item)


from .models import w_Item
admin.site.register(w_Item)


from .models import Misc
admin.site.register(Misc)

from .models import Post

admin.site.register(Post)

