label day1:
    
    scene black
    with dissolve

    play sound "audio/alarmclock.mp3" volume 0.5
    $ renpy.pause(2.25, hard=True)
    mc_known "Man, what time is it?"
    
    scene bedroom1
    with fade
    mc_known "(Dammit late again)"


    return
    # 1920x1080