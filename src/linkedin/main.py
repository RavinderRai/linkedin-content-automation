#!/usr/bin/env python
import sys
from linkedin.crew import LinkedinCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'description_of_you': input('Enter a description of yourself and your brand here: ')
    }
    LinkedinCrew().crew().kickoff(inputs=inputs)
