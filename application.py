from flask import Flask, render_template, request, redirect, url_for

# import my stuff
from storage import Archive
from forms import StoryForm

# EB looks for an 'application' callable by default.
app = Flask(__name__)
app.config.from_object('config')

# interface to create shareble story pages
@app.route('/')
def index():
    ## some intro
    # a form to create stories
    form = StoryForm()
    return render_template('index.html', form=form)

# page that renders the fake stories
# uses the Archive class to render the page from JSON file
@app.route('/story', methods=['POST'])
@app.route('/story/<story_id>', methods=['GET'])
def story(story_id=None):
    form = StoryForm(request.form)
    if request.method == 'POST':
        if form.validate():
            story = Archive().write_story(form.data)
            return redirect(url_for('story') + '/' + story['id'],)
            #return render_template('story.html', story=story)
        else:
            return redirect(url_for('index'))

    #sid = str(request.args.get('id'))
    story_exists, story = Archive().read_story(story_id)
    if story_exists:
        return render_template('story.html', story=story)
    else:
        return redirect(url_for('index'))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()
