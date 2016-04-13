from django.http import HttpResponseRedirect, JsonResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.views.generic import View
from django.shortcuts import render, redirect
from faces.forms import UploadFileForm
from faces.master import ApiCall
import base64
# import PIL
import io
# import pprint
from django.conf import settings

# import pudb

class homepage(View):
    api = ApiCall()


    template='homepage.html'
    def get(self,request):
        context={'forms':UploadFileForm()}
        return render(request,self.template, context)
    def post(self,request):

        # pu.db
        form = UploadFileForm(request.POST, request.FILES)
        # print (request.FILES['file'].values())
        # print (vars(request.FILES).keys())
        print(request.FILES)
        if form.is_valid():

            img = request.FILES['file']
            self.api.picture=img.file
            self.api.run()
            api = self.api.graph()
            context={
                'econ':api[0],
                'social':api[1],
                'forms':UploadFileForm(),
            }

        else:
            print('bad news is bad')

        return render(request, self.template, context)

def appcall(request):
    api = ApiCall()
    imgData = ""

    f = request.body
    f= str(f)
    f=f[8:-2]
    # print(f[:10])
    # for line in f:
        # print(line)
    f = f.replace('%0A', '\n')
    f = f.replace('-', '+')
    f = f.replace('_', '/')
    f = f.replace('%3D', '=')
        # imgData += line
    # print(f)
    # imgData += f
    # print(imgData)

    fh = open("imageToSave.png", "wb")
    fh.write(base64.b64decode(f))
    fh.close()
    fh = open('imageToSave.png', 'rb')
    api.picture=fh
    api.run()
    api = api.graph()
    print(api[0])
    print(api[1])
    context={
        'econ':api[0],
        'social':api[1],
    }
    return JsonResponse(context)
        
# appcall()



class master(View):
    template='master.html'
    def get(self,request):
        return render(request, self.template, {})

class score(View):
    template='homepage.html'
    def post(self,request):
        api.graph()
'''
ssh projects@byteprojects.co -p 13022
sudo su
ssource env...
python3 manage.py collectstatic
service apache2 restart
tail /var/log/apache2/error.log
password: tomiscool
passwd - change password
scp -P 13022 projects@byteprojects.co:/var/www/jng_phase3_final/django/faces/imageToSave.png ~/Desktop/saved.png
'''