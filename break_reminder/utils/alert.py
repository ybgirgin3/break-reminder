from pydub import AudioSegment
from pydub.playback import play


def alert(alert):
    "alert sound"
    play(AudioSegment.from_file(alert))
