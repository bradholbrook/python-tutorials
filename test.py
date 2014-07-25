#!C:\Python27

import sys

#Define a function to do things
def repeat(s, ex):
  """This function repeats some things
  """
  result = s * 3
  if ex:
    result = result + '!'
  return result

def main():
  print 'Hello ' + sys.argv[1]
  print repeat('hello ', True)
  print 'hello'

if __name__ == '__main__':
  main()