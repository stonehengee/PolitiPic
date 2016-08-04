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
import os
# import pprint
from django.conf import settings

# import pudb

class master(View):
    template='master.html'
    def get(self,request):
        return render(request, self.template, {})

class homepage(View):
    api = ApiCall()


    template='homepage.html'
    def get(self,request):
        context={'forms':UploadFileForm(),
                 'polcomp':"https://www.politicalcompass.org/analysis2",
        }
        return render(request,self.template, context)
    def post(self,request):

        # pu.db
        form = UploadFileForm(request.POST, request.FILES)
        # print (request.FILES['file'].values())
        # print (vars(request.FILES).keys())
        # print(request.FILES)
        if form.is_valid():

            img = request.FILES['file']
            self.api.picture=img.file
            self.api.run()
            api = self.api.graph()
            context={
                'econ':api[0],
                'social':api[1],
                'forms':UploadFileForm(),
                'polcomp':"https://www.politicalcompass.org/analysis2?ec=" + str(api[0]) + "&soc=" + str(api[1])
            }

        else:
            return self.get(request)
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
    resp = api.run()
    os.remove("imageToSave.png")
    # print (api)
    # api = api.graph()
    # print(api[0])
    # print(api[1])
    context={
        'econ':resp[0],
        'social':resp[1],
    }
    return JsonResponse(context)
        
# appcall()





# class score(View):
#     api = ApiCall()
#     template='homepage.html'
   
#     def post(self,request):
#         api.graph()
