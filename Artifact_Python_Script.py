
"""
Run:
    python3 Artifact_Python_Script.py

Output:
    Unessay_artifact.html
"""

from pathlib import Path

EVENTS = [
    {
        "year": "1859",
        "title": "Pennsylvania oil begins the modern industry",
        "lesson": "Lessons 1–2 / The Prize",
        "economy": "Oil became a scalable commercial product and laid the foundation for a modern energy market.",
        "politics": "Control over production, transport, and refining quickly became a source of power.",
        "daily_life": "Kerosene changed illumination and everyday household life."
    },
    {
        "year": "1901",
        "title": "Spindletop and the age of abundance",
        "lesson": "Early course / The Prize",
        "economy": "Massive production lowered costs and accelerated industrial expansion.",
        "politics": "Texas rose as a major oil center and shifted the American balance of oil power.",
        "daily_life": "Cheap oil expanded mobility and helped fuel the transition toward automobile society."
    },
    {
        "year": "1951",
        "title": "Iranian oil nationalization",
        "lesson": "Lessons 5–7 / The Prize",
        "economy": "The conflict showed how resource control could disrupt contracts, production, and global confidence.",
        "politics": "Oil became a symbol of sovereignty and anti-colonial power.",
        "daily_life": "The effects were not just local; instability in producing regions affected consumers elsewhere."
    },
    {
        "year": "1956",
        "title": "Suez Crisis",
        "lesson": "Lessons 6–7 / The Prize",
        "economy": "The crisis exposed how vulnerable oil transportation routes were to disruption.",
        "politics": "It marked a major shift in global influence and highlighted the strategic importance of chokepoints.",
        "daily_life": "It showed that distant geopolitical conflicts could quickly shape energy security."
    },
    {
        "year": "1973",
        "title": "First Oil Shock",
        "lesson": "Lesson 9 / The Prize",
        "economy": "Production cutbacks and embargoes drove inflation, recession pressure, and a new age of shortage.",
        "politics": "Oil became an explicit geopolitical weapon.",
        "daily_life": "Gas lines, panic buying, and rising fuel costs made the crisis highly personal."
    },
    {
        "year": "1979",
        "title": "Second Oil Shock and Iranian Revolution",
        "lesson": "Lesson 10 / The Prize",
        "economy": "Fear, stockpiling, and policy confusion intensified price spikes.",
        "politics": "A domestic upheaval in Iran became a global oil crisis.",
        "daily_life": "Consumers again faced gas lines, uncertainty, and higher prices."
    },
    {
        "year": "1986",
        "title": "Third Oil Shock: price collapse",
        "lesson": "Lesson 11 / The Prize and The Quest",
        "economy": "Oversupply and weak demand pushed prices sharply downward, hurting exporters.",
        "politics": "Low prices shifted leverage toward importing nations.",
        "daily_life": "Consumers benefited from cheaper energy, but producers and oil-dependent economies suffered."
    },
    {
        "year": "1990–1991",
        "title": "Gulf Crisis and market correction",
        "lesson": "Lesson 11 / The Prize",
        "economy": "Prices spiked on fear, then fell rapidly as the market adjusted and the SPR helped calm expectations.",
        "politics": "The war showed that oil remained central to global security and coalition politics.",
        "daily_life": "The lesson was that fear itself can move markets before actual shortage fully develops."
    },
    {
        "year": "2003–2008",
        "title": "New oil shock and demand surge",
        "lesson": "Lesson 11 Epilogue / The Quest",
        "economy": "Strong demand, supply constraints, geopolitics, costs, and financial flows pushed prices sharply higher.",
        "politics": "Oil remained tied to national strategy, especially in the Middle East and emerging economies.",
        "daily_life": "High prices again transferred costs to ordinary consumers through transport and household expenses."
    },
    {
        "year": "Late course",
        "title": "Unconventional energy, natural gas, and climate policy",
        "lesson": "Lesson 12 / The Quest",
        "economy": "Technology expanded recoverable energy and changed what counted as economically available supply.",
        "politics": "Energy security, Russian gas leverage, and carbon policy became major strategic issues.",
        "daily_life": "The future of energy became a question of balancing affordability, security, and sustainability."
    },
]

