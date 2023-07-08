from vpython import *
from raycast import *
from event import *


# Render
scene = canvas(width=1024, height=768, center=vec(0,0,0), background=vec(.6,.8,.8), range=15, fov=.001)
IMAGE_RES = .01
renderer = Renderer(IMAGE_RES)

# UI
wt_status = Label("Simulation Complete")
scene.append_to_caption("\n\n")

wt_slitN = Label("Slit Count")
slider_slitN = Slider(min=2, max=10, step=1, length=220, bind=event.push_N)
wt_slitN_v = Label(f"{slider_slitN.value()}")
scene.append_to_caption('\n')

wt_slitS = Label("Slit Spacing")
slider_slitS = Slider(min=1, max=1000, step=1, length=220, bind=event.push_S)
wt_slitS_v = Label(f"{slider_slitS.value()} 倍波長")
scene.append_to_caption('\n')

wt_L = Label("Wavelength")
slider_L = Slider(min=380, max=780, step=1, length=220, bind=event.push_L)
wt_L_v = Label(f"{slider_L.value()} nm")
scene.append_to_caption('\n')

wt_D = Label("Distance")
slider_D = Slider(min=100, max=10000, step=1, length=220, bind=event.push_D)
wt_D_v = Label(f"{slider_D.value()} 倍波長")
scene.append_to_caption("\n\n")

btn_simulate = button(text="Simulate", bind=event.push_Sim)
scene.append_to_caption("\n\n\n")


if __name__ == "__main__":
    running = True

    while running:
        if len(event.events) != 0:
            key = event.events[0]
            if key == 'N':
                txt = slider_slitN.value()
                wt_slitN_v.modify(txt)
                renderer.set_('N', txt)
            elif key == 'S':
                txt = slider_slitS.value()
                wt_slitS_v.modify(txt)
                renderer.set_('S', txt*renderer.get_('L'))
            elif key == 'L':
                txt = slider_L.value()
                wt_L_v.modify(txt)
                renderer.set_('L', txt)
            elif key == 'D':
                txt = slider_D.value()
                wt_D_v.modify(txt)
                renderer.set_('D', txt*renderer.get_('L'))
            elif key == "sim":
                wt_status.modify("Simulating")
                renderer.simulate()
                wt_status.modify("Simulation Complete")
            event.pop()