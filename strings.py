try:
    suppose = [i for i,x in enumerate("harshitha") if i%2 == 4]
    print(suppose) # [0,2,4,6,8]
    print(suppose[:-3:-1]) # []
    print(suppose[100])
except ValueError:
    print("There is an error please look at you input code are change the code")
except TypeError:
    pass
except KeyError:
    pass
except IndexError:
    pass
except ImportError as imperr:
    print("There is no module you want to access please use pip for installing", imperr)
except Exception as error:
    print("some error")
except IndentationError:
    print("some code is not intendet propely please look into it")
except SyntaxError:
    print("some some error")