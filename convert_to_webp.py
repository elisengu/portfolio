from PIL import Image
import os
import glob

def convert_to_webp(filepath, quality=90):
    """Convert image to WebP format with high quality"""
    try:
        webp_path = os.path.splitext(filepath)[0] + '.webp'
        original_size = os.path.getsize(filepath)
        
        with Image.open(filepath) as img:
            # Keep original resolution, just convert format
            if img.mode == 'RGBA':
                img.save(webp_path, 'WEBP', quality=quality, method=6)
            else:
                img.save(webp_path, 'WEBP', quality=quality, method=6)
        
        webp_size = os.path.getsize(webp_path)
        saved_pct = (1 - webp_size/original_size) * 100
        print(f"✓ {os.path.basename(filepath)}: {original_size/1024:.0f}KB → {webp_size/1024:.0f}KB ({saved_pct:.0f}% smaller)")
        return original_size - webp_size
    except Exception as e:
        print(f"✗ {filepath}: {e}")
        return 0

total_saved = 0
count = 0

for pattern in ['assets/**/*.png', 'assets/**/*.jpg', 'assets/**/*.jpeg']:
    for filepath in glob.glob(pattern, recursive=True):
        webp_path = os.path.splitext(filepath)[0] + '.webp'
        # Regenerate all WebP files with higher quality
        saved = convert_to_webp(filepath, quality=90)
        total_saved += saved
        count += 1

print(f"\nConverted {count} images at 90% quality")
print(f"Total saved: {total_saved/1024/1024:.1f}MB")
