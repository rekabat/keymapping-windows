# Requirement
Python 2.x, 3.x

# Directions
1. Add the hex scancodes of the keys you're interested in remapping to "scancodes.json". [This is a decent resource for scancodes](http://msdn.microsoft.com/en-us/library/aa299374(v=vs.60).aspx "Scancodes from Microsoft"). The file already contains a few entries, including NULL which makes a key do nothing.
2. Add the remaps you want to "preferences.json". Format is "PHYSICAL_KEY": "NEW_EFFECT". The demo maps CTRL to CAPS and CAPS to SCROLL LOCK, losing the funcitonality of SCROLL LOCK.
3. Run "generateRegEdit.py". Requires Python 2.x.
4. Run "generatedRegEdit.reg". (Always look at code that modifies your registers, it could easily be malicious! It isn't but it could be.)
5. Restart your computer.

# Revert Changes
Simply run "resetKeymappings.reg" and restart your computer.