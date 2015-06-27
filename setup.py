from distutils.core import setup

setup(
    name='vais',
    version='0.0.5',
    author='Duncan Murray',
    author_email='djmurray@acutesoftware.com.au',
    packages=['vais', 'vais.data','vais.examples','vais.npc'],
    url='https://github.com/acutesoftware/virtual-AI-simulator',
    install_requires=[
          'nose >= 1.0',
          'noise >= 1.2.1'
    ],
    license='LICENSE.txt',
    description='Virtual AI Simulator runs agents and players across multiple worlds',
    long_description=open('README.rst').read(),
    classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Programming Language :: Python :: 3.4',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Games/Entertainment :: Simulation',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],

)