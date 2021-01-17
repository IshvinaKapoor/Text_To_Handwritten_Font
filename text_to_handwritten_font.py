# -*- coding: utf-8 -*-
"""
Coverting text to handwritten font

@author: DELL Ishvina Kapoor
"""

#importing the module
import pywhatkit as pkt

#displaying a message 
print("Converting text to handwriten font")

#the text we need to convert
text = "Hello\nMy name is ABC\nThis code converts the text to a handwriten font"
#calling the function which coverts the text to a handwriten font
#by default the location of the result image will be the same as the folder in which the python script is saved

pkt.text_to_handwriting(text,"texttohandwriting.png")

#will display this message once the image opens successfully 
print("Converted!!")