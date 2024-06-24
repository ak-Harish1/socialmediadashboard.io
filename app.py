from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

accounts = []  # This will store our accounts
scheduled_posts = []  # This will store our scheduled posts

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/manage_accounts', methods=['GET', 'POST'])
def manage_accounts():
    if request.method == 'POST':
        platform = request.form['platform']
        username = request.form['username']
        accounts.append({'platform': platform, 'username': username})
        return redirect(url_for('manage_accounts'))
    return render_template('manage_accounts.html', accounts=accounts)

@app.route('/post_scheduler', methods=['GET', 'POST'])
def post_scheduler():
    if request.method == 'POST':
        content = request.form['content']
        platform = request.form['platform']
        schedule_time = datetime.strptime(request.form['schedule_time'], '%Y-%m-%dT%H:%M')
        scheduled_posts.append({
            'content': content,
            'platform': platform,
            'schedule_time': schedule_time
        })
        return redirect(url_for('post_scheduler'))
    return render_template('post_scheduler.html', accounts=accounts, scheduled_posts=scheduled_posts)

if __name__ == '__main__':
    app.run(debug=True)