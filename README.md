# Portfolio Website

A minimal, clean portfolio website.

## Setup

1. Replace placeholder content in `index.html` and `about.html` with your information
2. Add your images to the `assets/` folder:
   - `profile.jpg` - Your profile photo
   - Company logos (SVG or PNG recommended)
3. Update the `CNAME` file with your custom domain
4. Push to GitHub and enable GitHub Pages

## Customization

Edit `styles.css` to change:
- Colors (see `:root` variables)
- Fonts
- Spacing and layout

## GitHub Pages Deployment

1. Go to your repo Settings → Pages
2. Set Source to "Deploy from a branch"
3. Select `main` branch and `/ (root)` folder
4. Your site will be live at `https://yourusername.github.io/repo-name`

## Custom Domain

1. Update the `CNAME` file with your domain
2. In your domain registrar, add these DNS records:
   - A record: `185.199.108.153`
   - A record: `185.199.109.153`
   - A record: `185.199.110.153`
   - A record: `185.199.111.153`
   - Or CNAME: `yourusername.github.io`
