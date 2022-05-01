# How to build a dash app in Django with sqlite3?

## install python, install django
sudo pacman -S python
pip install django

## start project:
django-admin startproject agency

## start app:
django-admin startapp dash
settings.py >> installed apps >> put app name here;

## add database:
don't do anything for sqlite3

## make initial migration:
python manage.py migrate

## create the landing page:
### in dash/views:
from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'templates/index.html',)

### in agency/settings:
STATIC_ROOT =''
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join('static'),)

TEMPLATES DIRS: [BASE_DIR]

### in /static
Put Bootstrap files or written css, js files here.

### in /templates
Create index.html. Refer to css and js files as:
"{% static 'js/bootstrap.min.js' %}"

### in agency/urls:
from dash import views as dash_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns as statics
urlpatterns += path('', dash_views.index)
urlpatterns += statics()

##  create the dashboards:
### create the login templates:

#### in /templates:
Create login_zzz.html, register_zzz.html, password_reset.html.

#### in agency/urls:
urlpattern += path('login-zzz/', auth_views.as_view(template_name='templates/login-zzz.html'))

### create the dashboard templates
In the same way as above.

## create the Actor model:
### in dash/models:
class Actor(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT)
	bio = models.TextField(max_length=500, blank=True)
	birth_date = models.DateField(blank=True)

### in bash:
python manage.py makemigrations
python manage.py migrate


## To create user-side queries:
### In views:
if request.method == "POST":
    userName = request.POST.get("userName")
    customer = request.POST.get("customerId")
    orders = Order.objects.filter(customer=customer)
return render request with orders variable passed  

### In templates:
Create a form with hidden fields and only visible submission button:
<form action='/dash/orders/' method='post'>
{% csrf_token %}
<input type='hidden' name='customerId', value={{customer.pk}} />
<input type='hidden' name='userName', value='{{customer.companyName}}' />
<input type='submit' name='query', value='View' />
</form>