PRICE_POINTS = [
    ("1973", "11.64", "First shock"),
    ("1979", "34", "Second shock"),
    ("1985", "31.75", "Pre-collapse"),
    ("1986", "10", "Third shock"),
    ("1990", "40", "Gulf spike"),
    ("1991", "20", "Post-war correction"),
    ("2003", "30", "New shock begins"),
    ("2008", "145+", "Peak before recession"),
]

# Relative bar widths for visual emphasis only
BAR_WIDTHS = {
    "1973": 8,
    "1979": 23,
    "1985": 22,
    "1986": 7,
    "1990": 28,
    "1991": 14,
    "2003": 21,
    "2008": 100,
}

def event_card(e):
    return f"""
    <div class="event-card">
        <div class="event-top">
            <div class="year">{e['year']}</div>
            <div class="lesson">{e['lesson']}</div>
        </div>
        <h3>{e['title']}</h3>
        <div class="grid-3">
            <div>
                <div class="mini-head">Global economy</div>
                <p>{e['economy']}</p>
            </div>
            <div>
                <div class="mini-head">Political dynamics</div>
                <p>{e['politics']}</p>
            </div>
            <div>
                <div class="mini-head">Everyday life</div>
                <p>{e['daily_life']}</p>
            </div>
        </div>
    </div>
    """

