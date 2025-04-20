# activation and deactivation of venv in both windows and linux

## installing venv module
```bash
sudo apt install python3.10-venv
```

## venv in linx

- to initialize venv in linux we use `venv` command

```bash

python3 -m venv venv

```

- you will see a folder called venv in the directory you are working in

### activation of venv in linux

- what we do is

```bash

source venv\bin\activate

```

### deactivation of venv

- we type the command `deactivate`

```bash

# deactivating the venv

deactivate

```

### using venv

- the mainusage of venv is to create an isolated virtual enviroment to run our program and to install dependeces without altering any other packages in the device

- to install our packages we use `pip`

```bash

pip install pandas numpy

```

```bash

pip install fastapi uvicorn

```

- pip is a package manager working on python

## venv on windows

- activating venv on windows

```bash

venv\Scripts\activate

```

- deactivating the venv

```bash

deactivate

```

# requirments of the venv

- we can install any package on the venv

- to see all packages we installed we will use `freeze` command

```bash

pip freeze

```

- it will show us all requirments and the versions

## in order to make it more convienient

- we will direct the output to a file called requirments

```bash

pip freeze > requirments.txt

```

> [!NOTE]
> we need to update the requirments file every time we install a new library

## installing requirments

- we can pass the file to any user without our venv and then the user will intall all requirments

- to install all requirments we will do

```bash

pip install -r requirments.txt

```

# another way for venv

- we willinstall `pipenv` command on our local machine

```bash

# installing pipenv

pip install pipenv

```

## lets talk about `pipenv`

- `pipenv` is a command used for the installing and maintaining packages in the venv

- `pipvenv` automate the work you will do using the `pip` command and activating the venv

## installing packages by `pipenv`

```bash

# installing packages using venv

pipenv install fastapi

```

- what will happen is the `pipenv` command will create `pipfile` that contain all the information about packages

- another file is `Pipfile.lock` that have all instructions to the venv and the packages

## run the venv

- running the venv created by the command `pipenv` , we will use `pipenv run` or `pipenv shell`

```bash

# running the venv using pipenv run

pipenv run python3 main.py

```

```bash

# running the venv using thecommand pipenv shell

pipenv shell # will run the venv shell

```

### run venv for another device

- we use `pipenv install`

```bash

pipenv install

```

- this will automatically download dependencies

## installing for dev
- **dev packages** typically source files such as headers that may be required for other programs to develop and build applications related to that package.
- we use `--dev` option

```bash

# installing adeveloper package

pipenv install --dev pytest

```

## running the dev version

- by running `pipenv shell` + `--dev`

```bash

# running the dev version

pipenv install --dev

```

## exit the environment

```bash

exit

```

# uninstalling packages

- we use `uninstall`

```bash

# uninstalling packages

pipenv uninstall fastapi

```

# updating packages

-we use command `pipenv lock`

```bash

# updating lock file

pipenv lock

```