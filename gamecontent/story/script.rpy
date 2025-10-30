label start:
    # Birds Chirping
    scene black
    scene flashback1
    with fade
    scene flashback1
    with fade
    mc_unknown "Start Load Settings About Help Quit"

    mc_unknown "What's your name?"
    
    $ name = renpy.input("Enter Name: \n", length = 32)
    $ name = name.strip()

    if name == "":
        mc_unknown "No name provided."
        mc_unknown "Your name is Quinn."
        $ name = "Quinn"

    with dissolve
    
    scene flashback2
    bff "Hey..."
    bff "hey!"
    bff "Wake up [name], we have to go!"

    scene black
    jump day1
    return