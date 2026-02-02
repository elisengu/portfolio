#!/usr/bin/env python3
"""
Update HTML files to use blur-up placeholder technique.
Adds tiny placeholder as background, loads full image on top.
"""

import os
import re
from pathlib import Path

def update_html_file(filepath):
    """Update picture elements to include blur placeholder."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Pattern to match picture elements with webp source
    # We'll add a data-placeholder attribute to the img for JS to use
    pattern = r'<picture>\s*<source srcset="([^"]+\.webp)"[^>]*>\s*<img([^>]*?)src="([^"]+)"([^>]*?)>'
    
    def replace_picture(match):
        webp_src = match.group(1)
        img_attrs_before = match.group(2)
        png_src = match.group(3)
        img_attrs_after = match.group(4)
        
        # Generate placeholder path
        placeholder_src = webp_src.replace('.webp', '-placeholder.webp')
        
        # Check if placeholder exists
        # Convert relative path to check
        check_path = placeholder_src
        if filepath.startswith('work/'):
            check_path = placeholder_src.replace('../', '')
        
        if not os.path.exists(check_path):
            return match.group(0)  # Return unchanged if no placeholder
        
        # Add data-placeholder attribute if not already present
        if 'data-placeholder' not in img_attrs_before and 'data-placeholder' not in img_attrs_after:
            return f'<picture>\n                <source srcset="{webp_src}" type="image/webp">\n                <img{img_attrs_before}src="{png_src}" data-placeholder="{placeholder_src}"{img_attrs_after}>'
        
        return match.group(0)
    
    content = re.sub(pattern, replace_picture, content, flags=re.DOTALL)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    html_files = ['index.html', 'about.html']
    html_files.extend([f'work/{f}' for f in os.listdir('work') if f.endswith('.html')])
    
    updated = 0
    for filepath in html_files:
        if os.path.exists(filepath):
            if update_html_file(filepath):
                print(f"Updated: {filepath}")
                updated += 1
            else:
                print(f"No changes: {filepath}")
    
    print(f"\nUpdated {updated} files")

if __name__ == "__main__":
    main()
