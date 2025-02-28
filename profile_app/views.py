from django.shortcuts import render,redirect
from .forms import EditProfileImageForm,EditProfileNameForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import get_user_model,authenticate
from django.contrib.auth.decorators import login_required
from articles.models import Article
User = get_user_model()
# Create your views here.

@csrf_protect
def profile_view(request):
    errors = dict()
    form_avatar=""
    form_rename = ""
    articles = ""
    if  request.user.is_authenticated:
        #редактирование фото
        if 'photo_edit_button' in request.POST:
            form_avatar = EditProfileImageForm(request.POST,request.FILES,instance=request.user)
            if form_avatar.is_valid() and len(list(request.FILES))!=0:
                #Удаление старой аватарки
                user_uplodading = User.objects.get(id=request.user.id)
                user_uplodading.photo.delete(False)
                #сохранение фотки
                user_uplodading.photo = form_avatar.cleaned_data['new_photo']
                user_uplodading.save()
                return redirect('profile')
            else: errors['error_photo'] = "Пожалуйста, загрузите свою фотографию"
        else:
            form_avatar = EditProfileImageForm()
        #редактирование имени
        if "rename-button" in request.POST:
            form_rename = EditProfileNameForm(request.POST or None)
            if form_rename.is_valid():
                user = authenticate(username = request.user.username,password = form_rename.cleaned_data['password'])
                if user is not None:
                    new_username = form_rename.cleaned_data['new_username']
                    print(new_username)
                    try: User.objects.get(username=new_username)
                    except:
                        user.username = form_rename.cleaned_data['new_username']
                        user.save()
                        return redirect('profile')
                    else: errors['error_rename'] = "Пожалуйста, введите другое имя, это имя уже занято"
                else: errors['error_rename'] = "Пожалуйста, введите правильный пароль для изменения имени"
        else:
            form_rename = EditProfileNameForm()
        #записи пользователя
        articles = Article.objects.filter(autor=request.user)
    else:
        errors['if_not_aut'] ='Для просмотра своего профиля нужна регистрация!'
    context = {'form': form_avatar,
                'form_rename':form_rename,
                'errors':errors,
                'articles':articles}
    
        
    return render(request, 'profile_app/profile.html',context)