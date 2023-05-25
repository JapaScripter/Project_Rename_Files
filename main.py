# =====Imports===== #
import os
# =====Imports===== #

# =====Renomear todos os arquivos numeral continuo independente da extensão | Rename all files continuous number regardless of extension===== #
# =====Main===== #

i = 0

# =====Local===== #
path = "C:\\me"

# =====Tentar Rodar/Try Run===== #
try:

    # =====Se existe/If Exist===== #
    if os.path.exists(path):
	
	# =====Para o arquivo desse diretório/For the file of this directory===== #
        for file in os.listdir(path):

            # =====Se JPG ou jpg | If JPG ou jpg===== #
            if file.endswith('.JPG') or file.endswith('.jpg'):
                if file.endswith('.jpg'):
                    newFileJpg = '{}.jpg'.format(i)
                    os.rename(file, newFileJpg)
                elif file.endswith('.JPG'):
                    newFileJPG = '{}.JPG'.format(i)
                    os.rename(path + '/' + file, path + '/' + newFileJPG)
                i = i + 1
		
            # =====Se JPEG ou jpeg | If JPEG ou jpeg===== #
            elif file.endswith('.JPEG') or file.endswith('.jpeg'):
                if file.endswith('.jpeg'):
                    newFileJpeg = '{}.jpeg'.format(i)
                    os.rename(path + '/' + file, path + '/' + newFileJpeg)
                elif file.endswith('.JPEG'):
                    newFileJPEG = '{}.JPEG'.format(i)
                    os.rename(path + '/' + file, path + '/' + newFileJPEG)
                i = i + 1
		
            # =====Se PNG ou png | If PNG ou png===== #
            elif file.endswith('.PNG') or file.endswith('.png'):
                if file.endswith('.png'):
                    newFilePng = '{}.png'.format(i)
                    os.rename(path + '/' + file, path + '/' + newFilePng)
                elif file.endswith('.PNG'):
                    newFilePNG = '{}.PNG'.format(i)
                    os.rename(path + '/' + file, path + '/' + newFilePNG)
                i = i + 1
		
            # =====Se JFIF ou jfif | If JFIF ou jfif===== #
            elif file.endswith('.JFIF') or file.endswith('.jfif'):
                if file.endswith('.jfif'):
                    newFilejfif = '{}.jfif'.format(i)
                    os.rename(file, newFilejfif)
                elif file.endswith('.JFIF'):
                    newFileJFIF = '{}.JFIF'.format(i)
                    os.rename(path + '/' + file, path + '/' + newFileJFIF)
                i = i + 1
		
            # =====Printar Sucesso | Print Sucess===== #
            print("Documentos renomeados com sucesso!")
		
    # =====Se diretório não existe | If directory doens't exist===== #
    if not os.path.exists(path):
		
        # =====Printar não tem documentos | Print don't have documents===== #
        print("Não tem documentos!")

# =====Excesão não rodar | Exception dont work===== #
except Exception as e:
	
    # =====Printar erro | Print error=====#
    print(f"Deu erro! {e}")
	
#=====Main=====#

# =====Renomear todos os arquivos numeral diferenciando por extensão  | Rename all files number distinguishing the extensions===== #
# =====Main===== #

i = 0
j = 0
k = 0
l = 0

# =====Local===== #
path = "C:\\me"

# =====Tentar Rodar/Try Run===== #
try:

    # =====Se existe/If Exist===== #
    if os.path.exists(path):
	
	# =====Para o arquivo desse diretório/For the file of this directory===== #
        for file in os.listdir(path):

            # =====Se JPG ou jpg | If JPG ou jpg===== #
            if file.endswith('.JPG') or file.endswith('.jpg'):
                if file.endswith('.jpg'):
                    newFileJpg = '{}.jpg'.format(i)
                    os.rename(file, newFileJpg)
                elif file.endswith('.JPG'):
                    newFileJPG = '{}.JPG'.format(i)
                    os.rename(path + '/' + file, path + '/' + newFileJPG)
                i = i + 1
		
            # =====Se JPEG ou jpeg | If JPEG ou jpeg===== #
            elif file.endswith('.JPEG') or file.endswith('.jpeg'):
                if file.endswith('.jpeg'):
                    newFileJpeg = '{}.jpeg'.format(j)
                    os.rename(path + '/' + file, path + '/' + newFileJpeg)
                elif file.endswith('.JPEG'):
                    newFileJPEG = '{}.JPEG'.format(j)
                    os.rename(path + '/' + file, path + '/' + newFileJPEG)
                i = i + 1
		
            # =====Se PNG ou png | If PNG ou png===== #
            elif file.endswith('.PNG') or file.endswith('.png'):
                if file.endswith('.png'):
                    newFilePng = '{}.png'.format(k)
                    os.rename(path + '/' + file, path + '/' + newFilePng)
                elif file.endswith('.PNG'):
                    newFilePNG = '{}.PNG'.format(k)
                    os.rename(path + '/' + file, path + '/' + newFilePNG)
                i = i + 1
		
            # =====Se JFIF ou jfif | If JFIF ou jfif===== #
            elif file.endswith('.JFIF') or file.endswith('.jfif'):
                if file.endswith('.jfif'):
                    newFilejfif = '{}.jfif'.format(l)
                    os.rename(file, newFilejfif)
                elif file.endswith('.JFIF'):
                    newFileJFIF = '{}.JFIF'.format(l)
                    os.rename(path + '/' + file, path + '/' + newFileJFIF)
                i = i + 1
		
            # =====Printar Sucesso | Print Sucess===== #
            print("Documentos renomeados com sucesso!")
		
    # =====Se diretório não existe | If directory doens't exist===== #
    if not os.path.exists(path):
		
        # =====Printar não tem documentos | Print don't have documents===== #
        print("Não tem documentos!")

# =====Excesão não rodar | Exception dont work===== #
except Exception as e:
	
    # =====Printar erro | Print error=====#
    print(f"Deu erro! {e}")
	
#=====Main=====#
