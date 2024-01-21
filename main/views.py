from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic 
from .models import *
from .forms import ContactUsForm
from django.core.mail import send_mail
from core.settings import EMAIL_HOST_USER

# Create your views here.
class HomeListView(generic.ListView):
    template_name = 'index.html'

    @staticmethod
    def __extract_all_data():
        design = Design.objects.all()
        logo = Logo.objects.get()
        about = AboutTeam.objects.all()
        gallery = GalleryOne.objects.get()
        secondgallery = SecondGallery.objects.get()
        thirdgallery = ThirdGallery.objects.get()  
        contacttext = ContactText.objects.all()
        

        context = {
            'design': design,
            'logo': logo,
            'about': about,
            'gallery': gallery,
            'secondgallery': secondgallery,
            'thirdgallery': thirdgallery,
            'contacttext': contacttext,
           
        }

        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        context = self.__extract_all_data()

    
        return render(request, self.template_name, context = context)
    

    def post(self,request):
        context = self.__extract_all_data()
        form = ContactUsForm(request.POST)


        if form.is_valid():
            email = request.POST['email']
            send_mail(
                subject= 'Shop FeedBack',
                message= 'Thanks For Review',
                from_email= EMAIL_HOST_USER,
                recipient_list= [email],
                fail_silently=False,
            )

            form.save()
        else:
            form = ContactUsForm()

        context.update({'form':form})

        return render(request, self.template_name, context= context)


