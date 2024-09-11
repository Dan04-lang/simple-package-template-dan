from setuptools import setup, find_packages

setup(
    name='meu_projeto',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow>=9.0.0',
    ],
    entry_points={
        'console_scripts': [
            'processar-imagem=file2_name:processar_imagem',
        ],
    },
)
