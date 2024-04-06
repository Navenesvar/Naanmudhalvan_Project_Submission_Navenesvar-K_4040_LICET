from django.shortcuts import redirect, render
from music_app.models import Channel, Song, Watchlater, History
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.db.models import Case, When
from django.contrib import messages
from django.db import IntegrityError



def index(request):
    song = Song.objects.all()
    return render(request,'index.html',{'song':song})

def songs(request):
    song = Song.objects.all()
    return render(request,'music_app/songs.html',{'song':song})

def songpost(request,id):
    song = Song.objects.filter(song_id=id).first()
    return render(request,'music_app/songpost.html',{'song':song})
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use auth_login instead of login
            return redirect("/")  # Redirect the user after successful login
        else:
            messages.warning(request, "Invalid username or password. Please try again.")

    return render(request, 'music_app/login.html')

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        try:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = first_name
            myuser.last_name = last_name
            myuser.save()

            user = authenticate(username=username, password=pass1)
            from django.contrib.auth import login
            login(request, user)

            channel = Channel(name=username)
            channel.save()

            return redirect('/')
        except IntegrityError:
            messages.warning(request, "Username is already taken. Please try another one.")

    return render(request, 'music_app/signup.html')

def logout_user(request):
    logout(request)
    return redirect("/")

def channel(request, channel):
    chan = Channel.objects.filter(name=channel).first()
    video_ids = str(chan.music).split(" ")[1:]

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(video_ids)])
    song = Song.objects.filter(song_id__in=video_ids).order_by(preserved)    

    return render(request, "music_app/channel.html", {"channel": chan, "song": song})

def watchlater(request):
    if request.method == "POST":
        user = request.user
        video_id = request.POST['video_id']

        watch = Watchlater.objects.filter(user=user)
        
        for i in watch:
            if video_id == i.video_id:
                message = "Your Video is Already Added"
                break
        else:
            watchlater = Watchlater(user=user, video_id=video_id)
            watchlater.save()
            message = "Your Video is Succesfully Added"

        song = Song.objects.filter(song_id=video_id).first()
        return render(request, f"music_app/songpost.html", {'song': song, "message": message})

    wl = Watchlater.objects.filter(user=request.user)
    ids = []
    for i in wl:
        ids.append(i.video_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)

    return render(request, "music_app/watchlater.html", {'song': song})

def history(request):
    if request.method == "POST":
        user = request.user
        music_id = request.POST['music_id']
        history = History(user=user, music_id=music_id)
        history.save()

        return redirect(f"songs/{music_id}")

    history = History.objects.filter(user=request.user)
    ids = []
    for i in history:
        ids.append(i.music_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)

    return render(request, 'music_app/history.html', {"history": song})


def upload(request):
    if request.method == "POST":
        name = request.POST['name']
        singer = request.POST['singer']
        tag = request.POST['tag']
        image = request.FILES['image']
        movie = request.POST['movie']
        credit = request.POST['credit']
        song1 = request.FILES['file']

        song_model = Song(name=name, singer=singer, tags=tag, image=image, movie=movie, credit=credit, song=song1)
        song_model.save()

        music_id = song_model.song_id
        channel_find = Channel.objects.filter(name=str(request.user))
        print(channel_find)

        for i in channel_find:
            i.music += f" {music_id}"
            i.save()

    return render(request, "music_app/upload.html")

def search(request):
    query = request.GET.get("query")
    song = Song.objects.all()
    qs = song.filter(name__icontains=query)
    return render(request,'music_app/search.html',{'songs':qs,'query':query})