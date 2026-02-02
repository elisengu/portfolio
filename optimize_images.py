#!/usr/bin/env python3
"""
Re-compress WebP images at 80% quality and generate tiny blur placeholders.
"""

from PIL import Image
import os

ASSETS_DIR = "assets"
QUALITY = 80
PLACEHOLDER_SIZE = 20  # Tiny placeholder for blur-up effect

def get_image_files():
    """Get all PNG/JPG files in assets folders."""
    image_files = []
    for root, dirs, files in os.walk(ASSETS_DIR):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')) and not file.startswith('.'):
                image_files.append(os.path.join(root, file))
    return image_files

def compress_and_create_placeholder(image_path):
    """Compress to WebP at 80% and create tiny placeholder."""
    try:
        img = Image.open(image_path)
        
        # Convert to RGB if necessary
        if img.mode in ('RGBA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[3] if len(img.split()) > 3 else None)
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Save WebP at 80% quality
        webp_path = os.path.splitext(image_path)[0] + '.webp'
        old_size = os.path.getsize(webp_path) if os.path.exists(webp_path) else 0
        img.save(webp_path, 'WEBP', quality=QUALITY, method=6)
        new_size = os.path.getsize(webp_path)
        
        # Create tiny placeholder
        placeholder_path = os.path.splitext(image_path)[0] + '-placeholder.webp'
        aspect = img.width / img.height
        if aspect > 1:
            placeholder_size = (PLACEHOLDER_SIZE, int(PLACEHOLDER_SIZE / aspect))
        else:
            placeholder_size = (int(PLACEHOLDER_SIZE * aspect), PLACEHOLDER_SIZE)
        
        placeholder = img.resize(placeholder_size, Image.Resampling.LANCZOS)
        placeholder.save(placeholder_path, 'WEBP', quality=60)
        placeholder_size_bytes = os.path.getsize(placeholder_path)
        
        savings = old_size - new_size
        return savings, placeholder_size_bytes
        
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return 0, 0

def main():
    image_files = get_image_files()
    print(f"Processing {len(image_files)} images...")
    
    total_savings = 0
    total_placeholder_size = 0
    
    for i, image_path in enumerate(image_files, 1):
        savings, placeholder_size = compress_and_create_placeholder(image_path)
        total_savings += savings
        total_placeholder_size += placeholder_size
        print(f"[{i}/{len(image_files)}] {os.path.basename(image_path)} - saved {savings/1024:.1f}KB, placeholder {placeholder_size}B")
    
    print(f"\nTotal additional savings: {total_savings/1024/1024:.2f}MB")
    print(f"Total placeholder size: {total_placeholder_size/1024:.1f}KB")

if __name__ == "__main__":
    main()
