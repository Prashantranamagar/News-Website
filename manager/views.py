from django.shortcuts import render, get_object_or_404, redirect
from .models import Manager
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

# Create your views here.


def manager_list(request):

     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    
    manager = Manager.objects.all().exclude(utxt="admin")

    return render(request, 'back/manager_list.html', {'manager':manager})


def manager_del(request,pk):

     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})

    manager = Manager.objects.get(pk=pk)
    b = User.objects.filter(username=manager.utxt)
    b.delete()

    manager.delete()



    return redirect('manager_list')


def manager_group(request):

     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    
    group = Group.objects.all().exclude(name="masteruser")

    return render(request, 'back/manager_group.html', {'group':group})



def manager_group_add(request):

     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})

    if request.method == 'POST' :

        name = request.POST.get('name')

        if name != "" :

            if len(Group.objects.filter(name=name)) == 0 :

                group = Group(name=name)
                group.save()
    
    

    return redirect('manager_group')


def manager_group_del(request, name):

     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    
    b = Group.objects.filter(name=name)
    b.delete()

    return redirect('manager_group')


def users_groups(request,pk):

     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})

    manager = Manager.objects.get(pk=pk)

    user = User.objects.get(username=manager.utxt)

    ugroup = []
    for i in user.groups.all():
        ugroup.append(i.name)
    
    group = Group.objects.all()

    return render(request, 'back/users_groups.html', {'ugroup':ugroup, 'group':group, 'pk':pk})


def add_users_to_groups(request,pk):

     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})

    if request.method == 'POST' :

        gname = request.POST.get('gname')

        group = Group.objects.get(name=gname)
        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.utxt)
        user.groups.add(group)
    
    

    return redirect('users_groups' , pk=pk)


def del_users_to_groups(request,pk,name):


     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end



    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    

    group = Group.objects.get(name=name)
    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.utxt)
    user.groups.remove(group)
    
    

    return redirect('users_groups' , pk=pk)


def manager_perms(request):
    
     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    
    perms = Permission.objects.all()

    return render(request, 'back/manager_perms.html', {'perms':perms})


def manager_perms_del(request,name):
    
     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    
    perms = Permission.objects.filter(name=name)
    perms.delete()

    return redirect('manager_perms')


def manager_perms_add(request):
    
     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    
    
    if request.method == 'POST':

        name = request.POST.get('name')
        cname = request.POST.get('cname')

        if len(Permission.objects.filter(codename=cname)) == 0 :

            content_type = ContentType.objects.get(app_label='main', model='main')
            permission = Permission.objects.create(codename=cname, name=name, content_type=content_type)

        else:
            error = "This Codename Used Before"
            return render(request, 'back/error.html' , {'error':error})

    return redirect('manager_perms')


def users_perms(request,pk):
    
     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})

    manager = Manager.objects.get(pk=pk)

    user = User.objects.get(username=manager.utxt)

    permission = Permission.objects.filter(user=user)

    uperms = []
    for i in permission:
        uperms.append(i.name)
    
    perms = Permission.objects.all()

    return render(request, 'back/users_perms.html', {'uperms':uperms, 'pk':pk, 'perms':perms})


def users_perms_del(request,pk,name):
    
     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})



    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.utxt)

    permission = Permission.objects.get(name=name)
    user.user_permissions.remove(permission)

    return redirect('users_perms' , pk=pk)


def users_perms_add(request,pk):
    
     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})


    if request.method == 'POST' :

        pname = request.POST.get('pname')

        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.utxt)

        permission = Permission.objects.get(name=pname)
        user.user_permissions.add(permission)

    return redirect('users_perms' , pk=pk)


def groups_perms(request,name):
    
     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})

    group = Group.objects.get(name=name)
    perms = group.permissions.all()

    allperms = Permission.objects.all()

    return render(request, 'back/groups_perms.html', {'perms':perms, 'name':name, 'allperms':allperms})


def groups_perms_del(request,gname,name):
    
     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})

    group = Group.objects.get(name=gname)
    perm = Permission.objects.get(name=name)

    group.permissions.remove(perm)

    return redirect('groups_perms', name=gname)


def groups_perms_add(request,name):
    
     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})


    if request.method == 'POST' :

        pname = request.POST.get('pname')

        group = Group.objects.get(name=name)
        perm = Permission.objects.get(name=pname)

        group.permissions.add(perm)

    return redirect('groups_perms', name=name)