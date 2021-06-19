"""miac_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from monitoring_system.views import PatientView, PatientListView, PatientMeasurementsView, DoctorAuthView, \
    DoctorRegistryView, PatientAuthView, DoctorView, MedicinehView, PrivatePatientListView, PrivatePatientView, \
    SearchPatientView, PrescriptionView

urlpatterns = [
    path('api/doctors/<uid>/', DoctorView.as_view()),
    path('api/patients/auth/', PatientAuthView.as_view()),
    path('api/patients/<uid>/', PatientView.as_view()),
    path('api/patients/', PatientListView.as_view()),
    path('api/patients/<term>/', SearchPatientView.as_view()),
    path('api/patients/private', PrivatePatientListView.as_view()),
    path('api/patients/private/<uid>/', PrivatePatientView.as_view()),
    path('api/measurements/<uid>/', PatientMeasurementsView.as_view()),
    path('admin/', admin.site.urls),
    path('api/registry/', DoctorRegistryView.as_view()),
    path('api/auth/', DoctorAuthView.as_view()),
    path('api/<uid>/medicine/', MedicinehView.as_view()),
    path('api/<uid>/prescription/', PrescriptionView.as_view()),
]