price_rows = []
for year, price, label in PRICE_POINTS:
    width = BAR_WIDTHS[year]
    price_rows.append(f"""
    <div class="price-row">
        <div class="price-year">{year}</div>
        <div class="bar-wrap">
            <div class="bar" style="width:{width}%"></div>
        </div>
        <div class="price-label">${price}</div>
        <div class="price-note">{label}</div>
    </div>
    """)

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Oil, Power, and Everyday Life</title>
  <style>
    body {{
      margin: 0;
      font-family: Arial, Helvetica, sans-serif;
      background: #f6f8fb;
      color: #16202a;
      line-height: 1.5;
    }}
    .page {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 32px 28px 56px;
    }}
    .hero {{
      background: linear-gradient(135deg, #ffffff 0%, #eef3fb 100%);
      border: 1px solid rgba(15,76,129,0.12);
      border-radius: 20px;
      padding: 28px;
      box-shadow: 0 10px 28px rgba(15,76,129,0.08);
      margin-bottom: 24px;
    }}
    .eyebrow {{
      color: #0F4C81;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: .06em;
      font-size: 13px;
      margin-bottom: 8px;
    }}
    h1 {{
      margin: 0 0 10px 0;
      font-size: 38px;
      color: #0F4C81;
    }}
    .subtitle {{
      font-size: 18px;
      color: #334155;
      max-width: 900px;
    }}
    .cards {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      margin: 22px 0 28px;
    }}
    .card {{
      background: white;
      border-radius: 18px;
      padding: 18px;
      border: 1px solid rgba(15,76,129,0.10);
      box-shadow: 0 6px 18px rgba(15,76,129,0.06);
    }}
    .card h2 {{
      margin: 0 0 8px 0;
      font-size: 15px;
      text-transform: uppercase;
      letter-spacing: .04em;
      color: #0F4C81;
    }}
    .big {{
      font-size: 28px;
      font-weight: 800;
      color: #0F4C81;
      margin: 4px 0 6px;
    }}
    .section {{
      margin-top: 24px;
    }}
    .section h2 {{
      color: #0F4C81;
      margin-bottom: 10px;
      font-size: 28px;
    }}
    .event-card {{
      background: white;
      border-radius: 18px;
      padding: 18px;
      border: 1px solid rgba(15,76,129,0.10);
      box-shadow: 0 6px 18px rgba(15,76,129,0.06);
      margin-bottom: 14px;
    }}
    .event-top {{
      display: flex;
      justify-content: space-between;
      gap: 16px;
      align-items: center;
      margin-bottom: 6px;
    }}
    .year {{
      font-weight: 800;
      color: #C17C00;
      font-size: 18px;
    }}
    .lesson {{
      color: #64748b;
      font-size: 13px;
    }}
    .event-card h3 {{
      margin: 0 0 12px 0;
      color: #172554;
      font-size: 22px;
    }}
    .grid-3 {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
    }}
    .mini-head {{
      font-weight: 700;
      color: #0F4C81;
      margin-bottom: 4px;
    }}
    .price-panel {{
      background: white;
      border-radius: 18px;
      padding: 20px;
      border: 1px solid rgba(15,76,129,0.10);
      box-shadow: 0 6px 18px rgba(15,76,129,0.06);
    }}
    .price-row {{
      display: grid;
      grid-template-columns: 80px 1fr 90px 160px;
      gap: 12px;
      align-items: center;
      margin: 12px 0;
    }}
    .price-year {{
      font-weight: 700;
      color: #1e293b;
    }}
    .bar-wrap {{
      width: 100%;
      height: 16px;
      background: #e8eef7;
      border-radius: 999px;
      overflow: hidden;
    }}
    .bar {{
      height: 100%;
      background: linear-gradient(90deg, #0F4C81 0%, #4f88c6 100%);
      border-radius: 999px;
    }}
    .price-label {{
      font-weight: 700;
      color: #0F4C81;
    }}
    .price-note {{
      color: #64748b;
      font-size: 14px;
    }}
    .synthesis {{
      background: #0F4C81;
      color: white;
      border-radius: 20px;
      padding: 22px 24px;
      margin-top: 26px;
    }}
    .synthesis h2 {{
      color: white;
      margin-top: 0;
    }}
    .foot {{
      color: #64748b;
      font-size: 13px;
      margin-top: 18px;
    }}
    @media (max-width: 900px) {{
      .cards, .grid-3 {{
        grid-template-columns: 1fr;
      }}
      .price-row {{
        grid-template-columns: 70px 1fr;
      }}
      .price-label, .price-note {{
        grid-column: 2;
      }}
    }}
  </style>
</head>
<body>
  <div class="page">
    <div class="hero">
      <div class="eyebrow">Unessay Artifact • Python-based data storytelling</div>
      <h1>Oil, Power, and Everyday Life</h1>
      <div class="subtitle">
        This artifact argues that major turning points in oil history repeatedly reshaped the
        global economy, political power, and the daily lives of private citizens. Across the course,
        oil never acted as “just fuel.” It functioned as a strategic resource, a financial commodity,
        a source of sovereignty, and a driver of inflation, mobility, and environmental debate.
      </div>
    </div>

    <div class="cards">
      <div class="card">
        <h2>Core pattern</h2>
        <div class="big">Shock → adaptation</div>
        <div>Each crisis pushed markets, governments, and consumers to adjust through new policy, new supply, or new technology.</div>
      </div>
      <div class="card">
        <h2>Political lesson</h2>
        <div class="big">Oil shifted power</div>
        <div>Control over oil changed the position of states, companies, and alliances from the early concessions era through OPEC and beyond.</div>
      </div>
      <div class="card">
        <h2>Daily life lesson</h2>
        <div class="big">Consumers felt it directly</div>
        <div>Gas lines, inflation, transport costs, suburban lifestyles, efficiency standards, and energy anxiety all tied private life to global oil history.</div>
      </div>
    </div>

    <div class="section">
      <h2>Major Course Turning Points</h2>
      {''.join(event_card(e) for e in EVENTS)}
    </div>

    <div class="section">
      <h2>Illustrative Price Shock Story</h2>
      <div class="price-panel">
        <p>
          These benchmark figures come directly from course material emphasized in the lessons.
          They show that oil history is not a smooth upward march. It is a sequence of shocks,
          panics, collapses, and corrections shaped by geopolitics, expectations, and market structure.
        </p>
        {''.join(price_rows)}
      </div>
    </div>

    <div class="synthesis">
      <h2>Final Synthesis</h2>
      <p>
        Over the semester, the course showed that the history of oil is really the history of
        modern power. Oil influenced war strategy, national sovereignty, inflation, market structure,
        consumer behavior, and climate policy. Fears of “running out” repeatedly appeared, but the
        course also emphasized that reserves are a moving target shaped by technology, price, and access.
        In the final lessons, unconventional oil, natural gas, and carbon markets added a new dimension:
        the future of energy is not simply about replacing oil, but about balancing security, affordability,
        environmental cost, and technological change.
      </p>
      <p>
        The central takeaway is that oil’s importance has persisted because it sits at the intersection
        of economics, politics, infrastructure, and everyday life. That is why the subject remained
        relevant from Pennsylvania in 1859 to OPEC, the Gulf War, unconventional energy, and the
        climate-era debates covered at the end of the course.
      </p>
    </div>

    <div class="foot">
      Built with Python to create a static HTML artifact for the Unessay project.
    </div>
  </div>
</body>
</html>
"""

out_path = Path("oil_unessay_artifact.html")
out_path.write_text(html, encoding="utf-8")
print(f"Created: {out_path.resolve()}")
