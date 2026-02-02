from PIL import Image
import os

def convert_gif_to_webp(gif_path, quality=80):
    """Convert animated GIF to animated WebP"""
    try:
        webp_path = os.path.splitext(gif_path)[0] + '.webp'
        original_size = os.path.getsize(gif_path)
        
        with Image.open(gif_path) as img:
            # Get all frames
            frames = []
            durations = []
            
            try:
                while True:
                    # Convert frame to RGBA
                    frame = img.convert('RGBA')
                    frames.append(frame.copy())
                    durations.append(img.info.get('duration', 100))
                    img.seek(img.tell() + 1)
            except EOFError:
                pass
            
            if len(frames) > 1:
                # Save as animated WebP
                frames[0].save(
                    webp_path,
                    'WEBP',
                    save_all=True,
                    append_images=frames[1:],
                    duration=durations,
                    loop=0,
                    quality=quality,
                    method=4
                )
            else:
                frames[0].save(webp_path, 'WEBP', quality=quality)
        
        webp_size = os.path.getsize(webp_path)
        saved_pct = (1 - webp_size/original_size) * 100
        print(f"✓ {os.path.basename(gif_path)}: {original_size/1024/1024:.1f}MB → {webp_size/1024/1024:.1f}MB ({saved_pct:.0f}% smaller)")
        return original_size - webp_size
    except Exception as e:
        print(f"✗ {gif_path}: {e}")
        return 0

gifs = [
    "assets/Project 1/YB+WTR.gif",
    "assets/Project 2/CAB.gif",
    "assets/Project 2/color switching gif.gif",
    "assets/Project 3/image 0.gif",
    "assets/Project 4/nav bar.gif"
]

total_saved = 0
for gif in gifs:
    if os.path.exists(gif):
        saved = convert_gif_to_webp(gif)
        total_saved += saved

print(f"\nTotal saved: {total_saved/1024/1024:.1f}MB")
