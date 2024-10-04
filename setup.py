import setuptools

setuptools.setup(
    name="trading_dashboard",
    version="0.0.1",
    description="A small example package",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'pymysql',
        'scipy',
        'compress_pickle',
        'validators',
        'bokeh',
        'plotly',
        'numpy',
        'matplotlib',
        'pandas',
        'jupyter'
    ],
)
