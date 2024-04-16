from setuptools import setup

setup(
   name='kod',
   version='1.0',
   description='Provides a decorator for memory usage tracking. The part of FOSS course.',
   license='MIT',
   author='Kirilligu',
   author_email='k.degtyarev4@mail.ru',
   url='https://github.com/Kirilligu/setup',
   packages=['mtracker'],
   install_requires=[numpy],
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)

