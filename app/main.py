from flask import Flask, render_template, session, redirect, request
import requests
import json
from pyrebase import pyrebase

app = Flask(__name__)

config = {
    'apiKey': "AIzaSyDbljd-nk01eBY2-KqKPP84Uydquc3MZXQ",
    'authDomain': "auth-myflix.firebaseapp.com",
    'projectId': "auth-myflix",
    'storageBucket': "auth-myflix.appspot.com",
    'messagingSenderId': "647646447282",
    'appId': "1:647646447282:web:3fe02f795b00da98dbabab",
    'measurementId': "G-Z274PKD11W",
    'databaseURL' : ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key = "secret"
app.debug = True

catalogue_url = "35.233.78.186"
store_url = "35.210.137.140"

@app.route('/')
def index_page():
    return redirect('/home')

@app.route('/home', methods = ['POST', 'GET'])
def home_page():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if request.form.get('type') == 'login':
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                session['user'] = email
            except:
                return "Failed to login."
            else:
                return redirect('/films')
        if request.form.get('type') == 'register':
            try:
                user = auth.create_user_with_email_and_password(email, password)
                session['user'] = email
            except:
                return "Failed to register."
            else:
                return redirect('/films')

    return render_template("index.html")

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')

@app.route('/films')
def films_page():
    if not ('user' in session):
        return redirect('/home')
    uuid = []
    posters = []
    titles = []
    categories = []
    sections = []

    url = "http://" + catalogue_url + "/myflix/videos?filter={%22$and%22:[{%22video.category%22:%22action%22},{%22video.type%22:%22film%22}]}"
    sections.append("action")

    headers = {}
    payload = json.dumps({ })
    response = requests.get(url)
    #print (response)
    # exit if status code is not ok
    print ("Response:")
    print (response)
    print ("Response Code:")
    print (response.status_code)
    if response.status_code != 200:
      print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
      return "Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message'])

    jResp = response.json()
    print ("Response JSON:")
    print (type(jResp))
    for index in jResp:
        print ("----------------")
        for key in index:

            if (key !="_id"):
                print (index[key])
                for key2 in index[key]:
                    print (key2,index[key][key2])
                    if (key2=="Name"):
                        titles.append(index[key][key2])
                    if (key2=="pic"):
                        posters.append(index[key][key2])
                    if (key2=="uuid"):
                        uuid.append(index[key][key2])
                    if (key2=="category"):
                        categories.append((', '.join(index[key][key2])))
                    if (key2=="type"):
                        genre = index[key][key2]


    url = "http://" + catalogue_url + "/myflix/videos?filter={%22$and%22:[{%22video.category%22:%22fantasy%22},{%22video.type%22:%22film%22}]}"
    sections.append("fantasy")

    headers = {}
    payload = json.dumps({ })
    response = requests.get(url)
    #print (response)
    # exit if status code is not ok
    print ("Response:")
    print (response)
    print ("Response Code:")
    print (response.status_code)
    if response.status_code != 200:
      print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
      return "Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message'])

    jResp = response.json()
    print ("Response JSON:")
    print (type(jResp))
    for index in jResp:
        print ("----------------")
        for key in index:

            if (key !="_id"):
                print (index[key])
                for key2 in index[key]:
                    print (key2,index[key][key2])
                    if (key2=="Name"):
                        titles.append(index[key][key2])
                    if (key2=="pic"):
                        posters.append(index[key][key2])
                    if (key2=="uuid"):
                        uuid.append(index[key][key2])
                    if (key2=="category"):
                        categories.append((', '.join(index[key][key2])))
                    if (key2=="type"):
                        genre = index[key][key2]
    
    return render_template("display.html", server=store_url, type0 = genre, section0=sections[0], title0=titles[0], title1=titles[1], title2=titles[2], poster0=posters[0], poster1=posters[1], poster2=posters[2], uuid0=uuid[0], uuid1=uuid[1], uuid2=uuid[2], category0=categories[0], category1=categories[1], category2=categories[2], section1=sections[1], title3=titles[3], title4=titles[4], title5=titles[5], poster3=posters[3], poster4=posters[4], poster5=posters[5], uuid3=uuid[3], uuid4=uuid[4], uuid5=uuid[5], category3=categories[3], category4=categories[4], category5=categories[5])

@app.route('/shows')
def shows_page():
    if not ('user' in session):
        return redirect('/home')
    
    uuid = []
    posters = []
    titles = []
    categories = []
    sections = []

    url = "http://" + catalogue_url + "/myflix/videos?filter={%22$and%22:[{%22video.category%22:%22action%22},{%22video.type%22:%22show%22}]}"
    sections.append("action")
    headers = {}
    payload = json.dumps({ })
    response = requests.get(url)
    print ("Response:")
    print (response)
    print ("Response Code:")
    print (response.status_code)
    if response.status_code != 200:
        print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
        return "Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message'])

    jResp = response.json()
    print ("Response JSON:")
    print (type(jResp))
    for index in jResp:
        print ("----------------")
        for key in index:

            if (key !="_id"):
                print (index[key])
                for key2 in index[key]:
                    print (key2,index[key][key2])
                    if (key2=="Name"):
                        titles.append(index[key][key2])
                    if (key2=="pic"):
                        posters.append(index[key][key2])
                    if (key2=="uuid"):
                        uuid.append(index[key][key2])
                    if (key2=="category"):
                        categories.append((', '.join(index[key][key2])))
                    if (key2=="type"):
                        genre = index[key][key2]

    url = "http://" + catalogue_url + "/myflix/videos?filter={%22$and%22:[{%22video.category%22:%22fantasy%22},{%22video.type%22:%22show%22}]}"
    sections.append("fantasy")

    headers = {}
    payload = json.dumps({ })
    response = requests.get(url)
    print ("Response:")
    print (response)
    print ("Response Code:")
    print (response.status_code)
    if response.status_code != 200:
      print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
      return "Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message'])

    jResp = response.json()
    print ("Response JSON:")
    print (type(jResp))
    for index in jResp:
        print ("----------------")
        for key in index:

            if (key !="_id"):
                print (index[key])
                for key2 in index[key]:
                    print (key2,index[key][key2])
                    if (key2=="Name"):
                        titles.append(index[key][key2])
                    if (key2=="pic"):
                        posters.append(index[key][key2])
                    if (key2=="uuid"):
                        uuid.append(index[key][key2])
                    if (key2=="category"):
                        categories.append((', '.join(index[key][key2])))
                    if (key2=="type"):
                        genre = index[key][key2]
    
    return render_template("display.html", server=store_url, type0 = genre, section0=sections[0], title0=titles[0], title1=titles[1], title2=titles[2], poster0=posters[0], poster1=posters[1], poster2=posters[2], uuid0=uuid[0], uuid1=uuid[1], uuid2=uuid[2], category0=categories[0], category1=categories[1], category2=categories[2], section1=sections[1], title3=titles[3], title4=titles[4], title5=titles[5], poster3=posters[3], poster4=posters[4], poster5=posters[5], uuid3=uuid[3], uuid4=uuid[4], uuid5=uuid[5], category3=categories[3], category4=categories[4], category5=categories[5])

@app.route('/videos/<uuid>')
def video_page(uuid):
    if not ('user' in session):
        return redirect('/home')

    url = "http://35.233.78.186/myflix/videos?filter={%22video.uuid%22:%22" + uuid + "%22}"
    headers = {}
    payload = json.dumps({ })
    response = requests.get(url)

    print ("Response:")
    print (response)
    print ("Response Code:")
    print (response.status_code)
    if response.status_code != 200:
        print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
        return "Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message'])
    
    jResp = response.json()
    print ("Response JSON:")
    print (type(jResp))
    for index in jResp:
       print ("----------------")
       for key in index:

           if (key !="_id"):
              print (index[key])
              for key2 in index[key]:
                    print (key2,index[key][key2])
                    if (key2=="pic"):
                        poster=index[key][key2]
                    if (key2=="file"):
                        file=index[key][key2]
                    if (key2=="Name"):
                        name=index[key][key2]

    return render_template("video.html", title0=name, video0=file)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port="80")