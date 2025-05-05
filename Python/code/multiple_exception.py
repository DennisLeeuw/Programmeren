try:
    f = open('myfile.txt')
    s = f.readline()
except OSError as err:
    print("OS error:", err)
#except ValueError:
#    print("Could not convert data to an integer.")
#except FileNotFoundError:
#    print(f"File not found")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
else:
    try:
        i = int(s.strip())
    except ValueError:
        print("Could not convert data to an integer.")
    f.close()

