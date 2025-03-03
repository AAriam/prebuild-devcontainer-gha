def is_python_3_12():
    try:
        s = f"{f"{f"{f"{f"{f"{1+1}"}"}"}"}"}"
    except:
        return False
    return True

def main():
    if is_python_3_12():
        print("Python 3.12")
    else:
        print("Not Python 3.12")

if __name__ == "__main__":
    main()
