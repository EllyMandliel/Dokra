from distutils.core import setup

setup(
    name='Dokra',  # How you named your package folder (MyLib)
    packages=['Dokra'],  # Chose the same as "name"
    version='0.1',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Use type annotations to inject middleware functions!',  # Give a short description about your library
    author='Dirat Yokra',  # Type in your name
    author_email='ellykido@gmail.com',  # Type in your E-Mail
    url='https://github.com/EllyMandliel/Dokra',  # Provide either the link to your github or to your website
    download_url='https://github.com/EllyMandliel/Dokra/archive/0.1.tar.gz',
    keywords=['Annotations', 'hint', 'type', 'python', 'dokra'],  # Keywords that define your package best
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)
