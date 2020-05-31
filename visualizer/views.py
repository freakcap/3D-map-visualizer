from django.shortcuts import render
from django.conf import settings
from PIL import Image
import os, math, time
# Create your views here.

def visualize(request):
    create_sprite_atlas()
    return render(request, 'visualize.html', {})

def create_sprite_atlas():
    max_frames_row = 10.0
    frames = []
    tile_width = 0
    tile_height = 0

    spritesheet_width = 0
    spritesheet_height = 0

    files = os.listdir(settings.BASE_DIR +"/visualizer/frames")
    files.sort()
    print(files)

    for current_file in files :
        try:
            with Image.open(settings.BASE_DIR +"/visualizer/frames/" + current_file) as im :
                frames.append(im.getdata())
        except:
            print(current_file + " is not a valid image")

    tile_width = frames[0].size[0]
    tile_height = frames[0].size[1]

    if len(frames) > max_frames_row :
        spritesheet_width = tile_width * max_frames_row
        required_rows = math.ceil(len(frames)/max_frames_row)
        spritesheet_height = tile_height * required_rows
    else:
        spritesheet_width = tile_width*len(frames)
        spritesheet_height = tile_height
        
    print(spritesheet_height)
    print(spritesheet_width)

    spritesheet = Image.new("RGBA",(int(spritesheet_width), int(spritesheet_height)))
    # qq=0
    for current_frame in frames :
        top = tile_height * math.floor((frames.index(current_frame))/max_frames_row)
        left = tile_width * (frames.index(current_frame) % max_frames_row)
        bottom = top + tile_height
        right = left + tile_width
        
        box = (left,top,right,bottom)
        box = [int(i) for i in box]
        cut_frame = current_frame.crop((0,0,int(tile_width),int(tile_height)))
        cut_frame = cut_frame.convert("RGBA")
        # qq+=1
        # print(qq)
        spritesheet.paste(cut_frame, box)
        
    os.remove(settings.BASE_DIR +"/static/spritesheet.png")    
    spritesheet.save(settings.BASE_DIR +"/static/spritesheet" + ".png", "PNG")