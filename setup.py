#python'a
from setuptools import (setup, find_packages)

setup(
    name='gginin',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gginin = gginin.der:main' ] }
    
    )