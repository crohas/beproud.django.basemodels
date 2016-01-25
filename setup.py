from setuptools import setup, find_packages


requires = [
    "django",
]

setup(
    name="beproud.django.basemodels",
    version="0.0.0",
    packages=find_packages(),
    namespace_packages=[
        "beproud",
        "beproud.django",
    ],
    install_requires=requires,
)
