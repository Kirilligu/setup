from setuptools import setup

setup(
   name='triangle_area_calculator',
   version='1.0',
   description='a utility that calculates the area of a triangle',
   license='MIT',
   author='Kirilligu',
   author_email='k.degtyarev4@mail.ru',
   url='https://github.com/Kirilligu/setup',
   packages=[''],
   install_requires=[], # it is empty since we use standard python library,
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)

