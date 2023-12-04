import gtts.lang
from gtts import gTTS
from PyPDF2 import PdfReader

def convert_to_tts(pdf_text):
    input_text = pdf_text
    language = 'en'

    conv_object = gTTS(text=input_text, lang=language, slow=False)
    conv_object.save("convert3.mp3")

#Using PDFreader to convert pdf file and 1 page into text prior parsing to convert_to_tts function above
#Can be modified to render multiple pages to be converted to text
def conv_pdf_text():
    reader = PdfReader("test_pledge.pdf")
    page = reader.pages[0]
    pdf_text = page.extract_text()
    return pdf_text

passed_text = conv_pdf_text()
convert_to_tts(passed_text)

# lang = gtts.lang.tts_langs()
# print(lang)
