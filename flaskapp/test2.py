import sys
sys.path.append('../src/')

from test import get_results
from htmlify import htmlify

results = get_results(44121)
print(htmlify(results))
