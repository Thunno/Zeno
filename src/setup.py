from setuptools import setup, find_packages

ZENO_VERSION = "0.1"

long_description = (
    "Zeno is an intepreter for Thunno 2. Read more at https://github.com/Thunno/Zeno"
)

setup(
    name="thunno-zeno",
    version=ZENO_VERSION,
    license="CC0",
    description="Thunno 2 interpreter",
    author="Rujul Nayak",
    author_email="rujulnayak@outlook.com",
    url="https://github.com/Thunno/Zeno",
    download_url=f"https://github.com/Thunno/Zeno/archive/refs/tags/v{ZENO_VERSION}.tar.gz",
    keywords=["golfing", "code-golf", "language"],
    install_requires=["thunno2", "getkey"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=find_packages(),
    entry_points={"console_scripts": ["zeno = zeno.main:main"]},
)
