from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import madlibs_stories


app = Flask(__name__,
            template_folder= 'templates',
            static_folder='static')

app.config['SECRET_KEY'] = 'oh-so-secret'

debug = DebugToolbarExtension(app)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def home():
    """ Render the Homepage with a list of madlibs stories"""
    return render_template('home.html', stories = madlibs_stories)

@app.route('/submit_story')
def submit_story():
    """Render the form to submit words for a selected Madlibs story."""
    s_name = request.args.get('story')
    story = madlibs_stories.get(request.args.get('story'))
    words = story.prompts
    return render_template("submit_story.html", prompts = words, hidden_query = s_name )
    

@app.route('/show_story') 
def show_story():
    """Render the completed Madlibs story based on user inputs."""
    story = madlibs_stories.get(request.args.get('story_id'))
    words = story.prompts

    ans = {word: request.args.get(f'{word}') for word in words}

    completed_story = story.generate(ans)

    return render_template('show_story.html', result = completed_story)



