from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as f:
    readme = f.read()

setup(
    name="AIR_Bench",
    version="0.1.0",
    description="AIR-Bench: Automated Heterogeneous Information Retrieval Benchmark",
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email="zhengliu1026@gmail.com",
    url="https://github.com/AIR-Bench/AIR-Bench",
    packages=find_packages(),
    install_requires=[
        'datasets>=2.18.0',
        'mteb>=1.7.17',
        'torch>=1.6.0',
        'transformers>=4.33.0',
    ]
)
