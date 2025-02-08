def _validar_correo(correo):
        
        if not (len(correo.split("@")) == 2 and\
            len(correo.split("@")[1].split(".")) == 2 and\
            correo.split("@")[0] != "" and\
            correo.split("@")[1].split(".")[0] != "" and \
            correo.split("@")[1].split(".")[1].isalpha()):
                print("Invalido")
        else:
            print("valido")
correo = "buenojosefrancisco@1234.com"
_validar_correo(correo)
