from signxml import XMLSigner, XMLVerifier
from xml.etree import ElementTree

def sign(xml_file, cert_file, key_file, out_file):
    with open(xml_file, "rb") as f:
        xml_doc = f.read()

    with open(cert_file, "rb") as f:
        cert = f.read()

    with open(key_file, "rb") as f:
        key = f.read()

    root = ElementTree.fromstring(xml_doc)
    signed_root = XMLSigner().sign(root, key=key, cert=cert)
    signed_root.getroottree().write(out_file)

    print("Arquivo escrito em %s com sucesso." % out_file)

    with open(out_file, "r") as f:
        out_data = f.read()

def verify(xml_file, cacert_file):
    with open(xml_file, "r") as f:
        xml_doc = f.read()

    XMLVerifier().verify(xml_doc, ca_pem_file=cacert_file)
    print("Certificado verificado com sucesso.")
