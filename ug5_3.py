# Single Linked List Non Circular
class NodeArtis:
    # constructor
    def __init__(self, value):
        self.next = None
        self.data = value
    

class Artis:
    def __init__(self) -> None:
        self.head = None
        self.tail = self.head
        self.ukuran = 0
    def __len__(self):
        return self.ukuran
    def __str__(self):
        if self.ukuran == 0:
            hasil = 'Linked list kosong'
        else:
            hasil = f'Daftar Artis : \n'
            helper = self.head
            while helper != None:
                hasil = hasil + str(helper.data) +''
                helper = helper.next
        return hasil 

    def prepend_artis(self,data):
        newNode = NodeArtis(data)
        if self.ukuran == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.ukuran = self.ukuran + 1
    
    def append_artis(self,data):
        newNode = NodeArtis(data)
        if self.ukuran == 0:
            self.head = newNode
            self.tail = newNode
        else :
            self.tail.next = newNode
            self.tail = newNode
        self.ukuran = self.ukuran + 1

    

class NodeLagu:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.data = value
class Lagu:
    def __init__(self):
        self.head = None
        self.dict = {}
        self.tail = None
        self.ukuran = 0
       

    def insert_artis(self, new_data):
        node = NodeLagu(new_data)
        self.dict[new_data] = Artis()
        node.prev = self.dict[new_data]
        if self.ukuran != 0:
            node.next = self.head
            self.head = node
        else:
            
            self.head = node
            self.tail = node
        self.ukuran += 1
        

    def tambah_lagu(self, namaArtis, namaLagu):
        self.dict[namaArtis].append_artis(namaLagu)
    def cetak(self):
        helper = self.head
    
        for i in self.dict:
           
            output = f"{i} lagunya yaitu : "
            
            helper = self.dict[i].head
            for k in range(self.dict[i].ukuran):
                if k == self.dict[i].ukuran-1:
                     output += f"{helper.data}"
                     continue
                output2 = ""     
                output += f"{helper.data}{output2}, "
                helper = helper.next
            print(output)
            
  

artis = Artis()

lagu = Lagu()
lagu.insert_artis('Dewa 19')
lagu.tambah_lagu('Dewa 19', 'Kangen')
lagu.tambah_lagu('Dewa 19', 'Arjuna')
lagu.tambah_lagu('Dewa 19', 'Risalah Hati')
lagu.insert_artis('Ed Sheeran')
lagu.tambah_lagu('Ed Sheeran', 'Shape of You')
lagu.tambah_lagu('Ed Sheeran', 'Shivers')
lagu.insert_artis('Alan Walker')
lagu.tambah_lagu('Alan Walker', 'Faded')

lagu.insert_artis('Raisa')
lagu.tambah_lagu('Raisa', 'Bahasa Kalbu')
lagu.tambah_lagu('Raisa', 'Mantan Terindah')
lagu.cetak() 