from django.conf.urls import url, include
from django.contrib import admin
from registration.forms import RegistrationFormUniqueEmail
from registration.views import RegistrationView
from example.views import thnks, localForm

urlpatterns = [    
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.urls')),
    url(r'^register/$', RegistrationView.register, {'form': RegistrationFormUniqueEmail}, name='registration_register'),
    url('', include('registration.urls')),    
    url(r'^', include('example.urls')),
    url(r'^feedback/$', localForm),
    url(r'^about/', include('about.urls')),
    url(r'^', include('product.urls')),
    url(r'^', include('order.urls')),
]
