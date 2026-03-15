# Manas Parth Vaishnav - Portfolio Website

A modern, responsive portfolio website showcasing the skills and projects of Manas Parth Vaishnav, a Grade 7 student passionate about web development and Python programming.

## 📋 Features

- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Modern UI**: Clean and professional design with smooth animations
- **Interactive Elements**: Smooth scrolling, form validation, and dynamic effects
- **Skills Showcase**: Display of HTML, CSS, and Python skills with progress bars
- **Projects Gallery**: Showcase of various projects with descriptions and tags
- **Contact Form**: Functional contact form with validation
- **Mobile Menu**: Hamburger menu for mobile navigation
- **Accessibility**: Semantic HTML and keyboard navigation support

## 📁 Project Structure

```
portfolio_website/
├── index.html      # Main HTML file with page structure
├── style.css       # CSS styling and responsive design
├── script.js       # JavaScript for interactivity
├── app.py          # Python server to run the website
└── README.md       # This file
```

## 🚀 How to Run

### Option 1: Using Python Server (Recommended)

1. Open Command Prompt or Terminal
2. Navigate to the portfolio_website directory:
   ```bash
   cd "c:\Users\munag\OneDrive\Codingal Classes - AI\portfolio_website"
   ```
3. Run the Python server:
   ```bash
   python app.py
   ```
4. Open your browser and go to: `http://localhost:8000`

### Option 2: Direct File Opening

1. Navigate to the portfolio_website folder
2. Right-click on `index.html`
3. Select "Open with" and choose your browser

### Option 3: Using Python's Built-in Server

```bash
cd "c:\Users\munag\OneDrive\Codingal Classes - AI\portfolio_website"
python -m http.server 8000
```

## 📚 Technologies Used

- **HTML5**: Semantic markup and structure
- **CSS3**: Modern styling with gradients, flexbox, and grid
- **JavaScript**: Interactivity and dynamic features
- **Python**: Server-side file serving

## 🎨 Customization

### Update Personal Information

Edit `index.html` to update:
- Name and title
- About section content
- Contact information
- Social media links

### Modify Colors

Edit `style.css` CSS variables:
```css
:root {
    --primary-color: #6366f1;
    --secondary-color: #ec4899;
    --dark-bg: #0f172a;
    --light-bg: #f8fafc;
    --text-dark: #1e293b;
    --text-light: #64748b;
}
```

### Add More Projects

Add new project cards in the Projects section of `index.html`:
```html
<div class="project-card">
    <div class="project-image">
        <div class="project-placeholder">🎯</div>
    </div>
    <h3>Project Name</h3>
    <p>Project description</p>
    <div class="project-tags">
        <span class="tag">Technology</span>
    </div>
</div>
```

## 📱 Responsive Breakpoints

- **Desktop**: 1200px and above
- **Tablet**: 768px to 1199px
- **Mobile**: Below 768px

## ✨ Features Explained

### Navigation
- Sticky navigation bar with smooth scrolling
- Mobile hamburger menu for smaller screens
- Active link highlighting based on scroll position

### Hero Section
- Eye-catching gradient background
- Call-to-action button
- Animated entrance effect

### About Section
- Personal introduction
- Statistics cards with hover effects
- Responsive grid layout

### Skills Section
- Skill cards with icons
- Animated progress bars
- Hover effects and transitions

### Projects Section
- Project cards with emoji placeholders
- Technology tags
- Hover animations

### Contact Section
- Functional contact form
- Form validation
- Success message on submission

### Footer
- Social media links
- Copyright information

## 🔧 Browser Compatibility

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## 📝 Notes

- The contact form shows a success message but doesn't send emails (requires backend setup)
- All animations are CSS-based for better performance
- The website is fully responsive and mobile-friendly
- JavaScript includes smooth scrolling and form validation

## 🎓 Learning Resources

This portfolio demonstrates:
- HTML5 semantic structure
- CSS3 modern layouts (Flexbox, Grid)
- CSS animations and transitions
- JavaScript DOM manipulation
- Responsive web design
- Python HTTP server basics

## 📧 Contact

For questions or suggestions about this portfolio, feel free to reach out!

---

**Created by**: Manas Parth Vaishnav  
**Grade**: 7  
**Skills**: HTML, CSS, Python  
**Year**: 2024
