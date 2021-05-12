#### pip install reportlab

from reportlab.pdfgen import canvas

def GeneratePDF(lista):
    try:
        nome_pdf = input('Infome o nome do PDF: ')
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 720
        for nome, idade in lista.items():
            x -= 20
            pdf.drawString(247, x, '{} : {}'.format(nome, idade))
        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245, 750, 'Lista de Clientes')
        pdf.save()
        print('{}.pdf Criado com Sucesso!!'.format(nome_pdf))
    except:
        print('Erro ao Gerar {}.pdf'.format(nome_pdf))

lista = {'Arthur': '26', 'Rafael' : '42', 'Mara' : '26', 'Onofre' : '33'}

GeneratePDF(lista)