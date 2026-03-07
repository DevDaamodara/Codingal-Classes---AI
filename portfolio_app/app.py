from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# ============================
# Portfolio content placeholder
# Update these fields later with your real information. This is your single source of truth
# that feeds the page. You can change these now without touching the HTML.
# ============================
portfolio = {
    "name": "Your Name",
    "role": "Student / Developer",
    "summary": (
        "A short professional summary goes here. Share your passions, strengths, and "
        "what you are looking for (internship, collaboration, freelance, etc.)."
    ),
    "location": "City, Country",
    "email": "you@example.com",
    "phone": "+1 000 000 0000",
    "socials": {
        "github": "#",
        "linkedin": "#",
        "twitter": "#",
        "website": "#"
    },
    "skills": [
        {"name": "Python", "level": 85},
        {"name": "JavaScript", "level": 75},
        {"name": "HTML/CSS", "level": 90},
        {"name": "OpenCV", "level": 60}
    ],
    "projects": [
        {
            "title": "Project Alpha",
            "description": "Brief description of what the project does and why it matters.",
            "tags": ["Python", "Flask"],
            "link": "#",
            "repo": "#",
            "image": ""  # Optional: link to an image
        },
        {
            "title": "Project Beta",
            "description": "Another project summary, problems solved, and your role.",
            "tags": ["JavaScript", "Frontend"],
            "link": "#",
            "repo": "#",
            "image": ""
        }
    ],
    "experience": [
        {
            "company": "Company/Org Name",
            "role": "Role Title",
            "start": "Jan 2024",
            "end": "Present",
            "highlights": [
                "Key achievement or responsibility #1",
                "Key achievement or responsibility #2"
            ]
        }
    ],
    "education": [
        {
            "school": "School/University Name",
            "degree": "Degree / Program",
            "start": "2021",
            "end": "2025",
            "highlights": ["GPA / Awards / Activities"]
        }
    ],
    "achievements": [
        "Hackathon Winner - 2023",
        "Top 10 in Coding Challenge - 2024"
    ]
}


