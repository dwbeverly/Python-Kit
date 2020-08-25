import webbrowser

###################################
# Open browser to localhost:port  #
###################################

# I use this with docker containers running web apps
docker_port = 80

def test_web_container():
    webbrowser.open('http://localhost:{docker_port}', new=2)