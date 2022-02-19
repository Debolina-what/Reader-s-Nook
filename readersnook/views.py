
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages#connection sathi konti l mo
from .models import register1
from .models import Upload_Book
from .models import readersnook
from .models import Communication
from .models import feed
from .models import Book,Category
from django.forms.models import model_to_dict
# from django.contrib.auth import authenticate
# from django.contrib.auth.models import User,auth
from operator import itemgetter


from .models import Item
from .forms import currentBook

from .models import w_Item
from .forms import wantBook

from .models import Misc
from .forms import miscBook

from django.views import View
from .models import Post
from .forms import PostForm





# Create your views here.
#for CSS link
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'index.html')

def contact1(request):
    return render(request,'contact1.html')

def review(request):
    return render(request,'review.html')


def user(request):
    return render(request, 'user.html')



#just a sec
# def contact(request):
#     return render(request,'contact.html')#just a sec
# def shop(request):
#     return render(request,'Login.html')


#for registration database connection
# def OpenLogin(request):
#     return render(request, 'Sample.html')


def BookReaderLogin(request):
    if request.method == 'POST':
        print(request.POST["password"])
        try:
            temp=register1.objects.get(umail=request.POST["username"],upass=request.POST["password"])
            print(temp)
            return render(request, 'user.html')
        except register1.DoesNotExist as e:
            redirect('Login.html')
    else:
        return render(request, 'Login.html')

def LoginSuccess(request):
    return render(request, 'user.html')


# def login(request):
#         con=mysql.connector.connect(host='localhost',user='root',password='',database='newredersnook')
#         cursor=con.cursor()
#         con2 = mysql.connector.connect(host='localhost', user='root', password='', database='newredersnook')
#         cursor2 = con2.cursor()
#         sqlcommand = 'select umail from registration'
#         sqlcommand2 = 'select upass from registration'
#         cursor.execute(sqlcommand)
#         cursor2.execute(sqlcommand2)
#         e=[]
#         p=[]
#         for i in cursor:
#             e.append(i)
#         for j in cursor2:
#             p.append(j)
#         res=list(map(itemgetter(0),e))
#         res2 = list(map(itemgetter(0), p))
#
#         if request.method == 'POST':
#             umail=request.POST['umail']
#             upass=request.POST['upass']
#             i=1
#             k=len(res)
#             while i < k:
#                 if res[i]==umail and res2[i]==upass:
#                     return render(request,'index.html',{'umail':email})
#                     break
#                 i+=1
#             else:
#                 messages.info(request, "Invalid Credential")
#                 return render('Sample.html')




        #return redirect(request, 'index.html')
        #user=auth.authenticate(username=umail,password=upass)
        # if user is not None:
        #     auth.login(request,user)
        #     #messages.info(request,"Logged succesfull")
        #     return redirect(request,'index.html')
        # else:
        #     messages.info(request,"Invalid Credential")
        #     return redirect('Login.html')
    # else:
    #     messages.info(request, "Invalid Credential")
    #return render('Sample.html')

def Insertrecord(request):
    if request.method=='POST':
        if request.POST.get('uname') and request.POST.get('uphno') and request.POST.get('umail') and request.POST.get('upass') and request.POST.get('cpass'):
            saverecord=register1()#Registeration form kuthe a ?
            saverecord.uname=request.POST.get('uname')
            saverecord.uphno=request.POST.get('uphno')
            saverecord.umail=request.POST.get('umail')
            saverecord.upass=request.POST.get('upass')
            saverecord.cpass=request.POST.get('cpass')#run krun sang na error nakki kuthe generate hotot a
            saverecord.save()
            messages.success(request,'Registered Succuesfully....')
            return render(request,'Login.html')#me dileli zip extract keli ka ?
        elif request.POST.get('username') and request.POST.get('password'):
            try:
                temp = register1.objects.get(umail=request.POST["username"], upass=request.POST["password"])
                uobj = model_to_dict(temp)
                return render(request, 'user.html',uobj)
            except register1.DoesNotExist as e:
                return render(request, 'Login.html')


    else:
        return render(request,'Login.html')

def feedback(request):
    if request.method=='POST':
        if request.POST.get('umail') and request.POST.get('content'):
            saverecord=feed()#Registeration form kuthe a ?
            saverecord.umail=request.POST.get('umail')
            saverecord.content=request.POST.get('content')
            saverecord.save()
            messages.success(request,'Thank You For Feedback....')
            return render(request,'contact.html')
    else:
        return render(request,'contact.html')

def logout(request):
    if request.method=='POST':
        return render(request, 'index.html')

def profile1(request):
    # #umail=request.POST.get('umail')
    # umail1=register1.objects.filter(umail=request.POST.get('umail'))
    # print(umail1)
    uid = request.GET.get("uid")
    uname = request.GET.get("name")
    uphno = request.GET.get("uphno")
    umail = request.GET.get("umail")
    obj = {
        'uname' : uname,
        'uphno' : uphno,
        'umail' : umail,
        'uid' : uid
    }
    return render(request,'profile.html',obj)

