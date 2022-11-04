from pydub import AudioSegment
from pydub.playback import play


def alert():
    "alert sound when session done"
    sound = "media/alert.wav"
    song = AudioSegment.from_file(sound)
    play(song)
