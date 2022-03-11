import enum
from flask import Flask, jsonify
import sys, os, requests, json
from more_itertools import strip

app = Flask(__name__)

@app.route('/spare-parts/api/<PageNumber>')
def SpareParts(PageNumber):
    Page = None
    try:
        Page = int(PageNumber)
    except:
        return "The entered page number is not a number"
    data = []
    maxPerPage = 30
    with open("LE.txt", 'r', encoding="utf-8") as SP:
        Num = 0
        if Page == 1:
            for line in SP:
                data.append(line.strip().split('\t'))
                Num += 1
                if Num == maxPerPage:
                    break
        else:
            for i, line in enumerate(SP):
                if i > (((Page - 1) * maxPerPage) - 1) and i <= ((Page * maxPerPage) - 1):
                    data.append(line.strip().split('\t'))
                elif i > ((Page * maxPerPage) - 1):
                    break


    return jsonify({'Spare parts': data})

if __name__ == "__main__":
    app.debug = True
    app.run()