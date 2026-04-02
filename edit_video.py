import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def start_editing():
    print("Step 1: Removing background...")
    # This command uses AI to cut you out and put you on bg.jpg
    os.system('backgroundremover -i "input.mp4" -toi -bi "bg.jpg" -o "no_bg.mov"')

    print("Step 2: Adding Stanford-style text...")
    clip = VideoFileClip("no_bg.mov")
    
    # Large bold text
    txt = TextClip("SARA 2026", fontsize=150, color='white', font='Arial-Bold')
    txt = txt.set_position('center').set_duration(4).fadein(1)

    # Combine and save
    final = CompositeVideoClip([clip, txt])
    final.write_videofile("final_output.mp4", codec="libx264", fps=24)

if __name__ == "__main__":
    start_editing()
