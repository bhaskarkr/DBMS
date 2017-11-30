from django.shortcuts import render,HttpResponse,redirect
from .forms import addcomment
import datetime
from .models import directors,actors,movies,movie_cast,rating,comments
import time
from django.db import connection
# Create your views here.
def index(request):
    all_movies = movies.objects.all().order_by('title')
    now = datetime.datetime.now().date()
    showing=movies.objects.filter(year__lte=now).order_by('year').reverse()
    upcoming = movies.objects.filter(year__gt=now).order_by('year')
    context = {'all_movies': all_movies[0:4],'upcoming':upcoming[0:3],'showing':showing[0:3]}
    query = request.GET.get('q')
    if query:
        #filtre = request.GET.get('filtr')
        movie =movies.objects.filter(title__icontains = query)
        director =directors.objects.filter(name__icontains = query)
        actor = actors.objects.filter(name__icontains = query)
        return render(request,'MOVIE_REVIEW/search.html',{'movie':movie,'director':director,'actor':actor})
        #if filtre == "Director":
        #    direct = directors.objects.get(name=query)
         #   movie =movies.objects.filter(director=direct.id)
          #  if direct:
           #     return render(request, 'MOVIE_REVIEW/directo.html',{'direct': direct,'movie':movie})
            #else:
             #   return render(request,'MOVIE_REVIEW/base.html')
       # elif filtre == "Movie Name":
        #    movie =movies.objects.filter(title__contains = query)
         #   print(movie)
          #  def search(request):
           #     return render(request, 'MOVIE_REVIEW/search.html', {'movie':movie})
            #cursor = connection.cursor()
            #find = movies.objects.raw('SELECT * from MOVIE_REVIEW_movies WHERE title LIKE %s',[query])
            #movie = cursor.execute(find)
            #print (movie)
            #for movie in cursor.fetchall():
            #for mov in movie:
            #    print(movie)
    return render(request,'MOVIE_REVIEW/index.html',context)

def detail(request,movie_id):
    movie =movies.objects.get(pk=movie_id)
    director = directors.objects.get(pk=movie.director_id)
    actor = movie_cast.objects.filter(movie=movie_id)
    coment = comments.objects.filter(mov_id=movie.pk).order_by('created').reverse()
    len_coment = len(coment)
    if len_coment==0:
        average=0
    else:
        average = sum(com.points for com in coment)/len_coment
        average=round(average,2)
    form = addcomment(request.POST)
    query = request.GET.get('q')
    if query:
        #filtre = request.GET.get('filtr')
        movie =movies.objects.filter(title__icontains = query)
        director =directors.objects.filter(name__icontains = query)
        actor = actors.objects.filter(name__icontains = query)
        return render(request,'MOVIE_REVIEW/search.html',{'movie':movie,'director':director,'actor':actor})
    if request.method == 'POST':
        if True:
            form.is_valid()
            print("inside")
            form.instance.mov_id=movie
            #if form.instance.points < 0:
            #    form.instance.points=0
            #elif form.instance.points>10:
            #    form.instance.points=10
            md = form.instance.mov_id
            ed = form.instance.email
            mid=md.id
            #print(md.id)
            #print(ed)
            check = comments.objects.filter(mov_id=mid)
            k = True
            for ch in check:
                if ch.email == ed:
                    k = False     
            if k:
                form.save()
            else:  
                print("error")  
                return render(request,'MOVIE_REVIEW/comerror.html',{'mid':mid})
            cur = connection.cursor()  
            print("sdfabsdf kjbagfsakjdfgsdalkjfhk")
            print(md.id)
            # execute the stored procedure passing in   
            # search_string as a parameter  
            cur.callproc('avgfinder', [md.id,])
            coment = comments.objects.filter(mov_id=movie.pk).order_by('created').reverse()
            len_coment = len(coment)
            #if len_coment==0:
            #    average=0
            #else:
            #    average = sum(com.points for com in coment)/len_coment
            #    average=round(average,2)
            movie =movies.objects.get(pk=movie_id)
            average=movie.userrating
            average=round(average,2)
    form = addcomment()
    #return HttpResponse("movie name is "+str(movieid))
    return render(request,'MOVIE_REVIEW/detail.html',{'movie':movie,'director':director,'actor':actor,'coment':coment,'length':len_coment,'form':form,'average':average})

def acto(request,acto_id):
    act = actors.objects.get(pk=acto_id)
    movi = movie_cast.objects.filter(actor=acto_id)
    query = request.GET.get('q')
    if query:
        #filtre = request.GET.get('filtr')
        movie =movies.objects.filter(title__icontains = query)
        director =directors.objects.filter(name__icontains = query)
        actor = actors.objects.filter(name__icontains = query)
        return render(request,'MOVIE_REVIEW/search.html',{'movie':movie,'director':director,'actor':actor})
    #all_movies=movies.objects.filter(pk = movi.movie )
    return render(request, 'MOVIE_REVIEW/acto.html', {'actor': act,'movie':movi})

def directo(request,directo_id):
    direct = directors.objects.get(pk=directo_id)
    movie =movies.objects.filter(director=directo_id)
    query = request.GET.get('q')
    if query:
        #filtre = request.GET.get('filtr')
        movie =movies.objects.filter(title__icontains = query)
        director =directors.objects.filter(name__icontains = query)
        actor = actors.objects.filter(name__icontains = query)
        return render(request,'MOVIE_REVIEW/search.html',{'movie':movie,'director':director,'actor':actor})
    return render(request, 'MOVIE_REVIEW/directo.html', {'direct': direct,'movie':movie})

def about(request):
    query = request.GET.get('q')
    if query:
        #filtre = request.GET.get('filtr')
        movie =movies.objects.filter(title__icontains = query)
        director =directors.objects.filter(name__icontains = query)
        actor = actors.objects.filter(name__icontains = query)
        return render(request,'MOVIE_REVIEW/search.html',{'movie':movie,'director':director,'actor':actor})
    return render(request, 'MOVIE_REVIEW/about.html',)

def mov(request):
    all_movies = movies.objects.all().order_by('title')
    query = request.GET.get('q')
    if query:
        #filtre = request.GET.get('filtr')
        movie =movies.objects.filter(title__icontains = query)
        director =directors.objects.filter(name__icontains = query)
        actor = actors.objects.filter(name__icontains = query)
        return render(request,'MOVIE_REVIEW/search.html',{'movie':movie,'director':director,'actor':actor})
    return render(request, 'MOVIE_REVIEW/mov.html', {'movie':all_movies})

def dir(request):
    all_directors = directors.objects.all().order_by('name')
    query = request.GET.get('q')
    if query:
        #filtre = request.GET.get('filtr')
        movie =movies.objects.filter(title__icontains = query)
        director =directors.objects.filter(name__icontains = query)
        actor = actors.objects.filter(name__icontains = query)
        return render(request,'MOVIE_REVIEW/search.html',{'movie':movie,'director':director,'actor':actor})
    return render(request, 'MOVIE_REVIEW/dir.html', {'director':all_directors})

def act(request):
    all_male = actors.objects.all().order_by('name')
    query = request.GET.get('q')
    if query:
        #filtre = request.GET.get('filtr')
        movie =movies.objects.filter(title__icontains = query)
        director =directors.objects.filter(name__icontains = query)
        actor = actors.objects.filter(name__icontains = query)
        return render(request,'MOVIE_REVIEW/search.html',{'movie':movie,'director':director,'actor':actor})
    #all_female = actors.objects.filter(gender='female' or 'Female').order_by('name')
    return render(request, 'MOVIE_REVIEW/act.html', {'males':all_male})







