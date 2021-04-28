# Simple-PDF-to-Audiobook-Program

Converting PDF books to AudioBook using a simple Python program

<b>Step 1</b>

Install Python Library :

1. Install python Text to Speach Library

<code> pip install pyttsx3 </code>
 
2. Install python library to extract data from PDF files
  
<code> pip install PyPDF2 </code>

<b>Step 2</b>
 
Txt to Speach :

<pre><code>import pyttsx3
speaker = pyttsx3.init()
speaker.say('look Nikhil i am alive')
speaker.runAndWait()
</code></pre>

<b>Step 3</b>

Add a Pdf file and count no. of pages :

<pre><code>import PyPDF2
book = open('How to Win Every Argument.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
</pre></code>

<b>Step 4</b>
 
Convert specific page of a Pdf file into speech :

<pre><code>import pyttsx3
import PyPDF2
book = open('How to Win Every Argument.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
page = pdfReader.getPage(12) //Reading pgno.12
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
</code></pre>

<b>Step 5</b>

Convert Pdf file text into speech :

<pre><code>import pyttsx3
import PyPDF2
book = open('How to Win Every Argument.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
for num in range(12,pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

</code></pre>
