import PyPDF2

def rotateCounterClockwise(original, new):
	pdfFileObj = open(original, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	pdfWriter = PyPDF2.PdfFileWriter()

	for page in range(pdfReader.numPages):
		pageObj = pdfReader.getPage(page)
		pageObj.rotateCounterClockwise(90)
		pdfWriter.addPage(pageObj)

	newFile = open(new, 'wb')

	pdfWriter.write(newFile)
	pdfFileObj.close()
	newFile.close()


def rotateClockwise(original, new):
	pdfFileObj = open(original, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	pdfWriter = PyPDF2.PdfFileWriter()

	for page in range(pdfReader.numPages):
		pageObj = pdfReader.getPage(page)
		pageObj.rotateClockwise(90)
		pdfWriter.addPage(pageObj)

	newFile = open(new, 'wb')

	pdfWriter.write(newFile)
	pdfFileObj.close()
	newFile.close()


