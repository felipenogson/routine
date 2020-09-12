from flask import Blueprint, render_template, jsonify, request, flash, redirect, url_for
from r_help import til_random, affirmations


routine = Blueprint('routine', __name__, template_folder='templates', static_folder='static')


from project import Message, mail


@routine.route('/')
def index():
    return render_template('index.html')


@routine.route("/contact", methods=['GET', 'POST'])
def contact():
    """TODO: Docstring for contact.
    :returns: Serves contact page
    """
    if request.method == "POST":
        # app.logger.warning(request.form['email'])
        msg = Message("Este es un mensaje desde RUTINA by felipon", sender='services@nogson.com', recipients=['felipe@nogson.com'])
        msg.body = f'{request.form["email"]} : {request.form["message"]} '
        flash('Message Sended')
        mail.send(msg)
        return redirect(url_for('routine.index'))
    return render_template('contact.html', name="Contact")


@routine.route("/til")
def til():
    quote = til_random()
    return jsonify(quote)


@routine.route("/affirmations")
def affirmation():
    """ Un api para la aplicacion le mandamos una afirmacion.
    :returns:
    """
    return jsonify(affirmations())
