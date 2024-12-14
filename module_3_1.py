calls = 0

def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    tuple_ = len(string), string.upper(), string.lower()
    print(tuple_)
    count_calls()

def is_contains(string, list_to_search):
    string = string.lower()
    list_to_search = [s.lower() for s in list_to_search]
    if string in list_to_search:
        print(True)
    else:
        print(False)
    count_calls()

string_info('Capibara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN']) # Urban ~ urBAN
is_contains('cycle', ['recycling', 'cyclic']) # No matches
print(calls)