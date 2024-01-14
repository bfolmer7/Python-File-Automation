from setuptools import setup, find_packages

setup(
    name='file_organizer',
    version='1.0.0',
    description='Automatically organize files in the Downloads folder.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Bo Folmer',
    author_email='bofolmer06@gmail.com',
    url='https://github.com/bfolmer7/Python-File-Automation',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'file_organizer=file_organizer:main',
        ],
    },
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
