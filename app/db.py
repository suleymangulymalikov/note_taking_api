from datetime import datetime, timedelta

from app.models import Note

now = datetime.now()

notes_db: list[Note] = [
    Note(id=1, title="Morning Routine", content="Wake up, water, stretch 5 min.", tags=["health","habit"], created_at=now - timedelta(days=30), updated_at=now - timedelta(days=30)),
    Note(id=2, title="Grocery List", content="Milk, eggs, bread, tomatoes.", tags=["shopping","home"], created_at=now - timedelta(days=29), updated_at=now - timedelta(days=29)),
    Note(id=3, title="Project Idea", content="Minimal note app with offline sync.", tags=["coding","idea"], created_at=now - timedelta(days=28), updated_at=now - timedelta(days=28)),
    Note(id=4, title="Workout Plan", content="Pushups and squats 3 sets.", tags=["fitness"], created_at=now - timedelta(days=27), updated_at=now - timedelta(days=27)),
    Note(id=5, title="Book Quotes", content="Consistency beats motivation.", tags=["books","quotes"], created_at=now - timedelta(days=26), updated_at=now - timedelta(days=26)),
    Note(id=6, title="Travel Wishlist", content="Japan, Iceland, Norway.", tags=["travel"], created_at=now - timedelta(days=25), updated_at=now - timedelta(days=25)),
    Note(id=7, title="Meeting Notes", content="Add dark mode feature.", tags=["work"], created_at=now - timedelta(days=24), updated_at=now - timedelta(days=24)),
    Note(id=8, title="Pasta Recipe", content="Boil pasta, tomato sauce.", tags=["food","recipe"], created_at=now - timedelta(days=23), updated_at=now - timedelta(days=23)),
    Note(id=9, title="Movies", content="Watch sci-fi classics.", tags=["movies"], created_at=now - timedelta(days=22), updated_at=now - timedelta(days=22)),
    Note(id=10, title="Weekend Plans", content="Bike ride and coffee.", tags=["personal"], created_at=now - timedelta(days=21), updated_at=now - timedelta(days=21)),
 
    Note(id=11, title="Learning Goals", content="Practice FastAPI.", tags=["learning","coding"], created_at=now - timedelta(days=20), updated_at=now - timedelta(days=20)),
    Note(id=12, title="Security Note", content="Use password manager.", tags=["security"], created_at=now - timedelta(days=19), updated_at=now - timedelta(days=19)),
    Note(id=13, title="UI Idea", content="Glassmorphism cards.", tags=["design"], created_at=now - timedelta(days=18), updated_at=now - timedelta(days=18)),
    Note(id=14, title="Budget", content="Track expenses weekly.", tags=["finance"], created_at=now - timedelta(days=17), updated_at=now - timedelta(days=17)),
    Note(id=15, title="Podcast Ideas", content="AI future jobs.", tags=["ideas"], created_at=now - timedelta(days=16), updated_at=now - timedelta(days=16)),
    Note(id=16, title="Random Thought", content="Music feels different at night.", tags=["thoughts"], created_at=now - timedelta(days=15), updated_at=now - timedelta(days=15)),
    Note(id=17, title="Language Practice", content="10 Spanish words daily.", tags=["learning"], created_at=now - timedelta(days=14), updated_at=now - timedelta(days=14)),
    Note(id=18, title="Birthday Reminder", content="Buy gift before Friday.", tags=["reminder"], created_at=now - timedelta(days=13), updated_at=now - timedelta(days=13)),
    Note(id=19, title="Debugging", content="Missing header caused error.", tags=["coding","bug"], created_at=now - timedelta(days=12), updated_at=now - timedelta(days=12)),
    Note(id=20, title="Reading List", content="Read 2 chapters daily.", tags=["books"], created_at=now - timedelta(days=11), updated_at=now - timedelta(days=11)),

    Note(id=21, title="App Features", content="Markdown preview.", tags=["product"], created_at=now - timedelta(days=10), updated_at=now - timedelta(days=10)),
    Note(id=22, title="Meditation", content="10 min breathing.", tags=["mindfulness"], created_at=now - timedelta(days=9), updated_at=now - timedelta(days=9)),
    Note(id=23, title="Music Practice", content="Chord progression G major.", tags=["music"], created_at=now - timedelta(days=8), updated_at=now - timedelta(days=8)),
    Note(id=24, title="Tech Shopping", content="Ergonomic keyboard.", tags=["tech","shopping"], created_at=now - timedelta(days=7), updated_at=now - timedelta(days=7)),
    Note(id=25, title="HTTP Notes", content="200 OK, 404 Not Found.", tags=["study","tech"], created_at=now - timedelta(days=6), updated_at=now - timedelta(days=6)),
    Note(id=26, title="Reflection", content="Productive day.", tags=["journal"], created_at=now - timedelta(days=5), updated_at=now - timedelta(days=5)),
    Note(id=27, title="Cleaning Tasks", content="Clean desk.", tags=["home"], created_at=now - timedelta(days=4), updated_at=now - timedelta(days=4)),
    Note(id=28, title="Startup Idea", content="AI article summarizer.", tags=["startup"], created_at=now - timedelta(days=3), updated_at=now - timedelta(days=3)),
    Note(id=29, title="Health Reminder", content="Stand every hour.", tags=["health"], created_at=now - timedelta(days=2), updated_at=now - timedelta(days=2)),
    Note(id=30, title="Night Routine", content="No screens before sleep.", tags=["sleep","habit"], created_at=now - timedelta(days=1), updated_at=now - timedelta(days=1)),
]
