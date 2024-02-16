ALL_LETTERS = [chr(ord('a') + i) for i in range(26)]

# https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-pyth
str_input.isnumeric()  # if only numbers
str_input.isalpha()  # if only letters
str_input.isalnum()  # if only letters and numbers

os.path.join(a,b,c...)


mat = np.zeros((n, n))
api_pairs = (p for k in api_dict.keys() for p in combinations(k.split(","), 2))
pair_indices = [(api_to_idx[p[0]], api_to_idx[p[1]]) for p in api_pairs]
pair_indices, counts = np.unique(pair_indices, axis=0, return_counts=True)
rows, cols = zip(*pair_indices)
mat[rows, cols] = counts


from itertools import permutations
perms = list(permutations(range(len(raw_context))))  # very expensive!
# np. mean always computes an arithmetic mean, and has some additional options for input and output (e.g. what datatypes to use, where to place the result). np. average can compute a weighted average if the weights parameter is supplied
np.average(lst) 
np.random.permutation(10)
np.random.permutation(lst)

# read jsonl vs json
# jsonl or list of json
with open(infile) as f:
    results = f.readlines()
results = [json.loads(row) for row in results]

# json
with open(infile) as f:
    json.loads(f.read())

# or if it is a json string
json.loads(j_string)

# init default dict with keys
d = defaultdict(list,{ k:[] for k in ('a','b','c') })

all_apis = dict(sorted(all_apis.items(), key=lambda x: -x[1]))

sorted_apis = sorted(all_apis.items(), key=lambda x: -x[1])
all_apis = collections.OrderedDict(sorted_apis)
import os
os.getcwd()


from datetime import datetime, date, timedelta
from dateutil.parser
def str_to_dt(s):
    if s.endswith("Z"):
        s = s[:-1]
    return parser.parse(s).replace(tzinfo=None)
    
def dt_to_str(dt):
    assert isinstance(dt, datetime)
    return dt.replace(microsecond=0).isoformat(sep="T") + "Z"

def epoch_ms_to_dt(epoch):
    return datetime.fromtimestamp(epoch / 1000)
