from collections import Counter
counter = Counter(word_list)
counter.most_common() # [(Dog, 10), (Cat, 5)]
counter.most_common(1) # [(Dog, 10)]


from collections import defaultdict
defaultdict(float) # means the value of the dict should be float

# "detach" is the same as "with torch.no_grad():

str(datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S-%f'))

# download file from web and save
from urllib.request import urlretrieve
urlretrieve(url, filename) # this will download "url" and save in "filename"