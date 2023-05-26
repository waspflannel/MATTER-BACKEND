from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from PIL import Image
from django.urls import reverse
from django.template import loader
from .models import Image , Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User , auth
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreation , ImageForm
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.views.decorators.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import  ImageSerializer, CurrUserSerializer , ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from django.forms.models import model_to_dict
from django.core import serializers
from rest_framework.views import APIView 
from rest_framework import permissions
from django.utils.decorators import method_decorator
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from braces.views import CsrfExemptMixin

def homePage(request):
    return render(request, 'base.html', {})
    


class GetUsersView(APIView):
    permission_classes=(permissions.AllowAny,)

    def get(self,request,format=None):
        users = Profile.objects.all()
        users=ProfileSerializer(users,many=True)
        return Response(users.data)


class GetUserProfile(APIView):
    def get(self,request, format=None):
        user = self.request.user
        username = user.username
        print(user.id)
        user = User.objects.get(id=user.id)###
        user_profile = Profile.objects.get(user=user)
        user_profile = ProfileSerializer(user_profile)


        return Response({'profile': user_profile.data , 'username': str(username)})


class GetImageInfoView(APIView):
    def get(self , request, format = None):
        images = Image.objects.all()
        images = ImageSerializer(images , many=True)
        return Response(images.data)

class getImageInfo(APIView):
    def get(self,request,format=None):
        userReference = self.request.user
        userProfile = Profile.objects.get(user=userReference)
        userPosts = Image.objects.filter(user=userReference)
        userPosts = ImageSerializer(userPosts, many = True)
        return Response({'userPosts':userPosts.data})

#@method_decorator(csrf_protect , name="dispatch")


@method_decorator(ensure_csrf_cookie , name="dispatch")
class loginView(APIView):
    #authentication_classes=[]
    def post(self,request,format=None):
        if request.method == 'POST':
            name = request.POST.get('name')
            password = request.POST.get('password')
            user = authenticate(request, username=name, password=password)
            print(name , password)
            if user is not None:
                print("yes user")
                login(request, user)
                return redirect('/upload/')
                #return Response({'success':'logged in'})
            else:
                print("nouser")
                return redirect('login')
                #return Response({'Error':' not logged in'})

    def get(self,request,format=None):
        context = {}
        return render(request,'base.html',context)

        
@method_decorator(ensure_csrf_cookie , name="dispatch")
class registerView(APIView):
    def post(self,request,format=None):
        form = UserCreation
        if request.method == 'POST':
            name = request.POST['username']
            emailaddy = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            form = UserCreation(request.POST)
            if form.is_valid():
                if User.objects.filter(email=emailaddy).exists():
                    redirect('register')
                    return Response({'Error':' email already in use'})

                elif User.objects.filter(username=name).exists():
                    redirect('register')
                    return Response({'Error':' username already in use'})
                else:
                    form.save()
                    user_model = User.objects.get(username=name)
                    new_profile = Profile.objects.create(user=user_model,userId =user_model.id , username = name)
                    new_profile.save()
                    redirect('login')
                    return Response({'success':' account created'})

    def get(self,request,format=None):
        form = UserCreation
        context = {'form': form}
        return render(request, 'base.html', context)  # render must take a dict so put form in dictionarysasa


@method_decorator(ensure_csrf_cookie , name="dispatch")
class image_upload_view(APIView):
    def post(self,request,format=None):
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            print("here")
            if form.is_valid():
                print('hi')
                user = request.user.username
                image = request.FILES.get("image")
                title = request.POST.get('title')
                new_post = Image.objects.create(user=user, image=image, title=title, userWhoPosted = User.objects.get(username = user))
                new_post.save()
                posts = Image.objects.all()
                pfp = Profile.objects.all().values()
                print(pfp)
                render(request, 'base.html', {'form': form , 'posts':posts , 'user':user , 'image':image,'pfp':pfp})
                Response({'posted'})
                return redirect('upload')

    def get(self,request,format=None):
        form = ImageForm()
        posts = Image.objects.all()
        return render(request, 'base.html', {'form': form , 'posts':posts})

