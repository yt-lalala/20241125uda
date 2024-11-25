from django.views.generic import View
from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import UploadForm, UploadFormUra
from .models import UploadImage, UploadImageUra
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import os
from django.conf import settings
from django.http import HttpResponse

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "app/index.html")

class Top(View):
    def get(self, request, *args, **kwargs):
        return render(request, "app/1_top.html")
    
def single(request):
    params = {
        'title': '画像のアップロード',
        'upload_form': UploadForm(),
    }
    print('shimadaproject views.py  def singleが実行されている')
    if (request.method == 'POST'):
        print('request.method == POSTがtrueである')
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            print('form.is_valid()がtrueである')
            images = request.FILES.getlist('images')
            for image in images:
                UploadImage.objects.create(image=image)
            return redirect('preview')
        else:
            print('form.is_valid()がfalseである')
            print(form.errors)  # フォームのエラーを出力する
            params['upload_form'] = form  # エラーメッセージを含めてフォームを再表示する
        return render(request, 'app/preview.html', {'upload_form': form})
            
            # print(upload_image)
            # for image in request.FILES.getlist('images'):
            #     UploadImage.objects.create(image=image)
            # return redirect('preview')  # 画像がアップロードされた後にリダイレクトするページを指定する

    return render(request, 'app/single.html', params)

def single_ura(request):
    params = {
        'title': '画像のアップロード',
        'upload_form_ura': UploadFormUra(),
        # 'id': None,
    }
    print('shimadaproject views.py  def single_uraが実行されている')
    if (request.method == 'POST'):
        print('request.method == POSTがtrueである')
        form = UploadFormUra(request.POST, request.FILES)
        if form.is_valid():
            print('form.is_valid()がtrueである')
            # upload_image = form.save()
            # print(upload_image)
            for image in request.FILES.getlist('images'):
                UploadImageUra.objects.create(image=image)
            return redirect('preview_ura')  # 画像がアップロードされた後にリダイレクトするページを指定する

    return render(request, 'app/single_ura.html', params)

def preview(request):
    image_folder = os.path.join(settings.MEDIA_ROOT, 'img')
    
     # ディレクトリの存在確認と作成
    if not os.path.exists(image_folder):
        try:
            os.makedirs(image_folder)
        except Exception as e:
            return HttpResponse(f'Error: Could not create directory {image_folder}: {e}', status=500)
    
    try:
        image_files = os.listdir(image_folder)
        image_paths = [os.path.join(settings.MEDIA_URL, 'img', filename) for filename in image_files if filename.endswith('.jpg') or filename.endswith('.png')]
        
        params = {
            'title': 'オモテ画像の表示',
            'image_paths': image_paths
        }

        print('image_paths:', image_paths)
        print('Function-Based View shimadaproject views.py def preview2が実行されている')

        return render(request, 'app/preview.html', params)
    
    except FileNotFoundError as e:
        return HttpResponse(f'Error: {e}', status=404)

def preview_ura(request):
    image_folder = os.path.join(settings.MEDIA_ROOT, 'img_ura')
    
     # ディレクトリの存在確認と作成
    if not os.path.exists(image_folder):
        try:
            os.makedirs(image_folder)
        except Exception as e:
            return HttpResponse(f'Error: Could not create directory {image_folder}: {e}', status=500)
    
    try:
        image_files = os.listdir(image_folder)
        image_paths = [os.path.join(settings.MEDIA_URL, 'img', filename) for filename in image_files if filename.endswith('.jpg') or filename.endswith('.png')]
        
        params = {
            'title': 'ウラ画像の表示',
            'image_paths': image_paths
        }

        print('image_paths:', image_paths)
        print('Function-Based View shimadaproject views.py def preview2が実行されている')

        return render(request, 'app/preview_ura.html', params)
    
    except FileNotFoundError as e:
        return HttpResponse(f'Error: {e}', status=404)
    
class Aicall(TemplateView):
    print('Class-Based View shimadaproject views.py call Aicallが呼び出されている')
    template_name = 'app/7_graph.html'
    def get(self, request, *args, **kwargs):
        
        print('AI CALL before')
        
        # os.system('python3 ./AI/predict.py')
        
        print('AI CALL complete')
        
        return super().get(request, *args, **kwargs)

def analysis(request):

    print('def analysisが実行されている')
    return render(request, 'app/analysis.html')
