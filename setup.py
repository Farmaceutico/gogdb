from setuptools import setup, find_packages



requires = [
    # base
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'waitress',

    # database
    'pyramid_tm',
    'SQLAlchemy',
    'psycopg2',
    'transaction',
    'zope.sqlalchemy',

    # assets
    'pyramid_webassets',
    'webassets',
    'rcssmin',
    'rjsmin',

    # util
    'arrow',
    'requests',
    'requests-futures'
]

setup(
    name='gogdb_site',
    version='0.1',
    description='GOG Database',
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application'
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = gogdb_site:main'
        ],
        'console_scripts': [
            'initialize-db = gogdb_site.scripts.initializedb:main',
            'build-assets = gogdb_site.scripts.buildassets:main'
        ],
    }
)
