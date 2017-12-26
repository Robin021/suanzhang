from django import forms
#from django.contrib.admin import widgets

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码',widget=forms.PasswordInput)

class mingxiForm(forms.Form):
    riqi      = forms.DateTimeField(label='日期',widget=forms.DateTimeInput(attrs={'type': 'date'}))
    huozhu    = forms.CharField(label='货主')
    guonong   = forms.CharField(label='果农',error_messages={'required':u'果农姓名不能为空'})
    xiangshu  = forms.IntegerField(label='箱数')
    maozhong  = forms.IntegerField(label='毛重')
    jingzhong = forms.IntegerField(label='净重')
    danjia    = forms.IntegerField(label='单价')
    yingfu    = forms.IntegerField(label='应付')
    daishou   = forms.IntegerField(label='代收')
    tiaojia   = forms.IntegerField(label='调价')
    shifujine = forms.IntegerField(label='实付')
    beizhu    = forms.CharField(label='备注')

