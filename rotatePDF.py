import PyPDF2
import sys

def main():
	if(len(sys.argv) < 4):
		print("Usage: $ python rotatePdf.py direction fileToRotate rotatedFile")
	elif(str(sys.argv[1]) == "clockwise"):
		rotateClockwise(str(sys.argv[2]), str(sys.argv[3]))
	elif(str(sys.argv[1]) == "counter"):
		rotateCounterClockwise(str(sys.argv[2]), str(sys.argv[3]))
	else:
		flip(str(sys.argv[2]), str(sys.argv[3]))

def flip(original, new):
	pdfFileObj = open(original, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	pdfWriter = PyPDF2.PdfFileWriter()

	for page in range(pdfReader.numPages):
		pageObj = pdfReader.getPage(page)
		pageObj.rotateClockwise(180)
		pdfWriter.addPage(pageObj)

	newFile = open(new, 'wb')

	pdfWriter.write(newFile)
	pdfFileObj.close()
	newFile.close()

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

if __name__ == '__main__':
	main()
