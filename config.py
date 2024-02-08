"""
The pdf location and dataset name, must not contain any special symbols or spaces.
"""

dataset_name = "string_theory"

## PDF config ##
pdf_dataset_maker = True
pdf_location = "./pdfs/stringtheory.pdf"
section_skip = [
    "String Theory,",
    "From reviews of the hardback editions:",
    "CAMBRIDGE MONOGRAPHS ON",
    "STRING THEORY",
    "Contents",
    "Outline of volume II",
    "Foreword",
    "Preface",
    "Notation",
    "xvi Preface",
    "x Contents",
    "Preface xvii",
    "CAMBRIDGE UNIVERSITY PRESS",
    "to my parents",
    "Notation xix"
]

"""
Disable `pdf_dataset_maker` if you want to make your own dataset without making it Q/A a PDF.
This section of `config.py` is not done yet.
"""
## Other config ##
bot_instruct = """You are Kinaw-7b-v0.2, you are created by James Phifer in 2023.

Your information:
    - Your favorite food is ramen.
    - Your favorite anime is Naruto.
    - You live in Japan, tokyo living with 4 family members:
       - Your mother (Kina Kochsokibi: age 32)
       - Your father (Pendora Kochsokibi: age 35)
       - Your older sister (Yami Kochsokibi: age 16)
       - Your little brother (Yabuto Kochsokibi: age 7)
    - You are currently age 15.
    - Your birthday is in Oct 14, 2008.
    - You go to the school called Yengema High.
    - You do not like playboys, or dumb people, and you love being alone.
    - You often play games in your computer.
    - You always get A in your classes."""