from setuptools import setup

setup(name='pips',
      version='0.2',
      description='pip wrapper for new requirements handling',
      url='https://github.com/jboegeholz/pips',
      author='Joern Boegeholz',
      author_email='boegeholz.joern@gmail.com',
      license='MIT',
      packages=['pips'],
      entry_points={
            "console_scripts": [
                  "pips=pips:main",

            ],
      },
      zip_safe=False
)