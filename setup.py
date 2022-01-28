import os
import setuptools

required = []
if os.path.exists('requirements.txt'):
    with open('requirements.txt', 'r') as f:
        required = f.readlines()


setuptools.setup(
    name='dummy-package',
    version="0.0.1",
    author="Fedor Marchenko",
    author_email="mfs90@mail.ru",
    description="A small dummy package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=required,
)
