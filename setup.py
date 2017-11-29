from guldns import __version__
from setuptools import setup, find_packages

REQUIREMENTS = [line.strip() for line in open("requirements.txt").readlines()]

setup(name='guldns',
      version=__version__,
      platforms='linux',
      description='A decentralized replacement for DNS using the guld filesystem',
      author='isysd',
      author_email='public@iramiller.com',
      license='MIT',
      url='https://ns.guld.io/',
      packages=find_packages(exclude=['tests', 'tests.*']),
      entry_points={'console_scripts': ['gns = guldns:main']},
      zip_safe=False,
      include_package_data=True,
      install_requires=REQUIREMENTS,
      classifiers=[
          'Topic :: System :: Administration',
          'Development Status :: 4 - Beta',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Administration',
          'Topic :: Internet',
          'Topic :: Utilities'
])
