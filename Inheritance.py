#membuat class berisi state & method
class makhluk_hidup():
    def __init__(self,nama,umur,alamat):  
        self.nama=nama
        self.umur=umur
        self.alamat=alamat

    def print_variable(self):
        print('nama: ',self.nama, '\numur: ',self.umur,'\nalamat: ',self.alamat)

class manusia(makhluk_hidup):
        pass
       


hellman=manusia('hellman','23 tahun','banjarnegara')
hellman.print_variable()
        