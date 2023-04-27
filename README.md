# Credit Cards Simulator

This project is meant to simulate a sort-of bank systemthat receives operations via a txt file and process them against their credit records per individual.

## Design Overview

My design for developing was mainly thought to stick with functional programming because there is no need to create objects in this situation. However, for scalability and readability reasons I decided to create one object which is a user. It holds all its relevant pieces of information plus methods that modify them. This way we can keep user methods (charge, credit) from bank methods (run transactions, run tests, add user).

## Why did I choose python for this?

I chose to develop this with python because it personally is my strongest programming language. Whenever I need to develop something that's not runtime-sensible I always choose Python for its scalability and universality mainly because it's also easy to read, maintain and replicate.

Finally, it has many open-source libraries that helped me easily validate credit cards with Luhn 10 algorithm.

## How to install dependencies?

As mentioned on the design overview, the only external module used is luhn-validator found [here](https://pypi.org/project/luhn-validator/)

To install this, you only need to be inside the repo folder and run via terminal:
```
pip install -r requirements.txt
```

## Pre-requisites

1. Have Python 3.5 or greater installed on your machine. If you don't have it download it [here](https://www.python.org/downloads/)
2. Have pip installed. Check whether you have it or install it? Check this guide [here](https://www.geeksforgeeks.org/download-and-install-pip-latest-version/)

## How to run the project?

### Running all tests

0. Check you have all the necessary tools mentioned in "Pre-requirements" section above.
1. Open your terminal and access the repo (if you do not know how, check [this guide](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands/))
2. Run: `python -c "import main; main.run_tests()'"
3. Tests' output should be now printed on your cmd!

### Running specific test

0. Check you have all the necessary tools mentioned in "Pre-requirements" section above.
1. Open your terminal and access the repo (if you do not know how, check [this guide](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands/))
2. Open your file explorer, go to the repo folder and add your test file (in txt format) to the Tests directory
3. Run: `python -c "import main; main.run_specific_test('my_file.txt')"`
4. Your output should be now printed on your cmd!

### Run program as python main.py

0. Check you have all the necessary tools mentioned in "Pre-requirements" section above.
1. Open your terminal and access the repo (if you do not know how, check [this guide](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands/))
2. Open your file explorer, go to the repo folder and add your file in the same scope as the main.py. The txt file has to be strictly named "input.txt"
3. Run: `python main.py`
4. Your output should be now printed on your cmd!
