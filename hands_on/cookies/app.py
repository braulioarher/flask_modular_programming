from flask import Flask, make_response, request

app = Flask(__name__)



# use the route '/setcookie/' to set cookie
@app.route('/setcookie/')
def setcookie():
  vist_count = 1
  resp = make_response('cookie was successfully set')
  resp.set_cookie('holacookie', str(vist_count))
  return resp

# use the route '/getcookie/' to get cookie
@app.route('/getcookie/')
def getcookie():
  count = request.cookies.get('holacookie')
  inc = make_response('you visited this site {} times'.format(str(count)))
  nc = int(count) + 1
  inc.set_cookie('holacookie', str(nc))
  return(inc)
