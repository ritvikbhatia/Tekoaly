from pdfminer3.layout import LAParams, LTTextBox,LTLine,LTTextLine
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import PDFPageAggregator
extracted_text=''
fp = open('C:\\Users\\Ritvik\\Desktop\\Tekoaly\\PDF\\768686236423.pdf', 'rb')
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
pages = PDFPage.get_pages(fp)

for page in pages:
    print('Processing next page...')
    interpreter.process_page(page)
    layout = device.get_result()
    for lt_obj in layout:
	    if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
		    extracted_text += lt_obj.get_text()
    print(extracted_text)
    # for lobj in layout:
    #     if isinstance(lobj, LTTextBox):
    #         x, y, text = lobj.bbox[0], lobj.bbox[3], lobj
    #         print(' text: %s' % (text) ,end=' ')
