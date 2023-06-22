# -*- coding: utf-8 -*-
"""
Created on Wed May 31 21:55:42 2023

@author: jveraz
"""

#######################
## datos desde excel ##
#######################

import streamlit as st

## usamos la librería pandas y leemos el excel
import pandas as pd

from PIL import Image

## leemos los datos
datos = pd.read_excel('mapudungun.xlsx')

u = pd.read_excel(open('mapudungun.xlsx', 'rb'),sheet_name='consonante')
D = u.set_index('persona').to_dict(orient='index')

ui = pd.read_excel(open('mapudungun.xlsx', 'rb'),sheet_name='vocal no i')
Dui = ui.set_index('persona').to_dict(orient='index')

uo = pd.read_excel(open('mapudungun.xlsx', 'rb'),sheet_name='vocal i')
Duo = uo.set_index('persona').to_dict(orient='index')

## con este diccionario, cree una función que reciba tres parámetros: base, número y persona
## y conjugue la base. 

base = 'kon'
persona = 3
numero = 'dual'

def conjugacion(base,numero,persona):
    
    #conjugacion = base + D[persona][numero]
    
    if base[-1] not in "aeiou":
        conjugacion = base + D[persona][numero]
        
    if base[-1] in "aeou":
        conjugacion = base + Dui[persona][numero]
    
    if base[-1] in "i":
        
        if persona == 3 and numero == "singular":
            conjugacion = base 
        else:
            conjugacion = base + Duo[persona][numero]
    
    return conjugacion
    
#print(conjugacion(base,numero,persona))

#############################
## todas las conjugaciones ##
#############################

## Dado un verbo que termine en consonante (de la primera tabla), genere todas las formas
## asociadas a todas las combinaciones de números y personas. Guarde esta información en
## un diccionario d. Use la misma estructura del diccionario D, pero ahora en vez de morfemas
## guarde conjugaciones. 
## Con df = pd.DataFrame.from_dict(d).T transforme d en un dataframe df. 

## creando un d
base = 'kon'
d = {1:{}, 2:{}, 3:{}}

for persona in d.keys():
    #print(persona)
    for numero in ['singular','dual','plural']:
        #print(persona,numero)
        v = conjugacion(base,numero,persona)
        #print(v)
        d[persona][numero] = v

df = pd.DataFrame.from_dict(d).T
#df.to_excel('jane.xlsx')


######################
## función ampliada ##
######################

## Escriba las diferentes tablas de conjugación en diferentes hojas del mismo excel. Use
## Use pd.read_excel(open('mapudungun.xlsx', 'rb'),sheet_name='consonante') para leer cada hoja.
## Redefina la función anterior para cualquier verbo de los tres tipos de conjugación. 

#u = pd.read_excel(open('mapudungun.xlsx', 'rb'),sheet_name='consonante')
#D = u.set_index('persona').to_dict(orient='index')

#ui = pd.read_excel(open('mapudungun.xlsx', 'rb'),sheet_name='vocal no i')
#Dui = ui.set_index('persona').to_dict(orient='index')

#uo = pd.read_excel(open('mapudungun.xlsx', 'rb'),sheet_name='vocal i')
#Duo = uo.set_index('persona').to_dict(orient='index')

#############
## if-else ##
#############

## Reescriba la primera función, de la primera tabla, solo usando condiciones lógicas.

## los Excel son muchos diccionarios recopilados
#Y = ":blue[¡Conjuguemos los verbos en mapudungun!] ✨"


#st.markdown(Y)
st.markdown("<p style='color: blue; font-size: 32px; font-weight: bold;'>¡Conjuguemos los verbos en mapudungun! ✨</p>", unsafe_allow_html=True)
#st.markdown("<h1 style='text-align: center;'>:blue[¡Conjuguemos los verbos en mapudungun!] ✨</h1>", unsafe_allow_html=True)
#st.title(st.markdown(Y))
#st.title(":blue[¡Conjuguemos verbos en mapudungun!]✨")

st.write("El mapudungun es una lengua mapuche que abarca los actuales países de Chile y Argentina." 
         "Actualmente posee entre 100 000 y 200 000 hablantes. En términos lingüísticos, el mapuche es una lengua aislada, ya que no posee parentesco con otra.")

st.write('La conjugación de los verbos en esta lengua es interesante, ya que a la base del verbo se le añade un sufijo que contiene la información gramatical de persona y número.'
         'Este sufijo cambiará dependiendo de la última letra de la base. Así, si esta base termina en consonante, en una vocal <i> o una vocal distinta, la conjugación será diferente.')

archivo = pd.read_excel('verbos.xlsx')

Di = dict(zip(archivo['español'],archivo['mapudungun']))

option = st.selectbox(
    'Elige un verbo en español de la siguiente lista:',
    list(Di.keys()))

text_input = Di[option]

p = st.selectbox(
    'Elige una persona gramatical:',
    (1,2,3))

d = {1:'primera', 2:'segunda', 3:'tercera'}

n = st.selectbox(
    'Elige un número gramatical:',
    ('singular', 'dual', 'plural'))
c = conjugacion(text_input,n,p)

s = 'El verbo ' + '**' + option + '**' + ' en ' + d[p] + ' persona ' + ' y en ' + ' número ' + n + ' se escribe de la siguiente manera: ' + '➡️' + c + '⬅️'
     
st.write(s)

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

i = Image.open("fotogrupal.jpeg")
i = i.resize((300, 200))
#st.image(i)


col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image(i, caption="✨EQUIPO MARAJA✨")

with col3:
    st.write(' ')

