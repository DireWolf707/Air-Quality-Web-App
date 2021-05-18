from django.shortcuts import render

def HomeView(request):
    if request.method == "POST":
        import json
        import requests
        zipcode = request.POST['zipcode']
        try:
            api_req = requests.get(f'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=25&API_KEY=E123B51F-9F55-4F10-A490-28AEA4ABC73C')
            data = json.loads(api_req.content)
        except:
            data = None
        
        return render(request,'home.html',{'data':data})
    return render(request,'about.html')
    
