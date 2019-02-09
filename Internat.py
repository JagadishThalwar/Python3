

from django.shortcuts import render
from django.utils.translation import ugettext

def homepage(request):
    """
    Shows the homepage with a welcome message that is translated in the
    user's language.
    """
    message = ugettext('Welcome to our site!')
    return render(request, 'homepage.html', {'message': message})
      

