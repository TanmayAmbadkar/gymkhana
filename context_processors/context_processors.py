from clubs.models import Club
from committees.models import Committee
from festivals.models import Festival

def get_clubs(request):

    clubs = Club.objects.all()
    return {"clubs": clubs}

def get_committees(request):
    committees = Committee.objects.all()
    return {"committees": committees}

def get_fests(request):
    fests = Festival.objects.all()
    return {"fests": fests}
