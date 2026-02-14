

from setuptools import setup, find_packages

def get_requirements()-> list[str]:
    requirement_lst: list[str] = []
    try:
        with open('requirement.txt') as f:
            lines =  f.readlines()

            for line in lines:
                line = line.strip()
                if line and line!="-e .":
                    requirement_lst.append(line)
    except Exception as e:
        print(f"Error while reading requirement.txt: {e}")
    return requirement_lst

setup(
    name='network_security',
    version='0.1.0',
    packages=find_packages(),
    install_requires=get_requirements(),
    description='A package for network security analysis and monitoring.',
    author='Harshith Davanamsubbaramaiah',
    author_email='dsh819@gmail.com')