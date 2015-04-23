from distutils.core import setup

setup(
    name='vais',
    version='0.0.1',
    author='Duncan Murray',
    author_email='djmurray@acutesoftware.com.au',
    packages=['vais', 'vais.data','vais.examples','vais.npc'],
    url='https://github.com/acutesoftware/virtual-AI-simulator',
    license='LICENSE.txt',
    description='VAIS runs simulations of agents and players across multiple worlds',
    long_description=open('README.md').read(),
    classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Programming Language :: Python :: 3.4',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],

)