python-selenium, behave and pytest UI retesting on carrefour.fr
=============================================================

What Is This?
-------------

This is a simple Python-selenium/behave(python implementation on cumcumber)/pytest a application intended to provide a working ui retesting of carrefour website. The goal is to automate the retesting of the carref.

Important !
-----------

this readme assume you have `chromedriver` and `geckodriver` in your path, if not add it or:

1. modify `features/environment.py` and change `chromedriver` whit `your/chromedriver/path`



How To Install This ?
---------------------

1. get a copy of this directory by git clone it: `git clone https://github.com/zeufack/pk-cf-retest.git`
2. navigate to your copye: `cd pk-cf-retest`.
3. create a virtualenv with this project `python3 -m venv .`.
4. Run `source ./bin/activate ` to start the virtualenv
5. Run `pip install -r requirements.txt` to install dependencies
6. from there you can run `pytest tests/test_carrefour.py` for pytest result 
7. Or run `behave` for behave(python implementation of cumcumber)


Important directory
-------------------

1.`features`: feature description whit `.feature` extension
2.`featurer\steps`: implementation of features steps
3.`pages`: page object that describe the error process
4.`tests`: pytest implementation of test 



