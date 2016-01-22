from setuptools import setup, find_packages


requires = [
    "django",
]

setup(
    name="beproud.django.basemodels",
    packages=find_packages(),
    namespace_packages=[
        "beproud",
        "beproud.django",
    ],
    install_requires=requires,
)
