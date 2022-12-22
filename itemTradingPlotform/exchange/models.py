from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(verbose_name='手机号', max_length=11, unique=True, null=True) 
    avater = models.ImageField(verbose_name='头像', null=True, upload_to='img/')
    address = models.CharField(verbose_name='地址', max_length=50)
    house_number = models.CharField(verbose_name='门牌号', max_length=30)

    class Meta:
        db_table = 'user'
    
    def __str__(self):
        return self.username

class Requirement(models.Model):
    class EmergencyDegree(models.IntegerChoices):
        URGENCY = 1
        NORM = 2 
        LOOSENESS = 3
    
    class MaterialType(models.TextChoices):
        MEDICALSUPPLIES = '医疗物资'
        FOODS = '食物'
        DAILYNECESSITIES = '生活用品'
        OTHERS = '其他'

    class STATUS(models.IntegerChoices):
        UNRECEIVED = 1
        RECEIVED = 2
        FINISH = 3

    pub_user = models.ForeignKey(verbose_name='发布用户', related_name='pub_user', to='User',to_field='id',on_delete=models.CASCADE)    
    rec_user = models.ForeignKey(verbose_name='接收用户', related_name='rec_user', to='User',to_field='id',on_delete=models.CASCADE,null=True,blank=True)

    emergency_degree = models.SmallIntegerField(verbose_name='紧急程度',choices=EmergencyDegree.choices,default=3)
    material_type = models.CharField(verbose_name='物品种类',max_length=8,choices=MaterialType.choices,default='d')
    
    body = models.CharField(verbose_name='需求信息',max_length=100)
    keywords = models.CharField(verbose_name='关键字',max_length=50)
    
    pub_time = models.DateTimeField(verbose_name='发布时间',blank=False,default=now)
    rec_time = models.DateTimeField(verbose_name='接收时间',null=True,blank=True)
    finish_time = models.DateTimeField(verbose_name='完成时间',null=True,blank=True)

    status = models.SmallIntegerField(verbose_name='状态',choices=STATUS.choices,default=1)    

    def __str__(self):
        return self.keywords

# class Receive(models.Model):
#     user_id = models.ForeignKey(to='User',to_field='id',on_delete=models.CASCADE)
#     requirement_id = models.ForeignKey(to='Requirement',to_field='id',on_delete=models.CASCADE)
#     publish_time = models.DateTimeField(verbose_name='领取时间',default=now)    
#     finish_time = models.DateTimeField(verbose_name='完成时间',null=True,blank=True)

# class Person(models.Model):
#     name = models.CharField(verbose_name='姓名',max_length=5)