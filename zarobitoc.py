from flask import Flask, render_template, request, redirect
from sxemochka import Game
from db import Base, engine, SessionLocal
app = Flask(__name__)
Base.metadata.create_all(bind=engine)
@app.route('/')
def domic():
    session = SessionLocal()
    games = session.query(Game).all()
    session.close
    return render_template('domic.html', games=games)
@app.route('/add', methods=['POST', 'GET'])
def add_game():
    if request.method == 'POST':
        session = SessionLocal()
        new_game = Game(
            name= request.form['name'],
            description=request.form['description'],
            price=request.form['price']
        )
        session.add(new_game)
        session.commit()
        session.close()
        return redirect('/')
    return render_template('add_game.html')

if __name__ == '__main__':
    app.run(debug=True)