from flask import render_template, request, redirect, url_for, flash
from src import app, db
from src.models import Note

@app.route('/')
def index():
    """
    Handles the root path request. Fetches all notes from 
    the database and renders them using the `index.html` template.
    
    Returns:
        Rendered HTML template for the index page including the list of notes.
    """

    notes = Note.query.all()

    return render_template('index.html', notes=notes)


@app.route('/add', methods=['POST'])
def add_note():
    """
    Handles the addition of a new note. Retrieves note content from the form and saves it to the database.
    
    Returns:
        Redirect to the index page to display all notes including the newly added note.
    """

    content = request.form.get('content') # input text
    if content:
        new_note = Note(content=content)
        # db.create_all()  # Ensure the database and tables exist
        db.session.add(new_note)
        db.session.commit()

    return redirect(url_for('index'))

@app.route('/delete/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    """
    Deletes a note identified by `note_id` from the database.

    Args:
        note_id (int): The unique identifier of the note to be deleted.
    
    Returns:
        Redirect to the index route after the note has been deleted.
    """
    print(f"[DEBUG] note_id = {note_id}")
    note_to_delete = Note.query.get_or_404(note_id)
    db.session.delete(note_to_delete)
    db.session.commit()

    return {'message': 'Note successfully deleted!'}, 200
