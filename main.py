import cv2
from pyzbar import pyzbar

def KareKodOku(cerceve):
    karekodlar=pyzbar.decode(cerceve)
    for karekod in karekodlar:
        x, y, genislik, yukseklik=karekod.rect

        veri=karekod.data.decode("utf-8")
        cv2.rectangle(cerceve, (x, y), (x + genislik, y + yukseklik), (0, 0, 255), 2)
        print(veri)

    return cerceve

def KamerayiAcarakBasla():
    webcam = cv2.VideoCapture(0)
    ret, cerceve = webcam.read()
    while ret:
        ret, cerceve = webcam.read()
        cerceve=KareKodOku(cerceve)
        cv2.imshow("Karekod okuyucu", cerceve)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    webcam.release()
    cv2.destroyAllWindows()

KamerayiAcarakBasla()