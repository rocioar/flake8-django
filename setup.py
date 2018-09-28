import setuptools

with open("README.md") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name='flake8-django',
    license='GPL',
    version='0.0.1',
    description='Plugin to catch bad style specific to Django Projects',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Rocio Aramberri Schegel',
    author_email='rocioaramberri@schegel.net',
    url='http://github.com/rocioar/flake8-django',
    py_modules=['flake8_django', 'issues'],
    entry_points={
        'flake8.extension': [
            'DJ0 = flake8_django:DjangoStyleChecker',
        ],
    },
    install_requires=['flake8'],
    tests_require=['pytest'],
    classifiers=[
        'Framework :: Flake8',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
