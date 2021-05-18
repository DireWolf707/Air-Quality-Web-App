from django.shortcuts import render
from django.views.generic import TemplateView

def HomeView(request,):
    import json
    import requests
    try:
        api_req = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=E123B51F-9F55-4F10-A490-28AEA4ABC73C')
        data = json.loads(api_req.content)
    except:
        data = None
    
    return render(request,'home.html',{'data':data})
    
class AboutView(TemplateView):
    template_name = 'about.html'
