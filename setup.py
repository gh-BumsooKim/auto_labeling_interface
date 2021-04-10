from setuptools import setup


#with open("README.md", "r")as f:
#    description = f.read()
    
requirements = [
    'dlib>=19.7',
    'numpy',
    'Pillow'
]
    
setup(
    name = 'face_labeling',
    version = '0.1.1',
    install_requires = requirements,
    license = 'MIT license',
    py_modules = [
        'face_labeling',
    ],
    description = 'Make annoation file about face image automatically',
    author = 'BumsooKim',
    author_email = 'cmng828rhuypqq@gmail.com',
    url = 'https://github.com/gh-BumsooKim/face_labeling',
    #packages = setuptools.find_packages(),
    keywords = 'face_labeling',
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows"
    ],
)