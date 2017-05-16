class QueryPreprocessor(object):
    def process(self, query):
        # remove all of
        temp_query = query
        temp_query.replace("find ", "")
        temp_query.replace(" of ", "")
        temp_query.replace("step ", "step")

        processed = temp_query.split(" ")

        return processed