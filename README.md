# tile-engine

source env/bin/activate


pip install -r requirements.txt

python src/main.py

TO DO List: 
1. Ctrl shift I thing to automatically fix spacing stuff. 
2. Clean up import so that they don’t have *. Only import functions 
3. Exception Handling
4. Logging
5. Result Codes 
6. Validating Engine inputs
7. Strong typing / hybrid? Not sure? Research pros and cons. Might not be worth doing. 
8. Unit Testing - PyTest
9. Integration Testing
10. Acceptance Testing
11. Delete images we downloaded once we are done with them. Clean up functions for each engine call (assembler, downloader, etc.)
12. Bbox edge cases: lon and lat across prime meridian /equator. How are those handled. 
13. Think of better way to separate engine_utils into multiple utils. 


14. FIll in ValueValidator Class
