import traceback
import sys
try:
    raise ValueError
except ValueError:
    tb = traceback.format_exc()
    
else:
    tb = "No Error"
finally:
    print("Finally Block")