# Programming vacancies compare

The script displays data on the average salary of popular programming languages.

Data is taken through the sites API [HH](https://dev.hh.ru/) and [SuperJob](https://api.superjob.ru/).


### How to install
You need Python3 to run scripts.

Download the code from GitHub.

```
git clone https://github.com/kutuzov13/Job_Search.git
```

Install dependencies:

```
pip3 install -r requirements.txt
```

Run the script with the command:

```
python3 future_salary.py
```

The data will be output to the terminal.

## Environment Variables

Some project settings are taken from environment variables.
To define them, create a `.env`.
Write the data there in this format: `VARIABLE=value`.

#### Required variables:
- `TOKEN_SUPER_JOB` - secret key for access [API SuperJob](https://api.superjob.ru/#gettin).

## Libraries used

- [Requests](https://pypi.org/project/requests/) - for API requests

- [Python-Dotenv](https://pypi.org/project/python-dotenv/) - to access environment variables

- [Terminaltables](https://pypi.org/project/terminaltables/) - output to the terminal


### Project Goals
The code is written for educational purposes on online-course for web-developers [devman](https://dvmn.org/modules/).