def shop(request):
    uid = request.GET.get("uid")
    uname = request.GET.get("name")
    uphno = request.GET.get("uphno")
    umail = request.GET.get("umail")
    obj = {
        'uname': uname,
        'uphno': uphno,
        'umail': umail,
        'uid': uid
    }
    return render(request,'shop.html',obj)
def message(request):
    uid = request.GET.get("uid")
    uname = request.GET.get("name")
    uphno = request.GET.get("uphno")
    umail = request.GET.get("umail")
    obj = {
        'uname': uname,
        'uphno': uphno,
        'umail': umail,
        'uid': uid
    }
    return render(request,'message.html',obj)

def sell(request):
    return render(request,'sell.html')

def buy(request):
    return render(request,'buy.html')

def mypost(request):
    return render(request,'mypost.html')

def UploadBook(request):
    print(request.POST.get('op'))
    if request.POST.get('op') == "saveData" :
        print("inside Upload")
        if request.POST.get('fname') and request.POST.get('uname') and request.POST.get('umail') and request.POST.get('uid') and request.POST.get('bname') and request.POST.get('bprice') and request.POST.get('bimage'):
            saverecord=Upload_Book()#Registeration form kuthe a ?
            saverecord.fname=request.POST.get('fname')
            saverecord.uname=request.POST.get('uname')
            saverecord.umail=request.POST.get('umail')
            saverecord.uid=request.POST.get('uid')
            saverecord.bname=request.POST.get('bname')
            saverecord.bprice=request.POST.get('bprice')
            saverecord.bimage=request.POST.get('bimage')#run krun sang na error nakki kuthe generate hotot a
            saverecord.save()
            messages.success(request,'Book Succesfully Uploaded..')
            return render(request,'sell.html')
        else:
            return render(request,'user.html')
    else:
        return render(request, 'sell.html')
            # uid = request.GET.get("uid")
            # uname = request.GET.get("name")
            # uphno = request.GET.get("uphno")
            # umail = request.GET.get("umail")
            # obj = {
            #     'uname': uname,
            #     'uphno': uphno,
            #     'umail': umail,
            #     'uid': uid
            # }
            # return render(request, 'shop.html', obj)


def buybook(request):
    dests=Upload_Book.objects.all()
    print(dests)
    return render(request, 'buy.html',{'dests':dests} )

def mypost1(request):
    uid = request.GET.get("uid")
    uname = request.GET.get("name")
    uphno = request.GET.get("uphno")
    umail = request.GET.get("umail")
    obj = {
        'uname': uname,
        'uphno': uphno,
        'umail': umail,
        'uid': uid
    }
    print(obj)
    dests = Upload_Book.objects.filter(uid=uid)
    if obj['uid']==uid:
        print(dests)
        return render(request, 'mypost.html', {'dests': dests})

    #dest = Upload_Book.objects.filter(uid=uid)


def compose(request):
    uid = request.GET.get("uid")
    uname = request.GET.get("name")
    uphno = request.GET.get("uphno")
    umail = request.GET.get("umail")
    obj = {
        'uname': uname,
        'uphno': uphno,
        'umail': umail,
        'uid': uid
    }
    if request.method == 'POST':
        if request.POST.get('s_id') and request.POST.get('r_id') and request.POST.get('s_name') and request.POST.get('r_name') and request.POST.get('content'):
            saverecord=Communication()#Registeration form kuthe a ?
            saverecord.s_id=request.POST.get('s_id')
            saverecord.r_id=request.POST.get('r_id')
            saverecord.s_name=request.POST.get('s_name')
            saverecord.r_name=request.POST.get('r_name')
            saverecord.content=request.POST.get('content')
           #run krun sang na error nakki kuthe generate hotot a
            saverecord.save()
            messages.success(request,'Message Sent Succesfully..')
            return render(request,'compose_message.html',obj)
        else:
            return render(request,'user.html')
    else:
        return render(request, 'compose_message.html')


def inbox(request):
    uid = request.GET.get("uid")
    uname = request.GET.get("name")
    uphno = request.GET.get("uphno")
    umail = request.GET.get("umail")
    obj = {
        'uname': uname,
        'uphno': uphno,
        'umail': umail,
        'uid': uid
    }
    print(obj)
    dests = Communication.objects.filter(r_id=uid)
    if obj['uid'] == uid:
        print(dests)
    #return render(request, 'inbox.html',{'dests': dests},obj)
    return render(request, 'inbox.html', {'dests': dests,"obj":obj})


