import PyPDF2
import sys

def main():
	if(len(sys.argv) < 3):
		print("Usage: $ python rotatePdf.py direction fileToRotate")
		print("-- Options for direction --")
		print("clockwise")
		print("counter")
		print("flip")
	elif(str(sys.argv[1]) == "clockwise"):
		rotate(str(sys.argv[2]), str(sys.argv[2])[:-3]+"Rotated.pdf", 90)
	elif(str(sys.argv[1]) == "counter"):
		rotate(str(sys.argv[2]), str(sys.argv[2])[:-3]+"Rotated.pdf", 270)
	else:
		rotate(str(sys.argv[2]), str(sys.argv[2])[:-3]+"Rotated.pdf", 180)




def rotate(original, new, direction):
	pdfFileObj = open(original, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	pdfWriter = PyPDF2.PdfFileWriter()

	for page in range(pdfReader.numPages):
		pageObj = pdfReader.getPage(page)
		pageObj.rotateClockwise(direction)
		pdfWriter.addPage(pageObj)

	newFile = open(new, 'wb')

	pdfWriter.write(newFile)
	pdfFileObj.close()
	newFile.close()

if __name__ == '__main__':
	main()
