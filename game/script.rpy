# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

style phase_button is button:
    size_group "phase"
    idle_background Frame("gui/inactive_phase.png")
    hover_background Frame("gui/active_phase.png")
    xpadding 40
    ypadding 40
    xmargin 5

style phase_button_text:
    text_align 0.5
    color "#8C8ABE"
    hover_color "#ffffff"


# The game starts here.

label start:
    $malePoints = 0
    $femalePoints = 0

screen character_select:
    modal True #prevents things from under the screen from being interacted with.
    
    # background
    add "gui/select.png"
    
    # column
    vbox:
        xalign 0.5
        yalign 0.6
        
        hbox:
            text "Which character do you most identify with?":
                text_align 0.5
                xfill True
                yfill True
                color "#FFC20F"
            
            
        #row of image buttons
        hbox:
            imagebutton:
                xpadding 30
                auto "gui/female_%s.png"
                action SetVariable("femalePoints", femalePoints + 1), Return()
                focus_mask True
            imagebutton:
                xpadding 30
                auto "gui/male_%s.png"
                action SetVariable("malePoints", malePoints + 1), Return()
                focus_mask True

screen phase_select:
    modal True #prevents things from under the screen from being interacted with.
    
    # background
    add "gui/select.png"
    
    # column
    vbox:
        xalign 0.5
        yalign 0.2
        
        hbox:
            text "Select a Phase or Start from the Beginning":
                text_align 0.5
                xfill True
                yfill True
                color "#FFC20F" 

    vbox: 
        xalign 0.5
        yalign 0.35  
        #row of image buttons
        hbox:
            textbutton "Phase 1\nConsultation":
                action Jump("p1")
                style style.phase_button
            textbutton "Phase 2\nSimulation Scan":
                action Jump("p2")
                style style.phase_button
            textbutton "Phase 3\nPlanning":
                action Jump("p3")
                style style.phase_button
            textbutton "Phase 4\nTreatment":
                action Jump("p4")
                style style.phase_button
    
    vbox:
        xalign 0.5
        yalign 0.6  
        #row of image buttons
        hbox:
            textbutton "Start at the Beginning":
                action SetVariable("malePoints", malePoints + 1), Return()
                background Frame("gui/beginning.png")
                xpadding 50
                ypadding 20
                xmargin 20
                text_size 20
                text_text_align 0.5
                text_color "#ffffff"

label chrsel:
    $ renpy.call_screen("character_select")

    if malePoints ==1:
        "Boy" "I am a boy"

    if femalePoints == 1:
        "Girl" "I am a girl"
        
    $ renpy.call_screen("phase_select")

    # This ends the game.

label p1:
    "Narrator" "Phase 1: Consultation."

label p2:
    "Narrator" "Phase 2: Simulation Scan."

label p3:
    "Narrator" "Phase 3: Planning."

label p4:
    "Narrator" "Phase 4: Treatment."


    return
