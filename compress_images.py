from PIL import Image
import os
import glob

def compress_image(filepath, max_width=1600, quality=85):
    """Compress image while maintaining aspect ratio"""
    try:
        original_size = os.path.getsize(filepath)
        
        with Image.open(filepath) as img:
            # Convert RGBA to RGB for JPEG (if saving as JPEG)
            if img.mode == 'RGBA':
                # Keep as PNG but optimize
                if img.width > max_width:
                    ratio = max_width / img.width
                    new_height = int(img.height * ratio)
                    img = img.resize((max_width, new_height), Image.LANCZOS)
                img.save(filepath, optimize=True)
            else:
                # Resize if too large
                if img.width > max_width:
                    ratio = max_width / img.width
                    new_height = int(img.height * ratio)
                    img = img.resize((max_width, new_height), Image.LANCZOS)
                
                # Save with optimization
                if filepath.lower().endswith('.png'):
                    img.save(filepath, optimize=True)
                else:
                    img.save(filepath, quality=quality, optimize=True)
        
        new_size = os.path.getsize(filepath)
        saved = original_size - new_size
        if saved > 0:
            print(f"✓ {filepath}: {original_size/1024/1024:.1f}MB → {new_size/1024/1024:.1f}MB (saved {saved/1024/1024:.1f}MB)")
        return saved
    except Exception as e:
        print(f"✗ {filepath}: {e}")
        return 0

# Find all large images (>300KB)
total_saved = 0
for pattern in ['assets/**/*.png', 'assets/**/*.jpg', 'assets/**/*.jpeg']:
    for filepath in glob.glob(pattern, recursive=True):
        size = os.path.getsize(filepath)
        if size > 300 * 1024:  # >300KB
            saved = compress_image(filepath)
            total_saved += saved

print(f"\nTotal saved: {total_saved/1024/1024:.1f}MB")
