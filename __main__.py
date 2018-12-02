from sys import argv
from .crypto import sign, verify
# Argumentos padrão:
operation   = None
xml_file    = None
cert_file   = None
key_file    = None
cacert_file = None
out_file    = "out.xml"

argv.pop(0) # Descarta primeiro argumento

while argv:
    arg = argv.pop(0)
    if arg == "-in":
        xml_file = argv.pop(0)
    elif arg == "-out":
        out_file = argv.pop(0)
    elif arg == "-cert":
        cert_file = argv.pop(0)
    elif arg == "-key":
        key_file = argv.pop(0)
    elif arg == "-cacert":
        cacert_file = argv.pop(0)
    else:
        operation = arg

if operation == "sign":
    sign(xml_file, cert_file, key_file, out_file)
elif operation == "verify":
    verify(xml_file, cacert_file)
else:
    print("Operação inválida.")