#Book Upload
def pdf(request):
    uid = request.GET.get("uid")
    uname = request.GET.get("name")
    uphno = request.GET.get("uphno")
    umail = request.GET.get("umail")
    recommended_books = Book.objects.filter(recommended_books=True)
    fiction_books = Book.objects.filter(fiction_books=True)
    business_books = Book.objects.filter(business_books=True)
    obj = {
        'uname': uname,
        'uphno': uphno,
        'umail': umail,
        'uid': uid,
        'recommended_books': recommended_books,
        'business_books': business_books,
        'fiction_books': fiction_books

    }
    print(obj)


    return render(request, 'home.html',obj)



def category_detail(request, slug):
    uid = request.GET.get("uid")
    uname = request.GET.get("name")
    uphno = request.GET.get("uphno")
    umail = request.GET.get("umail")
    category = Category.objects.get(slug = slug)
    obj = {
        'uname': uname,
        'uphno': uphno,
        'umail': umail,
        'uid': uid,
        'category': category}
    return render(request, 'genre_detail.html',obj)

def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    book_category = book.category.first()
    similar_books = Book.objects.filter(category__name__startswith=book_category)
    return render(request, 'book_detail.html', {'book': book, 'similar_books': similar_books})



#Journal part
def journal(request):
    uid = request.GET.get("uid")
    uname = request.GET.get("name")
    uphno = request.GET.get("uphno")
    umail = request.GET.get("umail")
    obj = {
        'uname': uname,
        'uphno': uphno,
        'umail': umail,
        'uid': uid
    }
    print(obj)
    return render(request, 'Journal.html', obj)

#current book list
def current(request):
    return render(request, 'current.html')

def current_book(request):
    if request.method == 'POST':
        fm = currentBook(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            author = fm.cleaned_data['author']
            genre = fm.cleaned_data['genre']
            description = fm.cleaned_data['description']
            day = fm.cleaned_data['day']
            reg = Item(name=name, author=author, genre=genre, description=description, day=day)
            reg.save()
            fm = currentBook()
    else:
        fm = currentBook()
    book = Item.objects.all()
    return render(request, 'current.html', {'form': fm, 'book': book})

# def current_Del(request):
#     return render(request, 'current_done.html')

def delete_book(request, id):
    if request.method == 'POST':
        print(id)
        db = Item.objects.get(id=id)
        db.delete()
        return render(request, 'current_done.html')
    else:
        return HttpResponse(str(id))


def pick(request, id):
    if request.method == 'POST':
        db = Item.objects.get(pk=id)
        db.delete()
        return render(request, 'want.html')

def edit_book(request, id):
    if request.method == 'POST':
        db = Item.objects.get(pk=id)
        fm = currentBook(request.POST, instance=db)
        if fm.is_valid():
            fm.save()
    else:
        db = Item.objects.get(pk=id)
        fm = currentBook(instance=db)
    return render(request, 'edit.html', {'form': fm})

#want to read
def want(request):
    return render(request,'want.html')

def want_book(request):
    if request.method == 'POST':
        fm = wantBook(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            author = fm.cleaned_data['author']
            genre = fm.cleaned_data['genre']
            description = fm.cleaned_data['description']
            reg = w_Item(name=name, author=author, genre=genre, description=description)
            reg.save()
            fm = wantBook()
    else:
        fm = wantBook()
    book = w_Item.objects.all()
    return render(request, 'want.html', {'form': fm, 'book': book})

def delete_wbook(request, id):
    if request.method == 'POST':
        print(id)
        db = w_Item.objects.get(id=id)
        db.delete()
        return render(request, 'pick.html')
    else:
        return HttpResponse(str(id))


def edit_wbook(request, id):
    if request.method == 'POST':
        print(id)
        db = w_Item.objects.get(pk=id)
        fm = wantBook(request.POST, instance=db)
        if fm.is_valid():
            fm.save()
    else:
        db = w_Item.objects.get(pk=id)
        fm = wantBook(instance=db)
    return render(request, 'w_edit.html', {'form': fm})



#miscelleneous
def misc(request):
    return render(request, 'misc.html')

def misc_book(request):
    if request.method == 'POST':
        fm = miscBook(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            author = fm.cleaned_data['author']
            genre = fm.cleaned_data['genre']
            description = fm.cleaned_data['description']
            reg = Misc(name=name, author=author, genre=genre, description=description)
            reg.save()
            fm = miscBook()
    else:
        fm = miscBook()
    boo = Misc.objects.all()
    return render(request, 'misc.html', {'form': fm, 'book': boo})

def delete_mbook(request, id):
    if request.method == 'POST':
        print(id)
        db = Misc.objects.get(id=id)
        db.delete()
        return render(request, 'pick1.html')
    else:
        return HttpResponse(str(id))


class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'suggetion.html', context)

    def post(self, request):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.uname = request.POST.get('uname')
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,
        }
        print('data saved')
        return HttpResponseRedirect('suggetion.html')#render(request, 'suggestion.html', context)


def more(request):
    return render(request,'more.html')