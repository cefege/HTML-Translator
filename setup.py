import setuptools

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='html-translator',
    version='0.0.1',
    author='Mihai Mateias',
    author_email='mateiasmihaiandrei@gmail.com',
    description='Package to translate the webpages content while keeping the same page structure',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['html-translator'],
    install_requires=["beautifulsoup4==4.10.0", "deep-translator==1.8.1"],

)
