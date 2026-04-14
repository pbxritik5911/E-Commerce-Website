"""
Project: Contact Management System
Name: Ritik Sharma
Date: 2026
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage
contacts = []

# Home Route (READ)
@app.route('/')
def index():
    query = request.args.get('search')
    if query:
        filtered = [c for c in contacts if query.lower() in c['name'].lower() or query in c['phone']]
        return render_template('index.html', contacts=filtered)
    return render_template('index.html', contacts=contacts)

# Add Contact (CREATE)
@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        if not name or not phone or not email:
            return "All fields are required!"

        contacts.append({
            'id': len(contacts),
            'name': name,
            'phone': phone,
            'email': email
        })

        return redirect(url_for('index'))

    return render_template('add_contact.html')

# Edit Contact (UPDATE)
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):
    contact = next((c for c in contacts if c['id'] == id), None)

    if request.method == 'POST':
        contact['name'] = request.form['name']
        contact['phone'] = request.form['phone']
        contact['email'] = request.form['email']
        return redirect(url_for('index'))

    return render_template('edit_contact.html', contact=contact)

# Delete Contact (DELETE)
@app.route('/delete/<int:id>')
def delete_contact(id):
    global contacts
    contacts = [c for c in contacts if c['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)