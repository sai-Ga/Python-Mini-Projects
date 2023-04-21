import moviepy.editor as mp

def convert(path):
    clip = mp.VideoFileClip(r'{}'.format(path))
    clip.audio.write_audiofile(r'{}.mp3'.format(path[:-3]))
    
convert('samuari feels.webm')