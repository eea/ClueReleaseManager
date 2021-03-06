from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup

base_version = '0.3.3'

readme = open('README.txt').read().strip()
history = open('HISTORY.txt').read().strip()

url = 'http://projects.serverzen.com/pm/p/cluemapper/ClueReleaseManager'

setup(name='ClueReleaseManager',
      version=base_version,
      description="An implementation of a PyPi server",
      long_description=readme + "\n" + history,
      classifiers=[
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          ],
      keywords='',
      author='Rocky Burt',
      author_email='rocky@serverzen.com',
      url=url,
      license='BSD',
      package_dir={'': 'src'},
      packages=['clue'],
      include_package_data=True,
      zip_safe=False,
      test_suite="clue.relmgr.tests.test_suite",
      install_requires=[
          'setuptools == 38.2.3',
          'SQLAlchemy == 1.1.15',
          'repoze.who == 1.0.19',
          'Werkzeug == 0.4.1',
          'Jinja2 == 2.10',
          'docutils == 0.14',
          ],
      entry_points={
          'console_scripts': [
              'cluerelmgr-server = clue.relmgr.main:main',
              'cluerelmgr-admin = clue.relmgr.cmdtool:main',
              ],
          },
      )
