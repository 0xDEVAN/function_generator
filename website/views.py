from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from utility_functions import function_generator

views = Blueprint('views', __name__)

@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("notes.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/written_programs', methods=['GET', 'POST'])
@login_required
def programs():
    if request.method == 'POST':
        prog = request.form.get('prog')

        if len(prog) < 1:
            flash('Program is too short!', category='error')
        else:
            new_prog = Prog(data=prog, user_id=current_user.id)
            db.session.add(new_prog)
            db.session.commit()
            flash('Program added!', category='success')

    return render_template("written_programs.html", user=current_user)

@views.route("/create")
def create_program():
    if request.method == 'POST':
        prog = request.form.get('prog')

        if len(prog) < 1:
            flash('Program is too short!', category='error')
        else:
            new_prog = Prog(data=prog, user_id=current_user.id)
            db.session.add(new_prog)
            db.session.commit()
            flash('Program added!', category='success')
    
    return render_template("written_programs.html", user=current_user)

@views.route('/run')
def run_my_func(name):
    return name

@views.route('/update')
def update_my_func(name):
    return name

@views.route('/delete_prog', methods=['POST'])
def delete_my_prog(name):
    prog = json.loads(name.data)
    progID = prog['progID']
    prog = Prog.query.get(progID)
    if prog:
        if prog.user_id == current_user.id:
            db.session.delete(prog)
            db.session.commit()
    return jsonify({})
