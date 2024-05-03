from setuptools import setup, find_packages



setup(
    name='ml-project-demo',
    version='0.0.1',
    description='Demo ML Project created for learning',
    author='Amitesh',
    author_email='b.amitesh@gmail.com',
    url='https://github.com/amitesharqiva/ml-project-demo.git',
    packages=find_packages(),
    install_requires=[
        'requests','pandas','numpy'
    ],
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    long_description='This is a demo ML project'
)