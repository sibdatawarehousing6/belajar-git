"""
Ini adalah script untuk membangun kelas Satpam dengan fitur:
1. Menjaga TPU
2. Istirahat
3. Lembur
"""

from warga import Warga

class Satpam(Warga):

    def __init__(self,NIK,id_satpam):
        Warga.__init__(self,NIK)
        self.id_satpam = id_satpam

    def jaga_tpu(self,tempat):
        print(f'{self.id_satpam} jaga di {tempat}')
    
    def istirahat(self,tempat):
        print(f'{self.id_satpam} sedang melakukan istirahat jam 12.00 sampai 12.30 di {tempat}')

    def lembur(self,hari):
        print(f'{self.id_satpam} mengambil lembur di hari {hari}')