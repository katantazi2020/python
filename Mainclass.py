from Drums import Drums
from Synth import Synth

def play_instrument(obj):
    obj.play()

dr = Drums()
sy = Synth()

play_instrument(dr)
play_instrument(sy)