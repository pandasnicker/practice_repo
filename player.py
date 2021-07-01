from pygame import mixer

mixer.init()
try:
    mixer.music.load(r'C:\Users\mgula\Desktop\Py_Prog\The La La La Remix.mp3')
    mixer.music.play()
except:
    pass