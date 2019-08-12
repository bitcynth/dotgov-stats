from dgs import app, list_mgr
from flask import render_template, request, redirect

@app.route('/')
def index():
    if 'domain' in request.args:
        return redirect('/r/' + request.args['domain'])
    return render_template('index.html')

@app.route('/r/<domain>')
def report(domain):
    domain = domain.lower()
    if not domain in list_mgr.domains:
        return render_template('report.html', domain=domain, valid=False)
    report_email = None
    if domain in list_mgr.list_of_contacts:
        report_email = list_mgr.list_of_contacts[domain]
    return render_template('report.html', domain=domain, report_email=report_email)