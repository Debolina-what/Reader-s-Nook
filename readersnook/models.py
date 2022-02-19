from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class register1(models.Model):
    uid=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    uname=models.CharField(max_length=255)
    uphno=models.CharField(max_length=255)
    umail=models.CharField(max_length=255)
    upass=models.CharField(max_length=255)
    cpass=models.CharField(max_length=255)
    class Meta:
        db_table='registration'

class feed(models.Model):
    fid=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    umail=models.CharField(max_length=255)
    content=models.CharField(max_length=255)
    class Meta:
        db_table='feedback'

class Upload_Book(models.Model):
    b_id=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    fname=models.CharField(max_length=255)
    uname=models.CharField(max_length=255)
    umail=models.CharField(max_length=255)
    uid=models.CharField(max_length=255)
    bname=models.CharField(max_length=255)
    bprice = models.CharField(max_length=255)
    bimage = models.ImageField(upload_to='img', blank=True, null=True)
    class Meta:
        db_table='sell'
class Communication(models.Model):
    id=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    s_id=models.IntegerField()
    r_id=models.IntegerField()
    s_name=models.CharField(max_length=255)
    r_name=models.CharField(max_length=255)
    content=models.CharField(max_length=255)

    class Meta:
        db_table='communication'

# for book


class Category(models.Model):
    name = models.CharField('Categories', max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    cover_image = models.ImageField(upload_to='img', blank=True, null=True)
    author = models.CharField(max_length=50)
    summary = models.TextField()
    category = models.ManyToManyField(Category, related_name='books')
    pdf = models.FileField(upload_to='pdf')
    recommended_books = models.BooleanField(default=False)
    fiction_books = models.BooleanField(default=False)
    business_books = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class BookSearch(models.Model):
    name_of_book = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_book



#for Journal

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Item(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.TextField(max_length=50)
    author = models.TextField(max_length=50)
    genre = models.TextField(max_length=30)
    description = models.TextField(max_length=200, null=True)
    day = models.TextField(max_length=30)
    # image = models.ImageField(upload_to="img", null=True, blank=True)

    class Meta:
        db_table = 'item'


class w_Item(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.TextField(max_length=50)
    author = models.TextField(max_length=50)
    genre = models.TextField(max_length=30)
    description = models.TextField(max_length=200, null=True)
    # image = models.ImageField(upload_to="img", null=True, blank=True)

    class Meta:
        db_table = 'w_item'


class Misc(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.TextField(max_length=50)
    author = models.TextField(max_length=50)
    genre = models.TextField(max_length=30)
    description = models.TextField(max_length=200, null=True)

    class Meta:
        db_table = 'misc'


class readersnook(models.Model):
    uname=models.CharField(max_length=255)
    uphno=models.IntegerField()


#Suggetion Wall

class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    uname= models.TextField(max_length=50,null=True)

    def __str__(self):
        return self.body


