# -*- coding: utf-8 -*-
from flask import render_template, request, Blueprint, redirect, url_for, flash
import face_recognition

home_bp = Blueprint('home', __name__, url_prefix='/home')

@home_bp.route('/', methods=['GET', 'POST'])
def home():
    # Load the jpg files into numpy arrays
    obama_image = face_recognition.load_image_file('face-recognition/known_people/Barack_Obama.jpg')
    pele_image = face_recognition.load_image_file('face-recognition/known_people/Pelé.jpg')
    unknown_image = face_recognition.load_image_file('face-recognition/unknown_pictures/pelé_teste1.png')

    # Get the face encodings for each face in each image file
    # Since there could be more than one face in each image, it returns a list of encodings.
    # But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
    try:
        obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
        pele_face_encoding = face_recognition.face_encodings(pele_image)[0]
        unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
    except IndexError:
        print('deu ruim')

    known_faces = [
        pele_face_encoding,
        obama_face_encoding
    ]

    # results is an array of True/False telling if the unknown face matched anyone in the known_faces array
    results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

    print(results)
    print(known_faces[0])

    return 'Funciona'

@home_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    return render_template('index.html', form=form, titulo='Cadastrar')
