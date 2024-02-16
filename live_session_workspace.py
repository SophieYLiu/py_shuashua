from dateutil import parser
import collections
import json

class Query:

    def __init__(self, time_str, search_phrase, loc):
        self.time_str = time_str
        self.search_phrase = search_phrase
        self.loc = loc
        self.time_epoch = self.convert_str_time_to_epoch(time_str)

    @staticmethod
    def convert_str_time_to_epoch(time_str):
        return parser.parse(time_str).timestamp()

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

if __name__ == "__main__":


    # with open("DATA_IN_PATH") as f:
    #     data = f.readlines()
    #
    # with open('DATA_OUT_PATH', 'w') as f:
    #     f.write(json.dumps(logs) + '\n')


    logs = ["2009-03-08T00:28:31.807Z query1 beijing", "2009-03-08T00:27:31.807Z query2 shanghai",
            "2009-03-08T00:27:31.807Z query3 seattle", "2009-03-08T00:27:31.807Z query4 xian",
            "2009-03-08T00:29:31.807Z query5 taipei", "2009-03-08T01:27:31.807Z query6 beijing"]

    queries = []

    for log in logs:
        time, search, loc = [each.strip() for each in log.split(' ')]
        query = Query(time_str=time, search_phrase=search, loc=loc)
        queries.append(query)

    queries.sort(key=lambda q: q.time_epoch)

    sessions = []
    DELTA_IN_SEC = 30
    i = 0
    while i < len(queries):
        prev = queries[i]
        session = []
        while i < len(queries) and queries[i].time_epoch - prev.time_epoch < DELTA_IN_SEC:
            session.append(queries[i])
            prev = queries[i]
            i += 1
        if session:
            popular_locs = collections.Counter([each.loc for each in session]).most_common()
            popular_searches = collections.Counter([each.search_phrase for each in session]).most_common()
            sessions.append(session)

    for i, session in enumerate(sessions):
        print(f"{'*'*20} This session {i} {'*'*20}")
        for q in session:
            print(q.to_json())
