import sys
from sumatra import programs
from sumatra.dependency_finder import python

if __name__ == "__main__":
    print("\n".join(str(d)
                    for d in python.find_dependencies(sys.argv[1], programs.PythonExecutable(None))))
