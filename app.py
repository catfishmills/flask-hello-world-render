import os
import random
from flask import Flask, render_template_string

app = Flask(__name__)

# The "poster": HTML (words) + CSS (paint), with blanks to fill in.
PAGE = """
<!doctype html>
<html>
<head>
  <title>Larisa can't make up her mind</title>
  <style>
    body {
      margin: 0;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: Arial, sans-serif;
      color: white;
      text-align: center;
      background: linear-gradient(135deg, {{ color1 }}, {{ color2 }});
    }
    .card {
      background: rgba(0, 0, 0, 0.25);
      padding: 40px 60px;
      border-radius: 20px;
    }
    h1 { font-size: 3rem; margin: 0 0 10px; }
    .emoji { font-size: 5rem; }
  </style>
</head>
<body>
  <div class="card">
    <div class="emoji">{{ emoji }}</div>
    <h1>Hello, World!</h1>
    <h2>Catfish Awaits You</h2>
    <p>Refresh the page for a new look.</p>
    <small>Running commit: {{ commit }}</small>
  </div>
</body>
</html>
"""

PALETTES = [
    ("#ff512f", "#dd2476"),  # sunset
    ("#1fa2ff", "#12d8fa"),  # ocean
    ("#11998e", "#38ef7d"),  # mint
    ("#8e2de2", "#4a00e0"),  # grape
    ("#f7971e", "#ffd200"),  # sunshine
]
EMOJIS = ["🐟", "🎣", "🌊", "🐱", "🦈", "🐙"]

@app.route('/')
def hello_world():
    color1, color2 = random.choice(PALETTES)
    return render_template_string(
        PAGE,
        color1=color1,
        color2=color2,
        emoji=random.choice(EMOJIS),
        commit=os.environ.get("RENDER_GIT_COMMIT", "local")[:7],
    )
