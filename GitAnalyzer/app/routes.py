from app import app
from flask import request, render_template
from .Scrap import *

@app.route('/')
def index():
    user = request.args.get('username')
    type = request.args.get('type')
    textProfile = "<title>" + str(user) + " - " +  str(type)  + "</title>" + "<body style='text-align:center; letter-spacing: 3px; background: #616161; color: #fff'><h1 style='padding: 1.8%; font-size: 30px;'>" + str(user) + " - " +  str(type) + "</h1>"
    textData = "<title>" + str(user) + " - " +  str(type)  + "</title>" + "<body style='text-align:center; letter-spacing: 3px; background: #616161; color: #fff'><h1 style='padding: 1.8%; font-size: 30px;'>" + str(user) + " - " +  str(type) + "</h1>"
    if user:
        if type=="Profile":
            data = UserProfile(user)    
            main = dict()
            for i in data[1:len(data) - 1].split(','):
                if i.split(':')[1] == 'null':
                    pass
                else:
                    main[i.split(':')[0].strip('"')] = str(i.split(':')[1:]).strip('[').strip(']').strip("'").strip('"').replace("'","",2)


            textProfile += """
                    <table style='font-family: \"Trebuchet MS\", Arial, Helvetica; width: 60%; margin-left: 20%; text-align: left; border-collapse: collapse; background: #ddffdd;'>
                        <tr style='background: #4caf50; color: #fff;'>
                            <th style='padding: 16px; border: 1px solid #ddd;'>Key</th>
                            <th style='padding: 16px; border: 1px solid #ddd;'>Value</th>
                        </tr>"""
                        
            for key, value in main.items():
                textProfile += "<tr style='color: #000'> <td style='padding: 16px; border: 1px solid #ddd;'>" + key + "</td> <td style='padding: 16px; border: 1px solid #ddd;'>" + value + "</td> </tr>"
            textProfile += "</table></body>"
            return textProfile
            #return render_template('view.html', data = data)


        elif type=="Data":
            data_main = UserDetail(user)
            for data in data_main:
                print(data)
                main = dict()
                for key,value in data.items():
                    main[key] = value

                textData += """<table style='font-family: \"Trebuchet MS\", Arial, Helvetica; width: 60%; margin-left: 20%; text-align: left; border-collapse: collapse; background: #ddffdd;'>
                        <tr style='background: #4caf50; color: #fff;'>
                            <th style='padding: 16px; border: 1px solid #ddd;'>Key</th>
                            <th style='padding: 16px; border: 1px solid #ddd;'>Value</th>
                        </tr>"""
                        
                for key, value in main.items():
                    textData += "<tr style='color: #000'> <td style='padding: 16px; border: 1px solid #ddd;'>" + key + "</td> <td style='padding: 16px; border: 1px solid #ddd;'>" + value + "</td> </tr>"
                textData += "</table></body>"
            return textData

    else:
        return render_template("index.html")
