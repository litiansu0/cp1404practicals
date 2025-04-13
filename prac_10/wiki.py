from flask import Flask, render_template, request, redirect, url_for, session
import wikipedia

app = Flask(__name__)
app.secret_key = 'replace-this-with-a-secret-key'

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        session['search_term'] = request.form['search']
        return redirect(url_for('results'))
    return render_template("search.html")

@app.route('/results')
def results():
    search_term = session.get('search_term')
    if not search_term:
        return redirect(url_for('search'))
    page = get_page(search_term)
    return render_template("results.html", page=page)

def get_page(search_term):
    try:
        page = wikipedia.page(search_term, auto_suggest=False)
        summary = wikipedia.summary(search_term, auto_suggest=False)
        return {
            'status': 'ok',
            'title': page.title,
            'summary': summary,
            'url': page.url
        }
    except wikipedia.exceptions.PageError:
        return {
            'status': 'error',
            'message': f'Page id "{search_term}" does not match any pages. Try another id!'
        }
    except wikipedia.exceptions.DisambiguationError as e:
        return {
            'status': 'disambiguation',
            'message': "We need a more specific title. Try one of the following:",
            'options': e.options[:5]  # show first few options
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f"Unexpected error: {e}"
        }

if __name__ == '__main__':
    app.run(debug=True)
