# IronNest Fitness (Flask)

Gym website with services, membership plans, coaches, supplements store and a trial-booking form.

## Structure
```
gym_website/
├── app.py            # routes
├── data.py           # all content (services, plans, supplements): edit here
├── requirements.txt  # Flask + gunicorn
├── Procfile          # Heroku/Railway start command
├── render.yaml       # Render blueprint
├── templates/        # base, index, services, supplements, contact, 404, _product
└── static/           # css/style.css, js/main.js
```

## Run locally
```
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py                 # http://127.0.0.1:5000
```

## Deploy (Render, free tier)
1. Push this folder to GitHub.
2. Render > New > Web Service > connect repo.
3. Build: `pip install -r requirements.txt`   Start: `gunicorn app:app`
4. Add env var `SECRET_KEY` (any long random string).

Railway and Heroku work with the included `Procfile`.
Note: `messages.csv` is lost on redeploy on free hosts; use a database or email service for production.
