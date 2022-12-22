from django import forms
from captcha.fields import CaptchaField
from django.core.validators import RegexValidator
from .models import User


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    captha = CaptchaField(label='验证码')

class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label="地址", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    house_number = forms.CharField(label="门牌号", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="联系方式", validators=[RegexValidator(r'^1[3-9]\d{9}$','手机号格式错误')], widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", min_length=6, max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class EditForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control di'}))
    address = forms.CharField(label="地址", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control di'}))
    house_number = forms.CharField(label="门牌号", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control di'}))
    phone = forms.CharField(label="联系方式", validators=[RegexValidator(r'^1[3-9]\d{9}$','手机号格式错误')], widget=forms.TextInput(attrs={'class': 'form-control di'}))
# class PublishForm(forms.Form):
#     emergency_degree_choice = (
#         ('1','URGENCY'),
#         ('2','NORM'),
#         ('3','LOOSENESS')
#     )
#     material_type_choice = (
#         ('m','医疗物资'),
#         ('f','食物'),
#         ('d','生活用品')
#     )
#     emergency_degreee = forms.ChoiceField(label='紧急程度', choices=emergency_degree_choice)
#     material_type = forms.ChoiceField(label='物品种类', choices=material_type_choice)
#     body = forms.CharField(label='需求信息',max_length=)
# class LoginForm(AuthenticationForm):
#     def __init__(self,*args,**kwargs):
#         super(LoginForm,self).__init__(*args,**kwargs)
#         self.fields['username'].widget = widgets.TextInput(
#             attrs={'placeholder': "username", "class": "form-control"}
#         )
#         self.fields['password'].widget = widgets.PasswordInput(
#             attrs={'placeholder': "password", "class": "form-control"}
#         )

# class RegisterForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(RegisterForm,self).__init__(*args, **kwargs)
        
#         self.fields['username'].widget = widgets.TextInput(
#              attrs={'placeholder': "username", "class": "form-control"}
#         )
#         self.fields['password1'].widget = widgets.PasswordInput(
#             attrs={'placeholder': "password", "class": "form-control"}
#         )
#         self.fields['password2'].widget = widgets.PasswordInput(
#             attrs={'placeholder': "repeat password", "class": "form-control"}
#         )
#         self.fields['phone'].widget = widgets.TextInput(
#             attrs={'placeholder': "phone", "class": "form-control"}
#         )

#     def clean_phone(self):
#         phone = self.cleaned_data['phone']
#         if get_user_model().objects.filter(phone=phone).exists():
#             raise ValidationError('该联系方式已被注册')
#         return phone

#     class Meta:
#         model = get_user_model()
#         fields = ('username','phone')