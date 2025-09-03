
from blacklist.models import BlackList

def my_job():
    
    b = BlackList(ip="123456")
    b.save()