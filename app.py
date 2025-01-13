from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

nav_config = {
    "main_links": [
        {"name": "Home",
         "url": "home",
         "type": "route"},

        {"name": "About",
         "url": "about",
         "type": "route"},
        {
            "name": "Team",
            "url": "/team",
            "type": "dropdown",
            "children": [
                {"name": "FTC", "url": "/team/ftc"},
                {"name": "FRC", "url": "/team/frc"}
            ]
        },
        {"name": "Robots",
         "url": "robots",
         "type": "route"},

        {"name": "Contact",
         "url": "contact",
         "type": "route"}
    ]
}

# team data, called by team_info in html
ftc_info = {
    "team_number": "23785",
    "team_name": "Orion Robotics",
    "current_competition": "First Technical Challenge 2024",
    "achievements": [
        "Regional Winners 2023",
        "Innovation Award 2022",
        "Engineering Excellence 2021"
    ]
}

# team data, called by team_info in html
frc_info = {
    "team_number": "1810",
    "team_name": "Catatronics",
    "current_competition": "First Robotics Competition 2025",
    "achievements": [
        "First Control Award 2024"
    ]
}

index_info = {
    "team_number": "23785, 1810, 9316",
    "team_name": "Orion Robotics, Catatronics, Cubatronics",
    "current_competition": "First Technical Challenge 2024, First Robotics Competition 2025",
    "achievements": [
        "Regional Winners 2023",
        "Innovation Award 2022",
        "Engineering Excellence 2021",
        "First Control Award 2024"
    ]
}


@app.context_processor
def utility_processor():
    return dict(nav_config=nav_config)

@app.route('/')
def home():
    return render_template('index.html',
                         team_info=index_info,
                         current_year=datetime.now().year)

@app.route('/about')
def about():
    return render_template('about.html',
                           team_info=ftc_info,
                           current_year=datetime.now().year)

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/robots')
def robots():
    return render_template('robots.html')

@app.route('/team/ftc')
def ftc():
    return render_template('ftc.html',
                        team_info=ftc_info,
                        current_year=datetime.now().year)

@app.route('/team/frc')
def frc():
    return render_template('frc.html',
                           team_info=frc_info,
                           current_year=datetime.now().year)

@app.route("/contact")
def contact():
    return render_template('contact.html',
                           current_year=datetime.now().year)


if __name__ == '__main__':
    app.run(debug=True)
