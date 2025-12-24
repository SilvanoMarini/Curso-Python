from pathlib import Path
from pypdf import PdfReader, PdfWriter


PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'novos_arquivos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'pdf_focus.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

page1 = reader.pages[0]
imagem1 = page1.images[0]

# with open( PASTA_NOVA / 'bacen_img.png', 'wb') as fb:
#     fb.write(imagem1.data)


# writer = PdfWriter()

# with open( PASTA_NOVA / 'pages.pdf', 'wb') as fp:
#     for page in reader.pages:
#         writer.add_page(page)
#     writer.write(fp)


# for i, page in enumerate(reader.pages):
#     with open( PASTA_NOVA / f'page{i + 1}.pdf', 'wb') as fp:
#         writer = PdfWriter()
#         writer.add_page(page)
#         writer.write(fp)

pdf1 = PASTA_NOVA / 'page1.pdf'
pdf2 = PASTA_NOVA / 'page2.pdf'

writer = PdfWriter()

writer.append(pdf1)
writer.append(pdf2)

with open( PASTA_NOVA / 'pdfs_juntos.pdf', 'wb') as fp:
    writer.write(fp)