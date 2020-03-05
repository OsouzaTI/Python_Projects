from requests import get  # to make GET request
from os import sys
from time import sleep
from tqdm import tqdm
import math

print(sys.version_info)
if sys.version_info >= (3, 6):
    import zipfile
else:
    import zipfile36 as zipfile
    
class AutoUpdate:

    url = "https://www.dropbox.com/s/73ba44bw23gb8v8/versao.txt?raw=1";
    urlGame = "https://www.dropbox.com/s/jpq9emgbdatr2q2/GameSemNome_.zip?dl=1"
    mudancas = "https://www.dropbox.com/s/tjopw5k7x205uym/changes.txt?dl=1"
    arq = None;
    old_version = None;
    Version = None;
    Info = None
    txt_files = ["versao.txt",
                 "old_version.txt",
                 "GameSemNome.zip"
                 ]
    def __init__(self):
        self.r = None
        self.arq_dl = 0
        self.size_dl = 1
        self.block_size = 1024 #1 Kibibyte
        self._quit = None
        self.Info = "Verificando Update..."

    def OldVersion(self):
        arq = open(self.txt_files[0], "r")
        _old_version = arq.read()
        self.old_version = float(_old_version)
        arq.close()
        
        old_file = open(self.txt_files[1], "wb")
        old_file.write( _old_version.encode() )
        old_file.close()
        
    def download(self, url, file_name):
        self.OldVersion()
        # open in binary mode
        with open(file_name, "wb") as file:      
            
            # get request
            response = get(url)
            # write to file
            file.write(response.content)
            file.close()
            #retorna Ponteiro para arquivo
            arq = open(file_name, "r")
            self.Version = float(arq.read())
            arq.close()

    def GameUpdate(self):
        
        with get(self.urlGame, stream=True) as r:
            self.Info = "Atualizando"
            self.size_dl = int(r.headers['Content-length'])
            r.raise_for_status()
            with open(self.txt_files[2], "wb") as f:
                for chunk in r.iter_content(chunk_size=self.block_size):
                    if chunk:
                        f.write(chunk)
                        self.arq_dl += 1
         
        self.Info = "Descompactando..."
        with zipfile.ZipFile(self.txt_files[2], "r") as z:
            z.extractall()
        z.close()
        self.Info = "Descompactado!"
        self._quit = True
        return True

    def Mostrar_Mudancas(self):

        m = get(self.mudancas)        
        return m.content
        
                    
        
    def Mostrar_Versoes(self):
        
        self.download(self.url, self.txt_files[0])
        print("Versão Anterior:\t" + str(self.old_version) )
        print("Versão Atual:\t\t"    + str(self.Version) )

        if( self.old_version == self.Version ):
            self._quit = False            
        else:
            print("Jogo desatualizado!")
            self._quit = self.GameUpdate()                        
                
