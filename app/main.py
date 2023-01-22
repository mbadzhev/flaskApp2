from flask import Flask, render_template
import requests
import json
import re

app = Flask(__name__)

app.debug = True

title1 = "My Title"
h1 = "h1 or something"

catalogue_url = "35.233.78.186"
store_url = "35.210.137.140"

@app.route('/')
def home_page():
    return render_template("films.html")

@app.route('/films')
def films_page():
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

@app.route('/db')
def hello_world():
    url = "http://" + catalogue_url + "/myflix/videos"
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
    html="<h2> Your Videos</h2>"
    for index in jResp:
       #print (json.dumps(index))
       print ("----------------")
       for key in index:

           if (key !="_id"):
              print (index[key])
              for key2 in index[key]:
                  print (key2,index[key][key2])
                  if (key2=="Name"):
                      name=index[key][key2]
                  if (key2=="thumb"):
                      thumb=index[key][key2]
                  if (key2=="uuid"):
                      uuid=index[key][key2]  
            #   html=html+'<h3>'+name+'</h3>'
            #   ServerIP=request.host.split(':')[0]
            #   html=html+'<a href="http://'+ServerIP+'/Video/'+uuid+'">'
            #   html=html+'<img src="http://35.228.145.155/pics/'+thumb+'">'
            #   html=html+"</a>"        
            #   print("=======================")

    return "hello"

@app.route('/videos/<uuid>')
def video_page(uuid):
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

    return render_template("video.html", title0=name, video0="boom.mp4")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port="80")