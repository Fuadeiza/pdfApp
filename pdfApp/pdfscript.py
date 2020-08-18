# pdfscript.py
from pdfrw import PdfReader, PdfWriter, PageMerge, IndirectPdfDict

path = PdfReader(r'C:\Users\DELL\Python stuffs\pdf pypy\sample.pdf')
# r'C:\Users\DELL\Python stuffs\pdf pypy\reportlab-sample.pdf'


#function to get pdf info.
def get_pdf_info(path):
    pdf = PdfReader(path)
    print(pdf.keys())
    print(pdf.Info)
    print(pdf.Root.keys())
    print('PDF has {} pages'.format(len(pdf.pages)))

# get_pdf_info()


#This function split pages of a pdf and create a new on with the specified number of pages in output path

def split(number_of_pages, output):
    pdf_obj = PdfReader(r'C:\Users\DELL\Python stuffs\pdf pypy\reportlab-sample.pdf')
    total_pages = len(pdf_obj.pages)
    writer = PdfWriter()
    for page in range(number_of_pages):
        if page <= total_pages:
            writer.addpage(pdf_obj.pages[page])
    writer.write(output)

# split(number_of_pages=6, output=r'C:\Users\DELL\Python stuffs\pdf pypy\new-sample.pdf')



# This function merges 2 pdf files, paths is where you put in the location of both pdfs, while output is the final merged pdf
def concatenate(paths, output):
    writer = PdfWriter()
    for path in paths:
        reader = PdfReader(path)
        writer.addpages(reader.pages)



#This function rotates a certain page of the  pdf by 90degrees right.
def rotate(path, bad_page, output):
    reader = PdfReader(path)
    writer = PdfWriter()
    pages = reader.pages
    for page in range(len(pages)):
        if page == bad_page :
            pages[bad_page].Rotate = 90
            writer.addpage(pages[bad_page])
    writer.write(output)


# rotate(r'C:\Users\DELL\Python stuffs\pdf pypy\new-sample.pdf', 3, r'C:\Users\DELL\Python stuffs\pdf pypy\new_rotate_sample.pdf')


#This function takes 2 pdf's one with the watermark, the other is the main pdf, the watermark pdf is then underlayed and merged on every page of the main pdf 
def watermarker(path, watermark, output):
    base_pdf = PdfReader(path)
    watermark_pdf = PdfReader(watermark)
    mark = watermark_pdf.pages[0]
    for page in range(len(base_pdf.pages)):
        merger = PageMerge(base_pdf.pages[page])
        merger.add(mark).render()
    writer = PdfWriter()
    writer.write(output, base_pdf)


# watermarker(r'C:\Users\DELL\Python stuffs\pdf pypy\new-sample.pdf', r'C:\Users\DELL\Python stuffs\pdf pypy\new_rotate_sample.pdf', r'C:\Users\DELL\Python stuffs\pdf pypy\watermark.pdf')


