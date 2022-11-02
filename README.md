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
* Pydub playing audio output requires to modify one of library files.<br>
  |_ using with output issue.
  * How to solve by hand:
  * Regarding to this issue [#247](https://github.com/jiaaro/pydub/issues/247#issuecomment-791768412)

    - in `lib/python3.x/site-packages/pydub/playback.py` file modify the following function
    ```py
      def _play_with_ffplay(seg):
      PLAYER = get_player_name()
      with NamedTemporaryFile("w+b", suffix=".wav") as f:
          seg.export(f.name, "wav")
          with open(os.devnull, "w") as fp:
              subprocess.call([PLAYER, "-nodisp", "-autoexit", "-hide_banner", f.name], stdout=fp, stderr=fp)
    ```

