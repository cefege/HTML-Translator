import setuptools

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='HTML-Translator',
    version='0.0.1',
    author='Mihai Mateias',
    author_email='mateiasmihaiandrei@gmail.com',
    description='Package to translate the webpages content while keeping the same page structure',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['HTML-Translator'],
    install_requires=["beautifulsoup4==4.10.0", "certifi==2021.10.8", "charset-normalizer==2.0.12",
                      "deep-translator==1.8.1", "idna==3.3", "numpy==1.22.3", "pandas==1.4.1", "python-dateutil==2.8.2",
                      "pytz==2022.1", "requests==2.27.1", "six==1.16.0", "soupsieve==2.3.1", "tqdm==4.63.1",
                      "urllib3==1.26.9", ],
)
