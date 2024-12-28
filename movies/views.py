from django.shortcuts import render
from . models import Movieinfo,Censorinfo,Actor
from . forms import Movieform
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login/')
def list(request):
    #session
    count=request.session.get('count',0)
    count=int(count)
    count=count+1
    request.session['count']=count

   
    #cookies
    visits=int(request.COOKIES.get('visits',0))
    visits=visits+1
    # movie_data=Movieinfo.objects.filter().order_by('-year')
    # movie_data=Movieinfo.objects.filter(actors__name='lal',year__gt=2000).order_by('-year')
    movie_data=Movieinfo.objects.all()

    #session get
    recent_visits=request.session.get('recent_visits',[])
    rexent_movies_set=Movieinfo.objects.filter(pk__in=recent_visits)


    # exclude (to exclude the datas of condition)
    
    response=render(request,'list.html',{'movies':movie_data,'visits':visits,'count':count,'rexent_movies_set':rexent_movies_set})
    response.set_cookie('visits',visits)
    return response

def create(request):
   
    if request.POST:
        frm=Movieform(request.POST,request.FILES)
        if frm.is_valid:
           frm.save()
    else:
        frm=Movieform()
     
         
      


        # print(request.POST.get('title'))
     



    return render(request,'create.html',{'frm':frm})

def edit(request,pk):
    

    instance=Movieinfo.objects.get(pk=pk)
    if request.POST and request.FILES:
        # title=request.POST.get('title')
        # year=request.POST.get('year')

        # description=request.POST.get('description')
        # instance.title=title
        # instance.year=year
        # instance.description=description
        # instance.save()
        frm=Movieform(request.POST,request.FILES,instance=instance)
        if frm.is_valid:
            frm.save()

    #sesssion to store recent_visited primary keys        
    else:
        recent_visits=request.session.get('recent_visits',[])
        recent_visits.insert(0,pk)
        request.session['recent_visits']=recent_visits
        
    frm=Movieform(instance=instance)


    return render(request,'create.html',{'frm':frm})

def delete(request,pk):
    instance=Movieinfo.objects.get(pk=pk)
    instance.delete()
    return render(request,'list.html')


