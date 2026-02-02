import re
import glob
import os

def update_img_to_picture(html_content):
    """Replace <img> tags with <picture> elements for WebP support"""
    
    # Pattern to match img tags with src pointing to png/jpg
    img_pattern = r'<img([^>]*?)src="([^"]+\.(png|jpg|jpeg))"([^>]*?)>'
    
    def replace_img(match):
        before_src = match.group(1)
        src = match.group(2)
        ext = match.group(3)
        after_src = match.group(4)
        
        # Create webp path
        webp_src = src.rsplit('.', 1)[0] + '.webp'
        
        # Build picture element
        return f'''<picture>
                <source srcset="{webp_src}" type="image/webp">
                <img{before_src}src="{src}"{after_src}>
            </picture>'''
    
    return re.sub(img_pattern, replace_img, html_content, flags=re.IGNORECASE)

# Process all HTML files
html_files = ['index.html', 'about.html'] + glob.glob('work/*.html')

for filepath in html_files:
    print(f"Processing {filepath}...")
    with open(filepath, 'r') as f:
        content = f.read()
    
    updated = update_img_to_picture(content)
    
    with open(filepath, 'w') as f:
        f.write(updated)

print("Done! All HTML files updated to use WebP with PNG fallback.")
