from .volume import volume

def get():
    return volume.get()

def set(percent):
    volume.set(percent)

def mute():
    volume.mute()
