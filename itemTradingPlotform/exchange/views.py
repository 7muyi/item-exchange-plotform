from django.shortcuts import render, HttpResponse, redirect
from .models import Requirement, User
from .forms import EditForm, UserForm, RegisterForm
from .utils.pagination import Pagination
from django.utils.timezone import now
import hashlib
import json
import requests
from math import radians, cos, sin, asin, sqrt 


# Create your views here.
def geocode(address):
    paramters = {'address': address, 'output': 'json'}
    base = 'http://api.map.baidu.com/geocoder'
    response = requests.get(base, params=paramters)
    answer = response.json()
    return answer['result']

def parsing(address):
    json_address = geocode(address)
    return json_address['location']['lng'], json_address['location']['lat']

def distance(address1, address2):
    lng1, lat1, lng2, lat2 = parsing(address1,address2)
    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2]) 
    # haversine公式 
    dlng = lng2 - lng1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlng/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # 地球平均半径，单位为公里 
    return c * r * 1000
    return c * r

def hash_code(s, salt='exchange'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

def register(request): 
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        message = ''
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            phone = register_form.cleaned_data['phone']
            address = register_form.cleaned_data['address']
            house_number = register_form.cleaned_data['house_number']
            
            if password1 != password2:
                message = '两次输入的密码不同'
            elif User.objects.filter(username=username).exists():
                    message = '用户已存在'
            elif User.objects.filter(phone=phone).exists():
                    message = '该手机已被注册'
            else:
                new_user = User.objects.create()
                new_user.username = username
                new_user.password = hash_code(password1)
                new_user.phone = phone
                new_user.address = address
                new_user.house_number = house_number
                new_user.save()
                
                request.session['is_login'] = True
                request.session['user_id'] = new_user.id
                request.session['user_name'] = new_user.username
                return redirect('/publish/')
        return render(request, 'register.html', locals())
    register_form = RegisterForm()                
    return render(request, 'register.html', locals())

def login(request):
    if request.session.get('is_login',None):
        user_id = request.session.get('user_id')
        return redirect('/publish/')

    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = ''
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    user.last_login = now
                    return redirect(f'/publish/')
                else:
                    message = '密码不正确'
            except:
                message = '用户不存在'
        return render(request,'login.html', locals())
    
    login_form = UserForm()
    return render(request, 'login.html', locals())

def logout(request):
    if not request.session.get('is_login',None):
        return redirect('/login/')
    
    request.session.flush()
    return redirect('/login/')

# 发布需求
def publish(request):
    nid = int(request.session.get('user_id'))
    if request.method == 'POST':
        emergency_degree = int(request.POST.get('urgency'))
        material_type = request.POST.get('material_type')
        body = request.POST.get('body')
        keywords = request.POST.get('keyword')

        if emergency_degree and material_type and body and keywords:
            user = User.objects.get(id=nid)
            new_requirements = Requirement.objects.create(
                pub_user=user, 
                emergency_degree=emergency_degree,
                material_type=material_type,
                body=body,
                keywords=keywords
            )
            # new_requirements.save()
            return redirect(f'/publish/me/')
        else:
            return render(request, 'publish.html', {'message':"请填写完整信息"})
    return render(request,'publish.html')

# 个人发布需求列表
def publish_me(request):
    nid = int(request.session.get('user_id'))
    requirements = Requirement.objects.filter(pub_user_id=nid).order_by('status','emergency_degree','-pub_time')
    page = Pagination(request,requirements)
    query_set = page.page_queryset
    page_html_string = page.html()
    emergency = [] 
    for data in query_set:
        emergency.append(data.emergency_degree)
    emergency = json.dumps(emergency)
    return render(request,'publish_me.html', locals()) 

# 需求列表
def receive_list(request):
    nid = request.session.get('user_id')
    # 判断以接收数量
    count = Requirement.objects.filter(rec_user=nid,status=2).count()
    
    address = User.objects.get(id=nid).address
    requirements = Requirement.objects.exclude(pub_user_id=nid).filter(status=1,pub_user__address=address).order_by('emergency_degree')
    page = Pagination(request,requirements)
    query_set = page.page_queryset
    page_html_string = page.html()
    emergency = [] 
    for data in query_set:
        emergency.append(data.emergency_degree)
    emergency = json.dumps(emergency)
    return render(request,'receive_list.html', locals())

# 个人接受需求列表
def receive_requirement(request, rid):
    nid = int(request.session.get('user_id'))
    requirement = Requirement.objects.get(id=rid)
    requirement.rec_time = str(now())
    requirement.rec_user_id = nid
    requirement.status = 2
    requirement.save()
    return redirect('/receive/list')

def concel_requirement(request, rid):
    Requirement.objects.get(id=rid).delete()
    return redirect('/publish/me')

def abandon_requirement(request, rid):
    requirement = Requirement.objects.get(id=rid)
    requirement.status = 1
    requirement.save()
    return redirect('/receive/me')

def finish_requirement(request,rid):
    requirement = Requirement.objects.get(id=rid)
    requirement.finish_time = str(now())
    requirement.status = 3
    requirement.save()
    return redirect('/publish/me')

# 接受需求
def receive_me(request):
    nid = int(request.session.get('user_id'))
    requirements = Requirement.objects.filter(rec_user_id=nid).exclude(status=1).order_by('status','emergency_degree','-pub_time')
    page = Pagination(request,requirements)
    query_set = page.page_queryset
    page_html_string = page.html()
    emergency = [] 
    for data in query_set:
        emergency.append(data.emergency_degree)
    emergency = json.dumps(emergency)
    return render(request,'receive_me.html', locals()) 

def info_edit(request):
    nid = int(request.session.get('user_id'))
    user = User.objects.get(id=nid)
    message = ''
    if request.method == 'POST':
        edit_form = EditForm(request.POST)
        if edit_form.is_valid():            
            username = request.POST.get('username')
            address = request.POST.get('address')
            house_number = request.POST.get('house_number')
            phone = request.POST.get('phone')
            if User.objects.filter(username=username).exists():
                message = '用户名重复'
            else: 
                user.username = username
                user.address = address
                user.house_number = house_number
                user.phone = phone
                user.save()
                message = '修改成功'
        else:
            message = '请按标准填写'
            return render(request, 'user_info.html', locals())
    return render(request, 'user_info.html', locals())

