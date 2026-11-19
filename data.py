"""Edit this file to change gym content. No database needed."""

SERVICES = [
    {"icon": "🏋️", "name": "Strength Training", "text": "Full free-weight floor, power racks and platforms with coach guidance."},
    {"icon": "🧑‍🏫", "name": "Personal Training", "text": "One-to-one plans built around your goal, with weekly progress checks."},
    {"icon": "🔥", "name": "HIIT & CrossFit", "text": "45-minute group sessions, capped at 12 people so coaches can correct form."},
    {"icon": "🧘", "name": "Yoga & Mobility", "text": "Morning and evening classes for flexibility, recovery and posture."},
    {"icon": "🥗", "name": "Diet Consultation", "text": "Meal plans from a certified nutritionist, adjusted every 4 weeks."},
    {"icon": "🏃", "name": "Cardio Zone", "text": "Treadmills, rowers, air bikes and ellipticals with a 12-minute wait cap at peak."},
    {"icon": "💃", "name": "Zumba & Dance", "text": "High-energy dance classes, no experience needed."},
    {"icon": "🧊", "name": "Steam & Recovery", "text": "Steam room and stretch area open to all Premium and Elite members."},
]

PLANS = [
    {"name": "Starter", "price": 1499, "period": "month", "featured": False,
     "features": ["Gym floor access", "Cardio zone", "Locker room", "1 free fitness assessment"]},
    {"name": "Premium", "price": 3999, "period": "3 months", "featured": True,
     "features": ["Everything in Starter", "Group classes (HIIT, Yoga, Zumba)", "Steam room", "Diet chart"]},
    {"name": "Elite", "price": 12999, "period": "year", "featured": False,
     "features": ["Everything in Premium", "8 personal training sessions", "Monthly body analysis", "10% off supplements"]},
]

TRAINERS = [
    {"name": "Rohit Malik", "role": "Head Strength Coach", "bio": "10 years coaching powerlifting and body recomposition."},
    {"name": "Neha Arora", "role": "Yoga & Mobility", "bio": "RYT-500 certified, focused on injury recovery."},
    {"name": "Karan Singh", "role": "HIIT & Conditioning", "bio": "Former state-level athlete, runs our 6 AM batch."},
]

SUPPLEMENTS = [
    {"name": "Whey Protein Isolate", "brand": "IronNest Labs", "category": "Protein", "price": 3499, "size": "1 kg",
     "icon": "🥛", "text": "25 g protein per scoop, low lactose, chocolate or vanilla."},
    {"name": "Mass Gainer", "brand": "IronNest Labs", "category": "Protein", "price": 2799, "size": "3 kg",
     "icon": "💪", "text": "Calorie-dense blend for lean bulking."},
    {"name": "Creatine Monohydrate", "brand": "PureForm", "category": "Performance", "price": 999, "size": "250 g",
     "icon": "⚡", "text": "Micronized, unflavoured, 3 g daily dose."},
    {"name": "Pre-Workout", "brand": "PureForm", "category": "Performance", "price": 1599, "size": "300 g",
     "icon": "🔥", "text": "Caffeine and citrulline for focus and pumps."},
    {"name": "BCAA 2:1:1", "brand": "PureForm", "category": "Recovery", "price": 1299, "size": "250 g",
     "icon": "💧", "text": "Sip during training to support recovery."},
    {"name": "Omega-3 Fish Oil", "brand": "VitaCore", "category": "Wellness", "price": 799, "size": "90 softgels",
     "icon": "🐟", "text": "Heart and joint support, 1000 mg per capsule."},
    {"name": "Multivitamin", "brand": "VitaCore", "category": "Wellness", "price": 649, "size": "60 tablets",
     "icon": "🍊", "text": "Daily micronutrient cover for active people."},
    {"name": "Protein Bars (box of 12)", "brand": "IronNest Labs", "category": "Snacks", "price": 1099, "size": "12 bars",
     "icon": "🍫", "text": "20 g protein, no added sugar."},
]
