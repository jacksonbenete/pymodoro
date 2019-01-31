from PyPDF2 import PdfFileMerger
import os
import re

merger = PdfFileMerger()

print("Entre com o diretorio dos arquivos: ")
diretorio = input(">> ")

print("Entre com o nome do arquivo final: ")
nome_final = input(">> ")

# Encontrar todos os pdf
root_dir = './' + diretorio + '/'
input_pdf = []

for directory, subdirectories, files in os.walk(root_dir):
    for file in files:
        if re.search(".pdf", (os.path.join(directory, file))):
            #input_pdf.append(re.sub("./", "", os.path.join(directory, file)))
            input_pdf.append(os.path.join(directory, file))

# Coloca os pdf no vetor
##input_pdf = []
##input_pdf[0] = open("1-5.pdf", "rb")
##input_pdf[1] = open("6.pdf", "rb")
##input_pdf[2] = open("7.pdf", "rb")
##input_pdf[3] = open("8.pdf", "rb")
##input_pdf[4] = open("9.pdf", "rb")
##input_pdf[5] = open("11-15.pdf", "rb")
##input_pdf[6] = open("16.pdf", "rb")
##input_pdf[7] = open("Legacy.pdf", "rb")

print(input_pdf)
# Da merge em tudo
for x in input_pdf:
    try:
        y = open(x, "rb")
        merger.append(y)
        print(x + " Merged")
    except ValueError:
        print(x + " NOT Merged")

#merger.append(input3)

# Write to an output PDF document
nome_final = nome_final + ".pdf"
output = open(nome_final, "wb")
merger.write(output)
