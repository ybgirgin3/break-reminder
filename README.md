# break-reminder

## installation


** install requirements **
* for linux, mac
```sh
~$ pip install -r requirements.txt
```

* for windows
```sh
~$ pip install -r requirements.txt
~$ pip install -r requirements.windows.txt # for windows specific packages
```


** install dependencies **

* macOS
```sh
~$ brew install ffmpeg
```

* ubuntu, debian
```sh
~$ sudo apt install libnotify-bin
~$ sudo apt install ffmepeg
```

* fedora
```sh
~$ sudo dnf install libnotify
~$ sudo dnf instal ffmepeg
```


## For CLI
```sh
~$ python main.py --help

usage: main.py [-h] [--session-name SESSION_NAME] [--full] [--session-time SESSION_TIME] [--work-time WORK_TIME] [--break-time BREAK_TIME]

options:
  -h, --help            show this help message and exit
  --session-name SESSION_NAME
                        How many session do you plan to work (hour(s))
  --full                How many session do you plan to work (hour(s))
  --session-time SESSION_TIME
                        How many session do you plan to work (hour(s))
  --work-time WORK_TIME
                        work session time in minute
  --break-time BREAK_TIME
                        work session time in minute
```

## GUI
coming soon...



## Known Issues
* Pydub playing audio output requires to modify one of library files.
  |_ using with output issue.

