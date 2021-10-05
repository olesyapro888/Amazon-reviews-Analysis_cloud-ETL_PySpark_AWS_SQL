from mrjob.job import MRJob

# the class inherits, or takes properties
class Bacon_count(MRJob):
  # an underscore to indicate that we won’t use the second parameter
  def mapper(self, _, line):
    # split() to break the text into a list of words
    for word in line.split():
      # with convert to lowercase
      # When yield is called the function is suspended and returns a value
        if word.lower() == "bacon":
            yield "bacon", 1

# There's a shuffle step that occurs after the mapper. There is no code written for this step, and it occurs because the class inherits from the mrjob library

  def reducer(self, key, values):
    # "self" parameter is used in Python to represent the instance of the class.
    # "key" parameter represents the key of the key-value pair created in the mapper function
    # "values" parameter is a list of values created in the mapper function
    yield key, sum(values)

    # Conventional Python code for running the program
if __name__ == "__main__":
   Bacon_count.run()