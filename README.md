beegees
=======
![Beegees](http://sebastiandieser.com/dev/beegees/logo-beegees.jpg)

####"For those that are bored of their backgrounds."

**Why Beeges?**

backgrounds -> bg's -> bgs -> [beegees](https://www.youtube.com/watch?v=I_izvAbhExY "Beegees")

**Details:**

- Run `python download.py`
- Change path in scripts/beeges.py to yours. `beegees_dir = '.../pybeegees/images'` (Will set absolute path later but give the user option to change location of images)
- Run `python setup.py`
- Should set sym link. If it doesn't then you need to create link beegees to /scripts/beeges.py


**Features:**

- Change background image when script is invoked
- Set location and option to download backgrounds of pybeegees site

**Todo:**

- Set cron to change based on user preference. (Daily, weekly, monthly)
- Change backgrounds of all desktops. (Find a way)
- Option to delete current background image. API should be extended to be able to share backgrounds to other beegees users. Just a simple download request.