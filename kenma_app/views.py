from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage
from .forms import ContactForm
import textwrap

class IndexViews(View):
  def get(self, request, *args, **kwargs):   
    return render(request, 'kenma_app/index.html')  

class CompanyViews(View):
  def get(self, request, *args, **kwargs):   
    return render(request, 'kenma_app/company.html')  

class ServiceViews(View):
  def get(self, request, *args, **kwargs):   
    return render(request, 'kenma_app/service.html')  

class SaikenmaViews(View):
  def get(self, request, *args, **kwargs):   
    return render(request, 'kenma_app/saikenma.html')  

class SaidankiViews(View):
  def get(self, request, *args, **kwargs):   
    return render(request, 'kenma_app/saidanki.html')  

class SinbaViews(View):
  def get(self, request, *args, **kwargs):   
    return render(request, 'kenma_app/sinba.html')  

class SizaiViews(View):
  def get(self, request, *args, **kwargs):   
    return render(request, 'kenma_app/sizai.html')  

class ContactView(View):
   def get(self, request, *args, **kwargs):
      form = ContactForm(request.POST or None)
      return render(request, 'kenma_app/contact.html', {'form': form})

   def post(self, request, *args, **kwargs):
      form = ContactForm(request.POST or None)
      if form.is_valid():
          name = form.cleaned_data['name']
          message = form.cleaned_data['message']
          select = form.cleaned_data['select']
          email = form.cleaned_data['email']
          subject = 'お問い合わせありがとうございます。'
          contact = textwrap.dedent('''
             ※このメールはシステムからの自動返信です。

             {name} 様
            
             お問い合わせありがとうございました。
             以下の内容でお問い合わせを受け付けました。
             内容を確認させていただき、ご返信させていただきますので、少々お待ちください。

             ----------------------------------

             ・お名前
             {name}

             ・メールアドレス
             {email}

             ・タイトル
             {select}

             ・メッセージ
             {message}
             -----------------------------------
             株式会社　長町研磨
             〒700-0943
             岡山県岡山市南区新福1-14-4
             TEL 086-26-4-4111
             営業時間 8:15~17:00（月~金）
             WEB: https://www.nagamachi-kenma.com/
          ''').format(
             name=name,
             email=email,
             select=select,
             message=message
          )
          to_list = [email]
          bcc_list = [settings.EMAIL_HOST_USER]

          try:
             message = EmailMessage(subject=subject, body=contact, to=to_list,bcc=bcc_list)
             message.send()
          except BadHeaderError:
             return HttpResponse('無効なヘッダが検出されました。')
          return redirect('kenma_app:done')

      return render(request, 'kenma_app/contact.html',
                   {'form': form})       


class DoneViews(View):
  def get(self, request, *args, **kwargs):   
    return render(request, 'kenma_app/done.html')  
