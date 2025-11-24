from pypdf import PdfReader, PdfWriter


# Leitor do pdf 
reader = PdfReader("teste01.pdf")
writer = PdfWriter()
metadados = reader.metadata 
page = reader.pages

# Mostrar os texto 
for c in range(len(page)):
    all_page = page[c].extract_text(extraction_mode="layout",layout_mode_space_vertically=False)




'''
print(page[0].extract_text(extraction_mode="layout"))
print(page[0].extract_text(extraction_mode="layout",layout_mode_space_vertically=False)) # Removendo os espaços vercicalmente 
'''
