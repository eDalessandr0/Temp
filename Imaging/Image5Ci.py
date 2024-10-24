from PIL import Image

# Definisco una classe personale di gestione delle immagini
# In particolare che permetta l'apertura e l'elaborazione di una singola BMP
class Image5Ci:
    # Costruttore definito come metodo speciale DUNDER (Double Underscore)
    def __init__(self, imagePath):
        # Tento di aprire l'immagine il cui percorso è passato come parametro
        # Se non ci riesco per qualsiasi motivo, sollevo un'eccezione
        self.__myImage = None
        self.__imagePath = imagePath
        self.__pixels = None
        self.__width = 0
        self.__height = 0
        
        try:
            # Tentativo di apertura
            self.__myImage = Image.open(imagePath).convert("RGB")
            self.__pixels = self.__myImage.load()
            self.__width, self.__height = self.__myImage.size
        except Exception as ex:
            raise Exception(f"Attenzione! Qualcosa è andato storto nell'apertura dell'immagine {imagePath}")

    # Elenco di metodi pubblici di modifica dell'immagine
    
    # Negativo
    def Negative(self, showResult = False, saveResult = False):
        # Creo una nuova immagine per non rovinare quella esistente
        img = Image.new("RGB", (self.__width, self.__height))
        
        # Ciclo su ogni pixel e inverto il valore di ogni canale RGB
        for x in range(self.__width):
            for y in range(self.__height):
                # Recupero il pixel corrente
                r, g, b = self.__pixels[x, y]
                # Lo inverto e lo salvo nella nuova immagine
                img.putpixel((x, y), (255 - r, 255 - g, 255 - b))
                
        # Controllo se mostrare il risultato
        if showResult:
            img.show()
    
        # Controllo se salvare il risultato
        if saveResult:
            img.save("negativo.jpg", "JPEG", quality = 100, optimize = 100, progressive = True)
    
    # Specchiatura orizzontale
    def HorizontalFlip(self, showResult = False, saveResult = False):
        # Creo una nuova immagine per non rovinare quella esistente
        img = Image.new("RGB", (self.__width, self.__height))
        
        # Ciclo su ogni pixel e specchio i valori in orizzontale
        for x in range(self.__width):
            newX = self.__width - 1 - x
            for y in range(self.__height):
                # Salvo il pixel nella nuova posizione
                img.putpixel((newX, y), self.__pixels[x, y])
            
        # Controllo se mostrare il risultato
        if showResult:
            img.show()
    
        # Controllo se salvare il risultato
        if saveResult:
            img.save("HFlip.jpg", "JPEG", quality = 100, optimize = 100, progressive = True)

    # Specchiatura verticale
    def VerticalFlip(self, showResult = False, saveResult = False):
        # Creo una nuova immagine per non rovinare quella esistente
        img = Image.new("RGB", (self.__width, self.__height))
        
        # Ciclo su ogni pixel e specchio i valori in verticale
        for x in range(self.__width):
            for y in range(self.__height):
                newY = self.__height - 1 - y
                # Salvo il pixel nella nuova posizione
                img.putpixel((x, newY), self.__pixels[x, y])
            
        # Controllo se mostrare il risultato
        if showResult:
            img.show()
    
        # Controllo se salvare il risultato
        if saveResult:
            img.save("VFlip.jpg", "JPEG", quality = 100, optimize = 100, progressive = True)

    # Differenza fra immagini
    def Difference(self, otherImagePath, showResult = False, saveResult = False):
        otherImage = None
        otherPixels = None

        # Tento di aprire l'immagine il cui percorso è stato passato come parametro
        try:
            otherImage = Image.open(otherImagePath).convert("RGB")
            otherPixels = otherImage.load()
            width, height = otherImage.size
        except Exception as ex:
            # Questa non è una buona prassi... ma funziona!
            return
        
        # Se sono arrivato fin qua... tutto è andato bene
        # Controllo se le dimensioni sono uguali
        if width != self.__width or height != self.__height:
            raise Exception(f"Attenzione! L'immagine {otherImagePath} non ha le dimensioni corrette!")
        
        # Creo una nuova immagine per non rovinare quella esistente
        img = Image.new("RGB", (self.__width, self.__height))
        
        # valore di tolleranza
        tolerance = 10
        
        # Ciclo su ogni pixel e specchio i valori in verticale
        for x in range(self.__width):
            for y in range(self.__height):
                # Leggo i pixel delle due immagini
                rA, gA, bA = self.__pixels[x, y]
                rB, gB, bB = otherPixels[x, y]
                
                # E' sufficiente che in uno dei 3 canali ci sia abbastanza differenza per 
                # mettere il pixel a BIANCO
                # ...
    