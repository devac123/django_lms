from django.shortcuts import render
import base64

# Create your views here.
def image2base64(request):
    if request.method == 'POST':
        img_file = request.FILES['image']
        image_binary = img_file.read()    # Read the file content
        image_base64 = base64.b64encode(image_binary).decode('utf-8')
        return render(request, 'services/image2base64.html', {'base64_image': image_base64})
    return render(request, 'services/image2base64.html')