# Portfolio Editing Guide

A quick reference for making common updates to your portfolio.

---

## Pushing Changes Live

After making any changes, run these commands in your terminal:

```bash
git add .
git commit -m "Your description of changes"
git push
```

Your site will update automatically within 1-2 minutes.

---

## Adding a New Case Study

### 1. Create the project folder
Add your images to `assets/Project X/` (replace X with the next number).

### 2. Create the HTML file
Copy an existing project file (e.g., `projects/project-5.html`) and save as `projects/project-7.html`.

### 3. Update the new project file
Edit these parts:
- `<title>` tag
- Meta description and OG tags (URL-encode spaces in image paths with `%20`)
- `<h1>` and `.case-study-meta` text
- Hero image/video path
- All section content and image paths
- Table of contents links (if using)

### 4. Add to homepage (`index.html`)
Add a new work card before the closing `</section>` of the work section:

```html
<a href="/projects/project-7.html" class="work-card">
    <div class="work-image">
        <img src="assets/Project 7/thumbnail.png" alt="Project Name">
    </div>
    <div class="work-content">
        <h2>Project Name</h2>
        <p class="work-description">
            Short description here.
        </p>
        <span class="work-link">View case study →</span>
    </div>
</a>
```

### 5. Update navigation links
- In your new project: Set prev/next to adjacent projects
- In the previous last project: Update its "next" to point to your new project
- In project-1: Update its "prev" to point to your new project (projects loop)

Navigation structure:
```html
<nav class="case-study-nav">
    <a href="/projects/project-6.html" class="nav-prev">
        <div class="nav-text">
            <span>Previous</span>
            <strong>Project Name</strong>
        </div>
        <div class="nav-thumb">
            <img src="../assets/Project 6/thumbnail.png" alt="Project Name">
        </div>
    </a>
    <a href="/projects/project-1.html" class="nav-next">
        <div class="nav-text">
            <span>Next</span>
            <strong>Project Name</strong>
        </div>
        <div class="nav-thumb">
            <img src="../assets/Project 1/thumbnail.png" alt="Project Name">
        </div>
    </a>
</nav>
```

---

## Editing Existing Case Studies

Open the project file in `projects/` and edit the HTML directly.

### Common elements:

**Section with label:**
```html
<section class="case-study-section">
    <span class="section-label">Problem</span>
    <h2>Your heading here</h2>
    <p>Your paragraph text here.</p>
</section>
```

**Section without label:**
```html
<section class="case-study-section">
    <h2>Your heading here</h2>
    <p>Your paragraph text here.</p>
</section>
```

**Single image:**
```html
<figure class="case-study-image">
    <img src="../assets/Project X/image.png" alt="Description">
    <figcaption>Optional caption</figcaption>
</figure>
```

**Image gallery (2 columns):**
```html
<div class="case-study-gallery">
    <figure><img src="../assets/Project X/image1.png" alt=""></figure>
    <figure><img src="../assets/Project X/image2.png" alt=""></figure>
</div>
```

**3-column gallery:**
```html
<div class="case-study-gallery three-up">
    ...
</div>
```

**Quote (chat bubble style):**
```html
<blockquote>
    "Quote text here."
</blockquote>
```

**Green centered quote:**
```html
<blockquote class="green-quote">
    "Quote text here."
</blockquote>
```

**Callout box:**
```html
<div class="callout">
    <p>Important text here.</p>
</div>
```

**Bullet list:**
```html
<ul class="results-list">
    <li>Item one</li>
    <li>Item two</li>
</ul>
```

---

## Image Size Classes

Add these classes to `<figure class="case-study-image">` to control width:

| Class | Max Width |
|-------|-----------|
| (none) | 800px |
| `small` | 500px |
| `smaller` | 400px |
| `tiny` | 300px |

Example: `<figure class="case-study-image small">`

For inline styles: `<figure class="case-study-image" style="max-width: 600px;">`

---

## Gallery Alignment Classes

Add to `.case-study-gallery`:

| Class | Effect |
|-------|--------|
| `top-align` | Fixed 350px height, images crop from top |
| `top-align tall` | Fixed 450px height |
| `bottom-align` | Fixed 350px height, images show bottom portion |
| `align-top` | No fixed height, images align at top |

---

## Updating the About Page

Edit `about.html`:

- **Bio text:** Find the `<p class="lead">` tag
- **Currently reading:** Update the book image, title, author, and quote in `.currently-reading-box`
- **Profile picture:** Replace `assets/about/profile pic.jpg`

---

## Updating the Homepage

Edit `index.html`:

- **Hero text:** Find `.hero-title`
- **Work cards:** Each project is an `<a class="work-card">` block
- **Contact links:** Find `.contact-links`

---

## Adding Videos

**Hero video (with controls on hover):**
```html
<div class="case-study-hero">
    <video autoplay loop muted playsinline controls>
        <source src="../assets/Project X/video.mp4" type="video/mp4">
    </video>
</div>
```

**Inline video (no controls):**
```html
<figure class="case-study-image inline-video">
    <video autoplay loop muted playsinline>
        <source src="../assets/Project X/video.mp4" type="video/mp4">
    </video>
</figure>
```

---

## File Structure Reference

```
/
├── index.html          # Homepage
├── about.html          # About page
├── resume.html         # Resume (redirects to Google Drive)
├── styles.css          # All styling
├── projects/
│   ├── project-1.html  # Shop Goodreads on Amazon
│   ├── project-2.html  # Color Writing on Kindle
│   ├── project-3.html  # MongoDB Private Link
│   ├── project-4.html  # MyDiya
│   ├── project-5.html  # MongoDB Billing
│   └── project-6.html  # Disney
└── assets/
    ├── favicon.png
    ├── about/
    ├── Project 1/
    ├── Project 2/
    └── ...
```

---

## Quick Fixes

**Image not showing?**
- Check the file path (case-sensitive!)
- Spaces in paths need `%20` in URLs, but work fine in `src` attributes

**Thumbnail cut off on mobile?**
- Add a custom class in `styles.css` with mobile-specific `object-position`

**Need to update resume link?**
- Edit `resume.html` — change the URL in the meta refresh and JavaScript redirect
