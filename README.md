# Music Web Application Using Django Framework
## This is my seamless and interactive music web application developed for my Naan Mudhalvan Course Project Submission
## BeatBox
### __BeatBox__ is the name of my music web application . It is built using Django framework and aims to provide users with a 
- platform to listen to music
- search for their favorite tracks
- listen later their added tracks
- keep track of their listening history.

# Admin Username and Password (Superuser)
## To access the admin panel and manage the application, use the following credentials:
### Admin Username: Navenesvar
### Admin Password: navenesvar

# Regular Username and Password
## I used the following regular user credentials for my screenshots and channel music uploading.
###  Username: Navenesvar_27
###  Password: naven1032


## Features of the Web App
- User Authentication: Secure user authentication system allows users to create accounts, log in, and manage their profiles.
- Lister Later: Users can add tracks to their "Lister Later" playlist to listen to them at their convenience.
- My Channel: Personalized channels allow users to curate their own playlists and share them with others.
- Search Functionality: Robust search feature enables users to discover new music based on music title.
- History: Track listening history to revisit favorite songs and discover new ones based on past preferences.

# Project Setup
To set up the project locally, follow these steps:

- Clone the repository:
```
git clone https://github.com/Navenesvar/Naanmudhalvan_Project_Submission.git
```
- Create a virtual environment:
```
python -m venv venv
```

- Activate the virtual environment:
  - On Windows:

```
venv\Scripts\activate
```
  - On macOS/Linux:

```
source venv/bin/activate
```
- Navigate to the project directory:
```
cd naanmudhalvan_project_submission
```
- Install Django and Pillow(for managing images)
```
pip install django
pip -m install Pillow
```
- Create a superuser(admin): Give the username and password
```
python manage.py createsuperuser
```
- Start the development server:
```
python manage.py runserver
```

Visit http://127.0.01:8000 in your browser to access the Music web Application __BeatBox__

Visit http://127.0.0.1:8000/admin/ in your browser and log in with the superuser credentials.

