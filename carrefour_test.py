#!/home/zeufack/Documents/programming/python/test_carrefour/bin/python3 

import subprocess
import os

test_folder = "/home/zeufack/Documents/programming/python/test_carrefour"
repport_cmd = "behave -f allure_behave.formatter:AllureFormatter -o allure/results ./features"
display_cmd = "allure serve allure/results"

def mv_to_test(test_folder):
    os.chdir(test_folder)

def generate_repport(repport_cmd):
    subprocess.run(["rm", "*", "allure/results/"])
    subprocess.run([n for n in repport_cmd.split(' ')])

def display_repport(display_cmd):
    subprocess.run([n for n in display_cmd.split(' ')])


mv_to_test(test_folder)
generate_repport(repport_cmd)
display_repport(display_cmd)

