from django.conf import settings

def env_settings(request):

    
    return {
        'HOME_PAGE': settings.HOME_PAGE,  
    }