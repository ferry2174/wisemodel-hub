from setuptools import find_packages, setup


def get_version() -> str:
    rel_path = "src/wisemodel_hub/__init__.py"
    with open(rel_path, "r") as fp:
        for line in fp.read().splitlines():
            if line.startswith("__version__"):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


install_requires = [
    "packaging>=20.9",
    "requests>=2.20.0",
    "tqdm>=4.64.1",
    "urllib3>=1.24.2",
    "python-gitlab>=5.0.0",
]
# SQLAlchemy==1.1.15
# rsa==3.4.2
# redis==3.5.0

extras = {}

extras["torch"] = [
    "torch",
    "safetensors[torch]",
]

# Typing extra dependencies list is duplicated in `.pre-commit-config.yaml`
# Please make sure to update the list there when adding a new typing dependency.
extras["typing"] = [
    "typing-extensions>=4.8.0",
    "types-PyYAML",
    "types-requests",
    "types-simplejson",
    "types-toml",
    "types-tqdm",
    "types-urllib3",
]

extras["quality"] = [
    "ruff>=0.5.0",
    "mypy==1.5.1",
    "libcst==1.4.0",
]

extras["all"] = extras["quality"] + extras["typing"]

extras["dev"] = extras["all"]

setup(
    name="wisemodel_hub",
    version=get_version(),
    author="始智AI",
    author_email="4498237@qq.com",
    description="Client library to download and publish models, datasets and other repos on the wisemodel.cn hub",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="model-hub machine-learning models natural-language-processing deep-learning pytorch pretrained-models",
    license="Apache",
    url="https://github.com/wisemodel/wisemodel-hub",
    package_dir={"": "src"},
    packages=find_packages("src"),
    extras_require=extras,
    python_requires=">=3.8.0",
    install_requires=install_requires,
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    include_package_data=True,
)
