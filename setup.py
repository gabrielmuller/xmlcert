from setuptools import setup, find_packages

setup(
    name = 'xmlcert',
    version = '0.0.1',
    url = 'https://github.com/gabrielmuller/xmlcert',
    author = 'Gabriel Müller, Juliana Pinheiro',
    author_email = 'gabrielmullerw@gmail.com',
    description = 'Certificador XMLDsig para faturas de eletricidade.',
    packages = find_packages(),
    install_requires = ['signxml'],
)