# Minimal inline HTML/CSS/JS template to serve a complete outline immediately.
# Later, we can split this into templates and static files.
PAGE_TEMPLATE = """
<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\"> 
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> 
  <title>{{ data.name }} — Portfolio</title>
  <meta name=\"description\" content=\"Portfolio of {{ data.name }} - {{ data.role }}\"> 
  <style>
    :root {
      --bg: #0b0f14;
      --panel: #111827;
      --muted: #9ca3af;
      --text: #e5e7eb;
      --brand: #38bdf8; /* cyan-400 */
      --accent: #a78bfa; /* violet-400 */
      --ok: #34d399; /* emerald-400 */
      --warn: #fbbf24; /* amber-400 */
      --danger: #f87171; /* red-400 */
      --ring: rgba(56, 189, 248, 0.35);
    }

    * { box-sizing: border-box; }
    html, body { margin: 0; padding: 0; font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, Noto Sans, \"Apple Color Emoji\", \"Segoe UI Emoji\"; background: var(--bg); color: var(--text); }

    a { color: var(--brand); text-decoration: none; }
    a:hover { text-decoration: underline; }

    .container { max-width: 1100px; margin: 0 auto; padding: 0 1rem; }

    /* Header / Nav */
    header { position: sticky; top: 0; z-index: 10; background: rgba(11, 15, 20, 0.8); backdrop-filter: blur(10px); border-bottom: 1px solid #1f2937; }
    .nav { display: flex; align-items: center; justify-content: space-between; height: 64px; }
    .brand { display: flex; align-items: center; gap: .5rem; font-weight: 700; letter-spacing: .5px; }
    .brand .dot { width: 10px; height: 10px; border-radius: 50%; background: linear-gradient(135deg, var(--brand), var(--accent)); box-shadow: 0 0 0 4px rgba(56, 189, 248, 0.15); }
    .nav a { color: var(--text); opacity: 0.85; }
    .nav a.active { color: var(--brand); opacity: 1; }
    .nav-links { display: flex; gap: 1rem; align-items: center; }
    .theme-toggle { border: 1px solid #1f2937; background: var(--panel); color: var(--text); padding: .4rem .6rem; border-radius: 8px; cursor: pointer; }

    /* Hero */
    .hero { display: grid; grid-template-columns: 1.2fr .8fr; gap: 2rem; align-items: center; padding: 3rem 0; }
    .hero-card { background: linear-gradient(180deg, rgba(17,24,39,0.9), rgba(17,24,39,0.6)); border: 1px solid #1f2937; border-radius: 14px; padding: 1.5rem; box-shadow: 0 10px 30px rgba(0,0,0,0.25); }
    .hero h1 { font-size: clamp(1.8rem, 2.5vw, 2.6rem); margin: 0 0 .6rem; }
    .hero p { color: var(--muted); line-height: 1.6; }
    .quick { display: flex; gap: .75rem; flex-wrap: wrap; margin-top: 1rem; }
    .chip { border: 1px solid #1f2937; background: #0f172a; color: #cbd5e1; padding: .35rem .6rem; border-radius: 999px; font-size: .85rem; }

    /* Sections */
    section { padding: 2.5rem 0; }
    section h2 { font-size: 1.4rem; margin: 0 0 1rem; letter-spacing: .5px; }
    .panel { background: var(--panel); border: 1px solid #1f2937; border-radius: 12px; padding: 1rem; }

    /* Skills */
    .skills { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; }
    .skill { background: #0f172a; border: 1px solid #1f2937; border-radius: 12px; padding: .9rem; }
    .meter { height: 10px; background: #0b1220; border: 1px solid #172036; border-radius: 999px; overflow: hidden; margin-top: .6rem; }
    .meter > span { display: block; height: 100%; background: linear-gradient(90deg, var(--brand), var(--accent)); width: 0; transition: width .8s ease; }

    /* Projects */
    .projects { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; }
    .project { background: #0f172a; border: 1px solid #1f2937; border-radius: 12px; padding: 1rem; display: flex; flex-direction: column; gap: .6rem; }
    .project .tags { display: flex; gap: .4rem; flex-wrap: wrap; }
    .tag { background: rgba(56,189,248,.12); color: #93c5fd; border: 1px solid rgba(56,189,248,.25); padding: .15rem .45rem; border-radius: 6px; font-size: .78rem; }

    /* Experience, Education */
    .timeline { display: grid; gap: .8rem; }
    .entry { background: #0f172a; border: 1px solid #1f2937; border-radius: 12px; padding: .9rem; }
    .entry .when { color: var(--muted); font-size: .9rem; }
    .entry ul { margin: .4rem 0 0 1rem; color: #cbd5e1; }

    /* Contact */
    form { display: grid; gap: .7rem; }
    input, textarea { background: #0b1220; color: var(--text); border: 1px solid #1f2937; border-radius: 10px; padding: .7rem .8rem; outline: none; }
    input:focus, textarea:focus { border-color: var(--brand); box-shadow: 0 0 0 4px var(--ring); }
    button { background: linear-gradient(90deg, var(--brand), var(--accent)); color: #0b0f14; font-weight: 700; border: none; border-radius: 10px; padding: .7rem .9rem; cursor: pointer; }

    /* Footer */
    footer { border-top: 1px solid #1f2937; color: var(--muted); padding: 1.2rem 0 2.2rem; text-align: center; }

    /* Responsive */
    @media (max-width: 860px) {
      .hero { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
  <header>
    <div class=\"container nav\">
      <div class=\"brand\">
        <span class=\"dot\"></span>
        <span>{{ data.name }}</span>
      </div>
      <nav class=\"nav-links\">
        <a href=\"#about\">About</a>
        <a href=\"#skills\">Skills</a>
        <a href=\"#projects\">Projects</a>
        <a href=\"#experience\">Experience</a>
        <a href=\"#education\">Education</a>
        <a href=\"#achievements\">Achievements</a>
        <a href=\"#contact\">Contact</a>
        <button class=\"theme-toggle\" id=\"themeToggle\" aria-label=\"Toggle theme\">Theme</button>
      </nav>
    </div>
  </header>

  <main class=\"container\">
    <!-- Hero -->
    <section class=\"hero\" id=\"about\">
      <div class=\"hero-card\">
        <h1>{{ data.name }} — <span style=\"color:var(--brand)\">{{ data.role }}</span></h1>
        <p>{{ data.summary }}</p>
        <div class=\"quick\"> 
          <span class=\"chip\">📍 {{ data.location }}</span>
          <a class=\"chip\" href=\"mailto:{{ data.email }}\">✉️ {{ data.email }}</a>
          {% if data.phone %}<span class=\"chip\">📞 {{ data.phone }}</span>{% endif %}
        </div>
        <div class=\"quick\" aria-label=\"Social links\">
          {% if data.socials.github %}<a class=\"chip\" href=\"{{ data.socials.github }}\" target=\"_blank\">GitHub</a>{% endif %}
          {% if data.socials.linkedin %}<a class=\"chip\" href=\"{{ data.socials.linkedin }}\" target=\"_blank\">LinkedIn</a>{% endif %}
          {% if data.socials.twitter %}<a class=\"chip\" href=\"{{ data.socials.twitter }}\" target=\"_blank\">Twitter/X</a>{% endif %}
          {% if data.socials.website %}<a class=\"chip\" href=\"{{ data.socials.website }}\" target=\"_blank\">Website</a>{% endif %}
        </div>
      </div>
      <div>
        <div class=\"panel\">
          <h2>Profile Snapshot</h2>
          <ul>
            <li>Role: {{ data.role }}</li>
            <li>Location: {{ data.location }}</li>
            <li>Contact: <a href=\"mailto:{{ data.email }}\">{{ data.email }}</a></li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Skills -->
    <section id=\"skills\">
      <h2>Skills</h2>
      <div class=\"skills\">
        {% for s in data.skills %}
        <div class=\"skill\">
          <div style=\"display:flex;justify-content:space-between;align-items:center\">
            <strong>{{ s.name }}</strong>
            <span class=\"muted\">{{ s.level }}%</span>
          </div>
          <div class=\"meter\"><span style=\"width: {{ s.level }}%\"></span></div>
        </div>
        {% endfor %}
      </div>
    </section>

    <!-- Projects -->
    <section id=\"projects\">
      <h2>Projects</h2>
      <div class=\"projects\">
        {% for p in data.projects %}
        <div class=\"project\">
          <div style=\"display:flex;justify-content:space-between;gap:1rem;align-items:flex-start\">
            <h3 style=\"margin:.2rem 0\">{{ p.title }}</h3>
            {% if p.link %}<a href=\"{{ p.link }}\" target=\"_blank\">Live</a>{% endif %}
            {% if p.repo %}<a href=\"{{ p.repo }}\" target=\"_blank\">Code</a>{% endif %}
          </div>
          <p style=\"color:var(--muted)\">{{ p.description }}</p>
          {% if p.tags %}
          <div class=\"tags\">
            {% for t in p.tags %}<span class=\"tag\">{{ t }}</span>{% endfor %}
          </div>
          {% endif %}
        </div>
        {% endfor %}
      </div>
    </section>

    <!-- Experience -->
    <section id=\"experience\">
      <h2>Experience</h2>
      <div class=\"timeline\">
        {% for e in data.experience %}
        <div class=\"entry\">
          <div style=\"display:flex;justify-content:space-between;gap:1rem;align-items:center\">
            <strong>{{ e.role }}</strong>
            <span class=\"when\">{{ e.start }} — {{ e.end }}</span>
          </div>
          <div style=\"color:#cbd5e1\">{{ e.company }}</div>
          {% if e.highlights %}
          <ul>
            {% for h in e.highlights %}<li>{{ h }}</li>{% endfor %}
          </ul>
          {% endif %}
        </div>
        {% endfor %}
      </div>
    </section>

    <!-- Education -->
    <section id=\"education\">
      <h2>Education</h2>
      <div class=\"timeline\">
        {% for ed in data.education %}
        <div class=\"entry\">
          <div style=\"display:flex;justify-content:space-between;gap:1rem;align-items:center\">
            <strong>{{ ed.degree }}</strong>
            <span class=\"when\">{{ ed.start }} — {{ ed.end }}</span>
          </div>
          <div style=\"color:#cbd5e1\">{{ ed.school }}</div>
          {% if ed.highlights %}
          <ul>
            {% for h in ed.highlights %}<li>{{ h }}</li>{% endfor %}
          </ul>
          {% endif %}
        </div>
        {% endfor %}
      </div>
    </section>

    <!-- Achievements -->
    <section id=\"achievements\">
      <h2>Achievements</h2>
      <div class=\"panel\">
        <ul>
          {% for a in data.achievements %}<li>{{ a }}</li>{% endfor %}
        </ul>
      </div>
    </section>

    <!-- Contact -->
    <section id=\"contact\">
      <h2>Contact</h2>
      <div class=\"panel\">
        <form id=\"contactForm\" autocomplete=\"on\" novalidate>
          <div style=\"display:grid;grid-template-columns:1fr 1fr;gap:.7rem\">
            <input name=\"name\" placeholder=\"Your name\" required>
            <input type=\"email\" name=\"email\" placeholder=\"Your email\" required>
          </div>
          <textarea name=\"message\" rows=\"5\" placeholder=\"Your message\" required></textarea>
          <button type=\"submit\">Send Message</button>
          <div id=\"contactStatus\" style=\"margin-top:.6rem;color:var(--muted)\"></div>
        </form>
      </div>
    </section>
  </main>

  <footer>
    <div class=\"container\">© <span id=\"year\"></span> {{ data.name }} • Built with Python (Flask) + HTML/CSS/JS</div>
  </footer>

  <script>
    // Basic JS: nav active state, skill meter animation, theme toggle, and contact form post.

    // Active link on scroll
    const sections = [...document.querySelectorAll('main section')];
    const links = [...document.querySelectorAll('header nav a')];
    const setActive = () => {
      const pos = window.scrollY + 120;
      let id = sections[0]?.id;
      for (const s of sections) {
        if (s.offsetTop <= pos) id = s.id;
      }
      links.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + id));
    };
    document.addEventListener('scroll', setActive);
    window.addEventListener('load', () => {
      setActive();
      // Animate skill meters
      document.querySelectorAll('.meter > span').forEach((el) => {
        const w = el.style.width; el.style.width = '0'; setTimeout(() => el.style.width = w, 50);
      });
      document.getElementById('year').textContent = new Date().getFullYear();
    });

    // Theme toggle (dark is default)
    const themeToggle = document.getElementById('themeToggle');
    const setTheme = (mode) => {
      document.documentElement.dataset.theme = mode; // not used for now, placeholder for future
      localStorage.setItem('theme', mode);
    };
    themeToggle?.addEventListener('click', () => {
      const cur = localStorage.getItem('theme') || 'dark';
      setTheme(cur === 'dark' ? 'light' : 'dark');
      alert('Theme mode saved (UI style already dark-focused).');
    });

    // Contact form
    const form = document.getElementById('contactForm');
    const status = document.getElementById('contactStatus');
    form?.addEventListener('submit', async (e) => {
      e.preventDefault();
      status.textContent = 'Sending...';
      const payload = Object.fromEntries(new FormData(form));
      try {
        const res = await fetch('/contact', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
        const data = await res.json();
        if (res.ok) {
          status.style.color = 'var(--ok)';
          status.textContent = data.message || 'Sent!';
          form.reset();
        } else {
          status.style.color = 'var(--danger)';
          status.textContent = data.error || 'Failed to send';
        }
      } catch (err) {
        status.style.color = 'var(--danger)';
        status.textContent = 'Network error';
      }
    });
  </script>
</body>
</html>
"""


@app.route("/", methods=["GET"])
def home():
    return render_template_string(PAGE_TEMPLATE, data=portfolio)


@app.route("/contact", methods=["POST"])
def contact():
    payload = request.get_json(silent=True) or {}
    name = (payload.get("name") or "").strip()
    email = (payload.get("email") or "").strip()
    message = (payload.get("message") or "").strip()

    if not name or not email or not message:
        return jsonify({"error": "Name, email, and message are required."}), 400

    # For now, we just log to server console. Later: integrate email/Discord/DB/etc.
    app.logger.info("[Contact] %s <%s>: %s", name, email, message)

    return jsonify({"message": "Thanks, your message has been received!"})


@app.route('/favicon.ico', methods=["GET"])
def favicon():
    return ("", 204)


if __name__ == "__main__":
    # Run local dev server
    app.run(host="0.0.0.0", port=5000, debug=True)
