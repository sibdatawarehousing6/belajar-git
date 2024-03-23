from warga import Warga

class Satpam(Warga):

    def __init__(self,NIK,id_satpam):
        Warga.__init__(self,NIK)
        self.id_satpam = id_satpam

    def jaga_tpu(self,tempat):
        print(f'{self.id_satpam} jaga di {tempat}')
    