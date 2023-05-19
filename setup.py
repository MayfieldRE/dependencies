import setuptools

setuptools.setup(
    name='mre-dependencies',
    version='0.0.1',
    author='Zach Snyder',
    author_email='zach@mayfield.energy',
    description='Python dependencies for Mayfield Energy Excel automations',
    long_description="",
    long_description_content_type="text/markdown",
    url='https://github.com/MayfieldRE/dependencies.git',
    project_urls = {
        "Bug Tracker": "https://github.com/Muls/toolbox/issues"
    },
    packages=['mre-dependencies'],
    install_requires=[
    	'xlwings',
        'openpyxl',
    	'numpy',
    	'matplotlib',
    	'pandas',
    	'pyairtable'
    ]
)
