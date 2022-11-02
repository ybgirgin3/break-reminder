from pydub import AudioSegment
from pydub.playback import play


def alert():
    sound = "media/alert.wav"
    song = AudioSegment.from_file(sound)
    play(song)
