# Certificador XML para faturas de eletricidade

## Como instalar

Execute no diretório do projeto:
    cd xmlcert
    pip3 install .

Após instalar, entre no diretório pai para usar o módulo:
    cd ..

## Como usar

1. Crie um par de chaves RSA e um certificado autoassinado para testar:

`openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -subj '/CN=localhost' -nodes`

2. Crie um arquivo `xml` de exemplo.

`echo "<xml><name>John Doe</name></xml>" > example.xml

3. Assine o arquivo:
    
`python3 -m xmlcert sign -cert cert.pem -key key.pem -in example.xml -out out.xml`

4. Verifique a assinatura. Como o certificado é autoassinado, a autoridade
certificadora (cacert) e o certificado (cert) são o mesmo.

`python3 -m xmlcert verify -cacert cert.pem -in out.xml`
