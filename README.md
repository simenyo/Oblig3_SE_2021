# Oblig3_SE_2021
In this repository i have added Github actions to automatically run the tests for the isleapyear function. After some trying and failing i've got it working.
The problem I had was from the structure in my project. The error i got running the tests were  ModuleNotFoundError, resulting from the import of the function to the test file.
After restructuring the project i got everything running, and the tests pass!

I used the workflow package python-package.yml, which runs the tests in python 3.7, 3.8, and 3.9. 
