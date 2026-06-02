from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="kairos-scheduler",
    version="0.1.0",
    description="Industrial Job Shop Scheduling Library with OR-Tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kairos Team",
    url="https://github.com/kairos-scheduler/kairos",
    packages=find_packages(exclude=["tests*", "venv*"]),
    python_requires=">=3.8",
    install_requires=[
        "ortools>=9.0",
        "pandas>=1.3",
        "plotly>=5.0",
        "openpyxl>=3.0",
    ],
    extras_require={
        "gui": ["streamlit>=1.28"],
    },
    entry_points={
        "console_scripts": [
            "kairos-gui=kairos.gui.__main__:run_gui",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
    ],
    keywords="scheduling, job-shop, optimization, or-tools, manufacturing",
)

