from django.shortcuts import render
from time import gmtime, strftime
from datetime import datetime
from pytz import timezone
# Create your views here.
def index(request):
     fmt = "%Y-%m-%d %H:%M:%S %Z%z"
     now_utc = datetime.now(timezone('UTC'))
     now_pacific = now_utc.astimezone(timezone('US/Pacific'))
     context = {
          'time': now_pacific.strftime(fmt)
     }

     return render(request, 'index.html', context)
