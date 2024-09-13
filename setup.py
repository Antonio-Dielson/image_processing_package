from setuptools import setup, find_packages

setup(
    name='image_processing_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'opencv-python'
    ],
    description='Pacote para unir e identificar diferenças entre imagens',
    author='Antonio Dielson',
    author_email='seuemail@example.com',
    url='https://github.com/seuperfil/image_processing_package',
)
