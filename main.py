# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger
from unittest import main

#print(arithmetic_arranger(["32 - 6853", "3801 - 2", "45 + 4003", "123 + 49"], True))
#print(arithmetic_arranger(["3 + 855","3 + 855","3 + 855", "3801 - 2", "45 + 4653", "123 + 49"]))

# Run unit tests automatically
main(module='test_module', exit=False)