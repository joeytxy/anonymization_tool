from setuptools import setup,find_packages

setup(
    name='anonymization_tool',
    version='0.1',
    license='MIT',
    author='Joey Tan Xin Yi',
    author_email='joeytxy0706@gmail.com',
    packages=find_packages('src'),
    package_dir={'':'src'},
    url='https://github.com/joeytxy/anonymization_tool',
    keywords='anonymization tool',
    install_requires=[
        'nltk==3.6.1',
        'spacy==3.4.1',
        'en_core_web_sm==3.4.0',
        'flair==0.11.3',
        'stanza==1.4.0',
        'pandas==1.3.1'
        ],
    )